import time
from typing import Union, List, Optional, Tuple


from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.remote.webdriver import WebDriver

from Components.BasicComponent import BasicPerspectiveComponent

class SideBarMenu(BasicPerspectiveComponent):

    _RESPONCE_TIME = 0.8

    def __init__(
            self,
            locator: Tuple[By, str],
            driver: WebDriver,
            parent_locator_list: Optional[List[Tuple[By, str]]] = None,
            wait_timeout: float = 2,
            description: Optional[str] = None,
            poll_freq: float = 0.5):
        super().__init__(
            locator=locator,
            driver=driver,
            parent_locator_list=parent_locator_list,
            wait_timeout=wait_timeout,
            description=description,
            poll_freq=poll_freq)

    def select_menu_item_by_target(self, target):
        menu_item = self.driver.find_element(By.ID, "menu-item__" + target)
        menu_item.click()
        time.sleep(self._RESPONCE_TIME)
