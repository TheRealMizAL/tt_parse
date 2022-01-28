from .abc_exceptions import BaseParserException


class WrongDocumentTypeException(BaseParserException):
    pass


class NotFileLinkException(BaseParserException):
    pass


class ResponseCodeException(BaseParserException):
    pass