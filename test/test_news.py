import time

import pytest

from pages.login_page import Login_Page
from pages.news_page import News_Page
from utilities.excelutility import ExcelUtility
from selenium.webdriver.common.by import By


class TestNews:
    def test_verify_opening_news_tile(self,browser_instance):
        self.driver=browser_instance
        self.driver.maximize_window()
        #loginto grocery app using valid user name and password
        excel_utility=ExcelUtility(r"C:\\TestData.xlsx")
        username=excel_utility.get_string_data(2,1,"LoginPage")
        password=excel_utility.get_string_data(2,2,"LoginPage")
        #locate username and password field and send username and password
        # self.driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys(username)
        # self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']").send_keys(password)
        # time.sleep(2)
        #login
        # self.driver.find_element(By.CSS_SELECTOR,".btn.btn-dark.btn-block").click()
        # time.sleep(2)
        #locate and click on manage news tile
        # manage_news_tile=self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news']")
        # manage_news_tile.click()
        # time.sleep(2)
        # home_link=self.driver.find_element(By.XPATH,"//a[text()='Home']")
        # home_link.click()
        login_page=Login_Page(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        news_page=News_Page(self.driver)
        news_page.click_on_manage_news_tile()
        time.sleep(2)
        news_page.click_on_home_link()
        time.sleep(3)

        #assertion
        #actual_url=self.driver.current_url
        #assert actual_url=="https://groceryapp.uniqassosiates.com/admin/home"
        #time.sleep(2)

    def test_verify_entering_news(self,browser_instance):
        self.driver=browser_instance
        self.driver.maximize_window()
        #loginto grocery app using valid user name and password
        excel_utility=ExcelUtility(r"C:\\TestData.xlsx")
        username=excel_utility.get_string_data(2,1,"LoginPage")
        password=excel_utility.get_string_data(2,2,"LoginPage")
        #locate username and password field and send username and password
        # self.driver.find_element(By.CSS_SELECTOR,"input.form-control").send_keys(username)
        # self.driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']").send_keys(password)
        # time.sleep(2)
        #login
        # self.driver.find_element(By.CSS_SELECTOR,".btn.btn-dark.btn-block").click()
        # time.sleep(2)
        #locate and click on manage news tile
        # manage_news_tile=self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news']")
        # manage_news_tile.click()
        # time.sleep(2)
        # new_option=self.driver.find_element(By.CSS_SELECTOR,".btn.btn-rounded.btn-danger")
        # new_option.click()
        # time.sleep(2)
        # enter_news=self.driver.find_element(By.XPATH,"//textarea[@id='news']")
        # enter_news.send_keys("India won T20 World Cup")
        # time.sleep(2)
        # save=self.driver.find_element(By.CSS_SELECTOR,"button[name='create']")
        # save.click()
        # time.sleep(2)
        login_page = Login_Page(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        time.sleep(2)
        news_page = News_Page(self.driver)
        news_page.click_on_manage_news_tile()
        time.sleep(2)
        news_page.click_on_news_option()
        time.sleep(2)
        news_page.enter_news()
        time.sleep(2)
        news_page.save_news()
        time.sleep(2)

        #assertion
        #actual_result=self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
        #assert actual_result.is_displayed()


    @pytest.mark.parametrize("news_info",["Market Hits Record High","Heavy Rain Disrupt City","Fuel Price Rises Again"])
    def test_verify_search_news(self,browser_instance,news_info):
        self.driver=browser_instance
        self.driver.maximize_window()
        # loginto grocery app using valid user name and password
        excel_utility = ExcelUtility(r"C:\\TestData.xlsx")
        username = excel_utility.get_string_data(2, 1, "LoginPage")
        password = excel_utility.get_string_data(2, 2, "LoginPage")
        # # locate username and password field and send username and password
        # self.driver.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(username)
        # self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(password)
        # time.sleep(2)
        # # login
        # self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-dark.btn-block").click()
        # time.sleep(2)
        # locate and click on manage news tile
        # manage_news_tile = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news']")
        # manage_news_tile.click()
        # time.sleep(2)
        # search_option=self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
        # search_option.click()
        # time.sleep(2)
        # news_search_field=self.driver.find_element(By.XPATH,"//input[@class='form-control']")
        # news_search_field.send_keys("India won T20 World Cup")
        # search_button=self.driver.find_element(By.CSS_SELECTOR,".btn.btn-danger.btn-fix")
        # search_button.click()
        login_page = Login_Page(self.driver)
        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.click_login()
        time.sleep(2)
        news_page = News_Page(self.driver)
        news_page.click_on_manage_news_tile()
        time.sleep(2)
        news_page.search_news_option()
        time.sleep(2)
        news_page.enter_news_for_search(news_info)
        time.sleep(2)
        news_page.search_news()
        time.sleep(2)

        #assertion
        #actual_result=self.driver.find_element(By.XPATH,"//table[@class='table table-bordered table-hover table-sm']/tbody/tr[1]/td[1]").text
        #expected_result=["Market Hits Record High","Heavy Rain Disrupt City","Fuel Price Rises Again"]
        #assert actual_result in expected_result
        #time.sleep(2)









