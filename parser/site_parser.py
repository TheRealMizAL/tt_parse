import asyncio

from aiohttp import ClientSession
from bs4 import BeautifulSoup
from exceptions.parser_exceptions import ResponseCodeException


class SiteParser:

    def __init__(self, url):
        self.url: str = url

    @property
    async def __get_site(self) -> str:  # this might be useful in future
        async with ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    raise ResponseCodeException(f'Response not 200 ({response.status})')

    async def last_file(self) -> str:

        soup = BeautifulSoup(await self.__get_site, 'lxml')
        first_doc_raw = soup.find('div', {'class': 'file_link'})
        first_doc_url = '/'.join(self.url.split('/')[:3]) + first_doc_raw.find('a')['href']

        await asyncio.sleep(0.1)  # idk why, but without this pause code crashes
        return first_doc_url


if __name__ == '__main__':
    print(asyncio.run(SiteParser('https://permaviat.ru/raspisanie-zamen/').last_file()))
