
import time

from selenium.webdriver.common.by import By



class TabMenuHorizontal:

    def __init__(self, driver):
        self.driver = driver



    def select_tab_by_label(self, label):
        tab_item = self.driver.find_element(By.ID, "ocular-scada__tab-menu-horizontal__tab-item__" + label)
        tab_item.click()
        time.sleep(1)


