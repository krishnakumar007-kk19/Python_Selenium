import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import constance.constant
from pages.admin_page import Admin_page
from pages.login_page import Login_Page
from utilities.excelutility import ExcelUtility
from pages.home_page import Home_page

class TestAdmin:
    def test_verify_admin_users(self,browser_instance):
        self.driver=browser_instance
        self.driver.maximize_window()
        time.sleep(2)
        # loginto grocery app using valid user name and password
        #excel_utility = ExcelUtility("C:\\TestData.xlsx")
        excel_utility = ExcelUtility(constance.constant.file_path) #accessing constant.py
        username=excel_utility.get_string_data(2, 1, "LoginPage")
        password=excel_utility.get_string_data(2, 2, "LoginPage")
        # locate username and password field and send username and password
        # self.driver.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(username)
        # self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
        # time.sleep(2)
        # login
        # self.driver.find_element(By.CSS_SELECTOR,".btn.btn-dark.btn-block").click()
        # time.sleep(5)
        #locate admin tile
        # admin_tile=self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer'] ")
        # admin_tile.click()
        # time.sleep(2)
        #click on new
        # new_option=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-danger']")
        # new_option.click()
        # time.sleep(2)
        #enter username and password
        # username_field=self.driver.find_element(By.CSS_SELECTOR,"input[name='username']")
        # username_field.send_keys("aleena25")
        # password_field=self.driver.find_element(By.CSS_SELECTOR,"input[name='password']")
        # password_field.send_keys("aleena19847")
        # time.sleep(2)
        # user_type_dropdown=self.driver.find_element(By.CSS_SELECTOR,"select[name='user_type']")
        # select=Select(user_type_dropdown)
        # select.select_by_value("staff")
        # time.sleep(8)
        # save_button=self.driver.find_element(By.XPATH,"//button[@name='Create']")
        # save_button.click()
        # time.sleep(2)
        login_page = Login_Page(self.driver)
        login_page.enter_username(username).enter_password(password).click_login()
        #login_page.enter_password(password)
        #login_page.click_login()
        #time.sleep(2)
        admin_page = Admin_page(self.driver)
        admin_page.click_admin_tile().click_new_option().enter_admin_users_information()
        #time.sleep(2)
        #admin_page.click_new_option()
        #time.sleep(2)
        #admin_page.enter_admin_users_information()
        #time.sleep(2)

        #assertion
        actual_result=self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']").text
        assert "Username already exists." in actual_result
        #actual_result2=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
        #assert "User Created Successfully" in actual_result2


    def test_verify_search_username(self,browser_instance):
        self.driver=browser_instance
        self.driver.maximize_window()
        time.sleep(2)
        # loginto grocery app using valid user name and password
        #excel_utility = ExcelUtility("C:\\TestData.xlsx")
        excel_utility = ExcelUtility(constance.constant.file_path) #accessing constant.py
        username = excel_utility.get_string_data(2, 1, "LoginPage")
        password = excel_utility.get_string_data(2, 2, "LoginPage")
        # locate username and password field and send username and password
        # self.driver.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(username)
        # self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
        # time.sleep(2)
        # login
        # locate admin tile
        # admin_tile = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer'] ")
        # admin_tile.click()
        # time.sleep(2)
        # search_button=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
        # search_button.click()
        # time.sleep(2)
        # username_filed=self.driver.find_element(By.CSS_SELECTOR,"input.form-control")
        # username_filed.send_keys("username1")
        # user_type_dropdown = self.driver.find_element(By.CSS_SELECTOR, "select[name='ut']")
        # select = Select(user_type_dropdown)
        # select.select_by_value("staff")
        # time.sleep(8)
        # search_button=self.driver.find_element(By.XPATH,"//button[@type='submit']")
        # search_button.click()
        # time.sleep(10)
        login_page = Login_Page(self.driver)
        login_page.enter_username(username).enter_password(password).click_login()
        #login_page.enter_password(password)
        #login_page.click_login()
        #time.sleep(2)
        admin_page = Admin_page(self.driver)
        admin_page.click_admin_tile().click_search_option().search_user_information()
        #admin_page.click_search_option()
        #admin_page.search_user_information()
        #time.sleep(2)

        #assertion
        #expected_result=["aleena","staff","Active"]
        #for i in range(len(expected_result)):
        #    actual_result=self.driver.find_element(By.XPATH,f"//table[@class='table table-bordered table-hover table-sm']/tbody/tr[1]/td[{i+1}]").text
        #    assert expected_result[i] == actual_result

        # username_result=self.driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover table-sm']/tbody/tr[1]/td[1]").text
        # usertype_result=self.driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover table-sm']/tbody/tr[1]/td[2]").text
        # status_result=self.driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover table-sm']/tbody/tr[1]/td[3]").text
        #
        # assert username_result == "username"
        # assert usertype_result == "staff"
        # assert status_result == "Active"



