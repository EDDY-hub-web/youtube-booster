import asyncio
from playwright.async_api import async_playwright

async def run_bot(url):
    async with async_playwright() as p:
        # Gufungura browser imeze nka Chrome yo muri USA
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        page = await context.new_page()
        
        print(f"Iri kureba videwo: {url}")
        await page.goto(url)
        
        # Kureba videwo mu minota 10 (600 seconds)
        await asyncio.sleep(600) 
        
        await browser.close()

# Shyiramo link ya videwo yawe hano
asyncio.run(run_bot("https://www.youtube.com/watch?v=YOUR_VIDEO_ID"))
