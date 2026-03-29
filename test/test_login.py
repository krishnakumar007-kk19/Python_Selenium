import time
import pytest
import constance.constant
from pages.home_page import Home_page
from pages.login_page import Login_Page
from utilities.excelutility import ExcelUtility
from selenium.webdriver.common.by import By

class TestLogin:
    @pytest.mark.order(1)
    def test_verify_validlogin(self,browser_instance):
        from pages.home_page import Home_page
        from pages.login_page import Login_Page
        self.driver=browser_instance
        #excel_utility = ExcelUtility("C:\\TestData.xlsx")
        excel_utility = ExcelUtility(constance.constant.file_path) #accessing constant.py
        # test_case-1(valid username -valid password)
        username_value=excel_utility.get_string_data(2,1,"LoginPage")
        password_value=excel_utility.get_string_data(2,2,"LoginPage")
        #self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        # username=self.driver.find_element(By.XPATH,"//input[@name='username']")
        # username.send_keys(username_value)
        # password=self.driver.find_element(By.XPATH,"//input[@name='password']")
        # password.send_keys(password_value)
        # button=self.driver.find_element(By.XPATH,"//button[text()='Sign In']")
        # button.click()
        login_page=Login_Page(self.driver)
        login_page.enter_username(username_value).enter_password(password_value)
        #login_page.enter_password(password_value)
        homepage = Home_page(self.driver)
        homepage = login_page.click_login()

        #assertion
        #actual_url=self.driver.current_url
        #assert actual_url=="https://groceryapp.uniqassosiates.com/admin"
        time.sleep(2)

    @pytest.mark.order(2)
    def test_verify_invalid_username(self,browser_instance):
        self.driver = browser_instance
        #excel_utility = ExcelUtility("C:\\TestData.xlsx")
        excel_utility = ExcelUtility(constance.constant.file_path) #accessing constant.py
        # test_case-2(Invalid username-valid password)
        username_value = excel_utility.get_string_data(4, 1, "LoginPage")
        password_value = excel_utility.get_string_data(4, 2, "LoginPage")
        #self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        # username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username.send_keys(username_value)
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password.send_keys(password_value)
        # button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        # button.click()
        login_page = Login_Page(self.driver)
        login_page.enter_username(username_value).enter_password(password_value).click_login()
        #login_page.enter_password(password_value)
        #login_page.click_login()

        #assertion
        #actual_url = self.driver.current_url
        #assert actual_url == "https://groceryapp.uniqassosiates.com/admin/login"
        time.sleep(2)

    @pytest.mark.order(3)
    def test_verify_invalid_password(self,browser_instance):
        self.driver = browser_instance
        #excel_utility = ExcelUtility("C:\\TestData.xlsx")
        excel_utility = ExcelUtility(constance.constant.file_path) #accessing constant.py
        # test_case-3(valid username-invalid password)
        username_value = excel_utility.get_string_data(3, 1, "LoginPage")
        password_value = excel_utility.get_string_data(3, 2, "LoginPage")
        # #self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        # username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username.send_keys(username_value)
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password.send_keys(password_value)
        # button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        # button.click()
        login_page = Login_Page(self.driver)
        login_page.enter_username(username_value).enter_password(password_value).click_login()
        #login_page.enter_password(password_value)
        #login_page.click_login()

        #assertion
        #actual_url = self.driver.current_url
        #assert actual_url == "https://groceryapp.uniqassosiates.com/admin/login"
        time.sleep(2)

    @pytest.mark.order(4)
    def test_verify_invalid_login(self,browser_instance):
        # test_case-4(invalid username-invalid password)

        self.driver = browser_instance
        #excel_utility = ExcelUtility("C:\\TestData.xlsx")
        excel_utility = ExcelUtility(constance.constant.file_path) #accessing constant.py
        # test_case-4(Invalid username-invalid password)
        username_value = excel_utility.get_string_data(5, 1, "LoginPage")
        password_value = excel_utility.get_string_data(5, 2, "LoginPage")
        #self.driver.get("https://groceryapp.uniqassosiates.com/admin/login")
        # username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username.send_keys(username_value)
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password.send_keys(password_value)
        # button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        # button.click()
        login_page = Login_Page(self.driver)
        login_page.enter_username(username_value).enter_password(password_value).click_login()
        #login_page.enter_password(password_value)
        #login_page.click_login()

        #assertion
        #actual_url = self.driver.current_url
        #assert actual_url == "https://groceryapp.uniqassosiates.com/admin/login"
        time.sleep(2)





