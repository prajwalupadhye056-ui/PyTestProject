

def test_playwrightBasics(playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context() #do some operations login
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com")







