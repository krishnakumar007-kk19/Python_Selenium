from selenium.webdriver.common.by import By


class Home_page:
    def __init__(self,browser):
        self.driver=browser
        self.admin_tile_locator=By.XPATH, "//a[@data-toggle='dropdown']"
        self.logout_locator=By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/logout']"

    def click_admin(self):
        # locate Admin
        self.driver.find_element(*self.admin_tile_locator).click()
    def click_logout(self):
        self.driver.find_element(*self.logout_locator).click()
