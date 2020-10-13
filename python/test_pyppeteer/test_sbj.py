                # -*- coding: utf-8 -*-
import asyncio
from pyppeteer import launch

from pyppeteer import launcher

from python.test_pyppeteer.common import ProxyService
# from common import ProxyService

launcher.DEFAULT_ARGS.remove("--enable-automation")

exe_path = '/Users/long/Downloads/chrome-mac/Chromium.app/Contents/MacOS/Chromium'
options = {'executablePath': exe_path}

proxy_service = ProxyService()
proxy = proxy_service.get_alive_proxy()
# 5. 获取商标流程页面
proxies = {"http": "http://hexin:hx300033@%s:%s" % (proxy['Ip'], proxy['Port']),
           'https': "http://hexin:hx300033@%s:%s" % (proxy['Ip'], proxy['Port'])}


async def main(reg_num, int_cls):
    browser = await launch({
        'executablePath': exe_path,
        'headless': False,
        # 'headless': True,
        # 'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox'],
        # 'args': ['--disable-infobars', '--window-size=2560,1600', '--no-sandbox'],
        'args': ['--disable-infobars', '--no-sandbox', '-–proxy-server=' + proxies['http']],
    })
    page = await browser.newPage()
    # await page.setViewport({'width': 1920, 'height': 1080})
    # await page.setViewport({'width': 2560, 'height': 1600})
    await page.goto("http://wcjs.sbj.cnipa.gov.cn/")
    await asyncio.sleep(3)

    await page.click("#txnS03", delay=0.2)
    await asyncio.sleep(3)

    # await page.type('.input', '46023667')
    await page.type('.input', reg_num)
    await asyncio.sleep(3)

    await page.click('#_searchButton', delay=0.2)


    await asyncio.sleep(3)
    print('halaha')
    content = await page.content()
    print(content)
    print('hasdfsd')

    pages = await page.browser.pages()
    print(len(pages))
    for temp_page in pages:
        if 'http://wcjs.sbj.cnipa.gov.cn/txnRead01.do' in temp_page.url:
            page = temp_page
            await page.bringToFront()
            break
    content = await page.content()
    print(content)
    await asyncio.sleep(3)

    await asyncio.gather(
        page.waitForNavigation({}),
        page.click('a[onclick^="goDetail"]', {}),
    )
    # await page.click('a[onclick^="goDetail"]')

    # elements = await page.querySelectorAll('tr')
    # print(elements)
    # await asyncio.sleep(1)
    # x = None
    # x = await elements[1].JJ('td')
    # await asyncio.gather(
    #     page.waitForNavigation({}),
    #     x[4].click({}),
    # )
    await asyncio.sleep(4)
    # for element in elements[1:]:
    #     x = await element.JJ('td')
    #     value = await (await x[2].getProperty('textContent')).jsonValue()
    #     print(value)
    #     print(x)
    #     temp = await (await x[4].getProperty('textContent')).jsonValue()
    #     print(temp)
    #     if value == str(int_cls):
    #         print('ddd')
    #         await x[4].click(delay=0.2)
    #         await asyncio.gather(
    #             page.waitForNavigation({}),
    #             x[4].click(delay=0.2),
    #         )
    #         break
    print('ccc')
    # print(x)
    # await asyncio.gather(
    #     page.waitForNavigation({}),
    #     x[4].click(delay=0.2),
    # )
    # temp = await x[4].click(delay=0.2)
    # print(temp)
    content = await page.content()
    print(content)
    pages = await page.browser.pages()
    print(len(pages))
    await asyncio.sleep(1)
    await asyncio.gather(
        page.waitForNavigation({}),
        page.click('#txnDetail', {}),
    )
    content = await page.content()
    print(content)
    await asyncio.sleep(100)
    # # await browser.close()

reg_num = '50129033'
int_cls = 43
asyncio.get_event_loop().run_until_complete(main(reg_num, int_cls))
