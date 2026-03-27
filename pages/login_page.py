from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait

#from pages.home_page import Home_page
from utilities.wait_utility import Wait_utility

class Login_Page:
    def __init__(self,driver):
        self.driver=driver
        self.wait_utility = Wait_utility()
        self.username_locator=(By.XPATH, "//input[@name='username']")
        self.password_locator=(By.XPATH, "//input[@name='password']")
        self.login_button_locator=(By.XPATH, "//button[@type='submit']")
    def enter_username(self,username_value):
        #page factory
        self.driver.find_element(*self.username_locator).send_keys(username_value)
        return self
    def enter_password(self,password_value):
        self.driver.find_element(*self.password_locator).send_keys(password_value)
        return self

    def click_login(self):
        from pages.home_page import Home_page
        self.wait_utility.wait_until_clickable(self.driver,self.login_button_locator)
        self.driver.find_element(*self.login_button_locator).click()
        return Home_page(self.driver)


