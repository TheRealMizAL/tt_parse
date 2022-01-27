import re

from .file_parsers import *
from .abc import AbstractDocument
from exceptions.parser_exceptions import WrongDocumentTypeException, NotFileLinkException

__all__ = "DocumentParser"


class DocumentParser:

    def __init__(self, link: str):

        self.__document: AbstractDocument
        try:
            self.__doc_type = link.split('.')[-1]
            if not re.match('https://permaviat\.ru/_res/fs/\d+?file\.\w+', link):
                raise NotFileLinkException(f'{link} is not file link or has wrong type')
        except AttributeError:
            raise NotFileLinkException(f'{link} is not file link or has wrong type')

        match self.__doc_type:
            case 'xls':
                self.__document = ExcelDocument()
            case 'docx':
                self.__document = WordDocument()
            case _:
                raise WrongDocumentTypeException(
                    f'Passed document should be "docx" type or "xls", not {self.__doc_type}')

    async def find_changes(self):
        return await self.__document.parse()
