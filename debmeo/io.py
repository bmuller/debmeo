import aiohttp


async def get_page(url):
    agent = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 "
    agent += "(KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
    headers = {'User-Agent': agent}

    body = bytes()
    with aiohttp.Timeout(10):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url) as response:
                chunk = await response.content.read(1024)
                while chunk and len(body) < 3000000:
                    body += chunk
                    chunk = await response.content.read(1024)
                if not response.content.at_eof():
                    return None
                # pylint: disable=protected-access
                response._content = body
                body = await response.text()
    return body
