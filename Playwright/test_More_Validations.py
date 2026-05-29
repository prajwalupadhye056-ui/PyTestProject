import time

from playwright.sync_api import Page, expect

#hide/display and placeholder
def test_UIchecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


    #Alertboxes
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click() #Alert box will open
    time.sleep(5)


   #Mouse hover

    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    
   #Framehandling
    pageframe= page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link", name="All Access plan").click()
    expect(pageframe.locator(".body")).to_have_text("Happy Subscribers")


    #check the price of rice is equal to 37
    #identify price column
    #identity rice row
    #extract the price of rice

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")


    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue=index;
            print(f"Price column is value {priceColValue} ")
            break

    ricerow = page.locator("tr").filter(has_text="Rice")
    expect (ricerow.locator("td").nth(priceColValue)).to_have_text("37")



    










