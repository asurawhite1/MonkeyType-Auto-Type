from playwright.sync_api import sync_playwright
import time

def auto():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        page.goto('https://monkeytype.com') 
        page.wait_for_selector('.word')
        input("press enter to start, make sure to clean any gui on screen ! : ")
        words = page.query_selector_all('.word')
        for word in words:
            word_text = word.inner_text()
            for letter in word_text:
                page.type('body', letter)
                time.sleep(0.05)
            page.type('body', ' ')
            time.sleep(0.05)
            print(word_text)
        time.sleep(2)
        browser.close()
if __name__ == '__main__':
    auto()
