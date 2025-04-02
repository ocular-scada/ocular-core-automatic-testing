
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


from Pages.PerspectivePageObject import PerspectivePageObject
from OcularSCADA.Framework.SideBarMenu import SideBarMenu


class OcularPageObject(PerspectivePageObject):


    def __init__(self, driver, gateway_address, page_config_path):
        super().__init__(driver=driver, gateway_address=gateway_address, page_config_path=page_config_path)


    def open_menu_item(self, target):
        sideBarMenu = SideBarMenu(self.driver)
        sideBarMenu.select_menu_item_by_target(target)