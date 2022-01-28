import asyncio
import re

if __name__ == '__main__':
    from file_parsers import ExcelDocument, WordDocument
    from file_parsers.abc import AbstractDocument
else:
    from .file_parsers import ExcelDocument, WordDocument
    from .file_parsers.abc import AbstractDocument
from exceptions.parser_exceptions import WrongDocumentTypeException, NotFileLinkException
from aiohttp import ClientSession

__all__ = "DocumentParser"


class DocumentParser:

    def __init__(self, link: str):
        self.__link = link
        self.__document: AbstractDocument
        try:
            self.__doc_type = link.split('.')[-1]
            if not re.match('https://permaviat\.ru/_res/fs/\d+?file\.\w+', self.__link):
                raise NotFileLinkException(f'{self.__link} is not file link or has wrong type')
        except AttributeError:
            raise NotFileLinkException(f'{self.__link} is not file link or has wrong type')

        if self.__doc_type == 'xls':
            self.__document = ExcelDocument()
        elif self.__doc_type == 'docx':
            self.__document = WordDocument()
        else:
            raise WrongDocumentTypeException(
                f'Passed document should be "docx" type or "xls", not {self.__doc_type}')

    async def find_changes(self):
        await asyncio.sleep(0.5)
        return await self.__document.parse(await self.__bytes_file)

    @property
    async def __bytes_file(self):
        async with ClientSession() as session:
            async with session.get(self.__link) as resp:
                if resp.status == 200:
                    return await resp.read()


if __name__ == '__main__':
    asyncio.run(DocumentParser('https://permaviat.ru/_res/fs/2452file.docx').find_changes())
