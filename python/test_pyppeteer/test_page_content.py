# -*- coding: utf-8 -*-
import asyncio
from pyppeteer import launch

from pyppeteer import launcher
launcher.DEFAULT_ARGS.remove("--enable-automation")

exe_path = '/Users/long/Downloads/chrome-mac/Chromium.app/Contents/MacOS/Chromium'
options = {'executablePath': exe_path}

async def main():
    browser = await launch({
        'executablePath': exe_path,
        'headless': False,
        # 'headless': True,
        # 'args': ['--disable-infobars', '--window-size=1920,1080', '--no-sandbox'],
        # 'args': ['--disable-infobars', '--window-size=2560,1600', '--no-sandbox'],
        'args': ['--disable-infobars', '--no-sandbox'],
    })
    page = await browser.newPage()
    # await page.setViewport({'width': 1920, 'height': 1080})
    # await page.setViewport({'width': 2560, 'height': 1600})
    await page.goto("http://www.robinjia.org/")
    content = await page.content()
    print(content)


asyncio.get_event_loop().run_until_complete(main())