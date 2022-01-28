from parser.site_parser import SiteParser
import pytest


@pytest.mark.asyncio
async def test_last_file():
    link = await SiteParser('https://permaviat.ru/raspisanie-zamen/').last_file_link()
    assert link == 'https://permaviat.ru/_res/fs/2457file.xls'
