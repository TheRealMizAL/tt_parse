from .abc import AbstractDocument

__all__ = ("WordDocument", "ExcelDocument")


class WordDocument(AbstractDocument):

    async def parse(self):
        # todo: end this method
        return 'word parser'


class ExcelDocument(AbstractDocument):

    async def parse(self):
        # todo: end this method
        return 'excel parser'
