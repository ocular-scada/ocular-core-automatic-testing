
import time
from typing import Union, List, Optional, Tuple

from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.remote.webdriver import WebDriver

from Components.BasicComponent import BasicPerspectiveComponent


class TabMenuHorizontal(BasicPerspectiveComponent):

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

    def select_tab_by_label(self, label):
        tab_item = self.driver.find_element(By.ID, "tab-item__" + label)
        tab_item.click()
        time.sleep(1)


