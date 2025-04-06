
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time


from Pages.PerspectivePageObject import PerspectivePageObject
from OcularSCADA.Framework.SideBarMenu import SideBarMenu
from OcularSCADA.Framework.TabMenuHorizontal import TabMenuHorizontal

class OcularPage(PerspectivePageObject):


    def __init__(self, driver, gateway_address, page_config_path):
        super().__init__(driver=driver, gateway_address=gateway_address, page_config_path=page_config_path)

        self.side_bar_menu = SideBarMenu(locator=(By.ID, "ocular-scada__side-bar-menu"), driver=self.driver)


    def open_menu_item(self, target):
        self.side_bar_menu.select_menu_item_by_target(target)

    def select_tab_by_label(self, label):
        tabMenuHorizontal = TabMenuHorizontal(locator=(By.CLASS_NAME, "psc-os-tabMenuHorizontal"), driver=self.driver)
        tabMenuHorizontal.select_tab_by_label(label)