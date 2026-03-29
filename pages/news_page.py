import time
from selenium.webdriver.common.by import By

class News_Page:
    def __init__(self,driver):
        self.driver=driver
        self.manage_news_tile_locator=(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news']")
        self.home_link_locator=(By.XPATH, "//a[text()='Home']")
        self.new_option_locator=(By.CSS_SELECTOR, ".btn.btn-rounded.btn-danger")
        self.enter_news_locator=(By.XPATH, "//textarea[@id='news']")
        self.save_news_locator=(By.CSS_SELECTOR, "button[name='create']")
        self.search_news_option_locator=(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
        self.enter_news_for_search_locator=(By.XPATH, "//input[@class='form-control']")
        self.search_news_locator=(By.CSS_SELECTOR, ".btn.btn-danger.btn-fix")

#moved to home_page.py
#    def click_on_manage_news_tile(self):
#        self.driver.find_element(*self.manage_news_tile_locator).click()
    def click_on_home_link(self):
        self.driver.find_element(*self.home_link_locator).click()
        return self
    def click_on_news_option(self):
        self.driver.find_element(*self.new_option_locator).click()
        return self
    def enter_news(self):
        self.driver.find_element(*self.enter_news_locator).send_keys("India won T20 World Cup")
        return self
    def save_news(self):
        self.driver.find_element(*self.save_news_locator).click()
        return self
    def search_news_option(self):
        self.driver.find_element(*self.search_news_option_locator).click()
        return self
    def enter_news_for_search(self,message):
        self.driver.find_element(*self.enter_news_for_search_locator).send_keys(message)
        return self
    def search_news(self):
        self.driver.find_element(*self.search_news_locator).click()
        return self








