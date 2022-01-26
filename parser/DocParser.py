from abc import ABC, abstractmethod


class AbstractDocument(ABC):
    """
    Base class for all types of documents
    """
    @abstractmethod
    async def parse(self):
        pass


class WordDocument(AbstractDocument):

    async def parse(self):
        pass  # todo: end this method


class ExcelDocument(AbstractDocument):

    async def parse(self):
        pass  # todo: end this method


class DocumentParser:

    def __init__(self, link: str):

        self.__document: AbstractDocument
        match link.split('.')[-1]:
            case 'xls':
                self.__document = ExcelDocument()
            case 'docx':
                self.__document = WordDocument()
            case _:
                pass

    async def find_changes(self):
        await self.__document.parse()
