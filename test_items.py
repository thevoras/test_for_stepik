import time
from selenium import webdriver

def test_is_button_on_page(browser):

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    
    button1 = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    button1_check = button1.get_attribute("type")
    assert button1_check == "submit", "Element 'Button' is no on this page"
