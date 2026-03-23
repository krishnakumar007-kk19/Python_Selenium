import time

from selenium.webdriver.common.by import By

from pages.home_page import Home_page
from pages.login_page import Login_Page
from utilities.excelutility import ExcelUtility


class TestHome():
    def test_verify_logout(self,browser_instance):
        self.driver = browser_instance

        self.driver.maximize_window()
        excel_utility = ExcelUtility("C:\\TestData.xlsx")
        # (login with valid username-valid password)
        username_value = excel_utility.get_string_data(2, 1, "LoginPage")
        password_value = excel_utility.get_string_data(2, 2, "LoginPage")
        # self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        # username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username.send_keys(username_value)
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password.send_keys(password_value)
        # button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        # button.click()
        # time.sleep(2)
        #locate Admin
        # admin=self.driver.find_element(By.XPATH,"//a[@data-toggle='dropdown']")
        # admin.click()
        #time.sleep(2)
        #locate logout
        # logout=self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/logout']")
        # logout.click()
        # time.sleep(2)
        login_page = Login_Page(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.click_login()
        home_page=Home_page(self.driver)
        home_page.click_admin()
        home_page.click_logout()


        #assertion
        actual_result=self.driver.current_url
        expected_result="https://groceryapp.uniqassosiates.com/admin/login"
        assert expected_result==actual_result








