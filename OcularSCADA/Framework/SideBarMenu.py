
import time

from selenium.webdriver.common.by import By



class SideBarMenu:

    def __init__(self, driver):
        self.driver = driver



    def select_menu_item_by_target(self, target):
        menu_item = self.driver.find_element(By.ID, "ocular-scada__side-bar-menu__menu-item__" + target)
        menu_item.click()
        time.sleep(2)
