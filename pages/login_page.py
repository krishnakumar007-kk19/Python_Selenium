from selenium.webdriver.common.by import By


class Login_Page:
    def __init__(self,driver):
        self.driver=driver
        self.username_locator=(By.XPATH, "//input[@name='username']")
        self.password_locator=(By.XPATH, "//input[@name='password']")
        self.login_button_locator=(By.XPATH, "//button[@type='submit']")
    def enter_username(self,username_value):
        #page factory
        self.driver.find_element(*self.username_locator).send_keys(username_value)
    def enter_password(self,password_value):
        self.driver.find_element(*self.password_locator).send_keys(password_value)
    def click_login(self):
        self.driver.find_element(*self.login_button_locator).click()



