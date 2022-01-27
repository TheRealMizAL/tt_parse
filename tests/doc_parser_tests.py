from parser.doc_parser import DocumentParser
from exceptions.parser_exceptions import WrongDocumentTypeException, NotFileLinkException
import pytest


@pytest.mark.asyncio
async def test_docx():
    result = await DocumentParser('https://permaviat.ru/_res/fs/2457file.docx').find_changes()
    assert result == 'word parser'


@pytest.mark.asyncio
async def test_xls():
    result = await DocumentParser('https://permaviat.ru/_res/fs/2457file.xls').find_changes()
    assert result == 'excel parser'


@pytest.mark.asyncio
async def test_wrong_type():
    with pytest.raises(WrongDocumentTypeException):
        await DocumentParser('https://permaviat.ru/_res/fs/2457file.png').find_changes()


@pytest.mark.asyncio
async def test_wrong_value():
    with pytest.raises(NotFileLinkException):
        await DocumentParser(123).find_changes()


@pytest.mark.asyncio
async def test_none_value():
    with pytest.raises(NotFileLinkException):
        await DocumentParser(None).find_changes()

@pytest.mark.asyncio
async def test_wrong_link():
    with pytest.raises(NotFileLinkException):
        await DocumentParser('smakldmklsdkfm').find_changes()