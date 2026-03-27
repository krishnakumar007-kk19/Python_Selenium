from selenium.webdriver.common.by import By

from pages.admin_page import Admin_page
from pages.login_page import Login_Page
from pages.news_page import News_Page


class Home_page:
    def __init__(self,browser):
        self.driver=browser
        self.admin_tile_locator=By.XPATH, "//a[@data-toggle='dropdown']"
        self.logout_locator=By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/logout']"

    def click_admin(self):
        # locate Admin
        self.driver.find_element(*self.admin_tile_locator).click()
        return self
    def click_logout(self):
        from pages.login_page import Login_Page
        self.driver.find_element(*self.logout_locator).click()
        return Login_Page(self.driver)

#tile for admin tile in home page : from admin_page.py
    def click_admin_tile(self):
        from pages.admin_page import Admin_page
        self.driver.find_element(*self.admin_tile_locator).click()
        return Admin_page(self.driver)

#tile for news tile in home page : from news_page.py
    def click_on_manage_news_tile(self):
        from pages.news_page import News_Page
        self.driver.find_element(*self.manage_news_tile_locator).click()
        return News_Page(self.driver)



