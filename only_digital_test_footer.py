
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.context.tracing.start(
        screenshots=True,  
        snapshots=True,   
        sources=True      
    )
    endpoints=["","company","projects","fields","blog"]
    for endpoint in endpoints:
        page.goto("https://only.digital/"+ endpoint, wait_until="load") 
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        expect(page.locator("footer")).to_be_visible()
        expect(page.get_by_text("Начать проектbedptgvkTelegram")).to_be_visible()
        expect(page.locator("footer").get_by_role("button", name="Начать проект")).to_be_visible()
        expect(page.get_by_text("Создаем digital-продукт на базе стратегии, креатива и технологий")).to_be_visible()
        expect(page.locator("footer").get_by_role("img")).to_be_visible()
        expect(page.locator("footer").get_by_role("img").locator("path").first).to_be_visible()
        expect(page.locator("footer").get_by_role("img").locator("g path")).to_be_visible()
        expect(page.locator("footer").get_by_role("img").locator("path").nth(2)).to_be_visible()
        expect(page.locator("footer").get_by_role("link", name="hello@only.digital")).to_be_visible()
        expect(page.locator("footer").get_by_role("link", name="+7 (495) 740 99")).to_be_visible()
        expect(page.get_by_role("main").get_by_text("Telegram для связи", exact=True)).to_be_visible()
        expect(page.locator("footer").get_by_role("link", name="@onlydigitalagency")).to_be_visible()
        expect(page.locator("footer").get_by_role("link", name="pdf")).to_be_visible()
        expect(page.locator("footer").get_by_role("link", name="pitch")).to_be_visible()
        expect(page.get_by_role("main").get_by_text("Презентация компании", exact=True)).to_be_visible()
        expect(page.get_by_role("paragraph").filter(has_text="© 2014 -")).to_be_visible()
        expect(page.get_by_role("link", name="be", exact=True)).to_be_visible()
        expect(page.get_by_role("link", name="dp")).to_be_visible()
        expect(page.get_by_role("link", name="tg")).to_be_visible()
        expect(page.get_by_role("link", name="vk", exact=True)).to_be_visible()
        expect(page.get_by_text("creative digital production", exact=True)).to_be_visible()
        expect(page.get_by_role("main").get_by_text("bedptgvk")).to_be_visible()
        expect(page.get_by_role("paragraph").filter(has_text="© 2014 -")).to_be_visible()
        expect(page.get_by_role("main").get_by_text("pdfpitchПрезентация компании", exact=True)).to_be_visible()
        expect(page.locator("footer").get_by_text("hello@only.digital+7 (495)")).to_be_visible()

    page.context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
