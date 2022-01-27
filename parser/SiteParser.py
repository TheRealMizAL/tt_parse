from aiohttp import ClientSession
from hashlib import md5
import asyncio
from bs4 import BeautifulSoup
from doc_parser import DocumentParser


class SiteParser:

    def __init__(self, url):
        self.url: str = url

    async def run_forever(self):
        """
        Check for updates on site every 30 minutes forever.
        Also start parsing if update found.
        :return: None
        """
        prev_hash: str | None = None
        while True:
            async with ClientSession() as session:
                async with session.get(self.url) as response:
                    text = await response.text()
                    site_hash = md5(bytes(text.encode('utf-8'))).hexdigest()

                    if site_hash != prev_hash:  # comparing only checksums of site. If changed, start parsing
                        await self.__parse_site(text)
                    prev_hash = site_hash
            await asyncio.sleep(30*60)

    async def __parse_site(self, text):
        """
        Hardcoded af parser for only site in this world.
        Searches only first document on the site.
        :param text: html of site.
        :return: None
        """
        soup = BeautifulSoup(text, 'lxml')
        first_doc_raw = soup.find('div', {'class': 'file_link'})
        first_doc_url = '/'.join(self.url.split('/')[:3]) + first_doc_raw.find('a')['href']

        print(first_doc_url)
        await DocumentParser(first_doc_url).find_changes()


if __name__ == '__main__':  # for debug only!!!
    asyncio.run(SiteParser('https://permaviat.ru/raspisanie-zamen/').run_forever())