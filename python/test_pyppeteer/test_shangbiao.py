import asyncio
from pyppeteer import launch

async def main():
    # exepath = r'C:\Users\Administrator\AppData\Local\pyppeteer\pyppeteer\local-chromium\575458\chrome-win32/chrome.exe'
    exe_path = '/Users/long/Downloads/chrome-mac/Chromium.app/Contents/MacOS/Chromium'
    options = {'executablePath': exe_path}
    browser = await launch(options)
    page = await browser.newPage()
    await page.goto('http://wcjs.sbj.cnipa.gov.cn/txnT01.do')
    await page.screenshot({'path': 'test_example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())