from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Admin_page:
    def __init__(self,browser):
        self.driver=browser
        self.admin_tile_locator=(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer'] ")
        self.new_option_locator=(By.XPATH,"//a[@class='btn btn-rounded btn-danger']")
        self.user_name_in_new_option_locator=(By.CSS_SELECTOR, "input[name='username']")
        self.password_in_new_option_locator=(By.CSS_SELECTOR, "input[name='password']")
        self.drop_down_in_new_option_locator=(By.CSS_SELECTOR, "select[name='user_type']")
        self.select_dropdown_value_in_new_option_locator=(By.XPATH, "//button[@name='Create']")
        self.search_button_in_new_option_locator=(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        self.username_in_search_option_locator=(By.CSS_SELECTOR, "input.form-control")
        self.user_type_drop_down_in_search_option_locator=(By.CSS_SELECTOR, "select[name='ut']")
        self.search_button_in_search_option_locator=(By.XPATH, "//button[@type='submit']")


    def click_admin_tile(self):
        self.driver.find_element(*self.admin_tile_locator).click()
    def click_new_option(self):
        self.driver.find_element(*self.new_option_locator).click()
    def enter_admin_users_information(self):
        self.driver.find_element(*self.user_name_in_new_option_locator).send_keys("User_name1")
        self.driver.find_element(*self.password_in_new_option_locator).send_keys("password1")
        user_type_dropdown=self.driver.find_element(*self.drop_down_in_new_option_locator)
        select = Select(user_type_dropdown)
        select.select_by_value("staff")
        self.driver.find_element(*self.select_dropdown_value_in_new_option_locator).click()
    def click_search_option(self):
        self.driver.find_element(*self.search_button_in_new_option_locator).click()
    def search_user_information(self):
        self.driver.find_element(*self.username_in_search_option_locator).send_keys("User_name1")
        user_type_dropdown = self.driver.find_element(*self.user_type_drop_down_in_search_option_locator)
        select = Select(user_type_dropdown)
        select.select_by_value("staff")
        self.driver.find_element(*self.search_button_in_search_option_locator).click()









