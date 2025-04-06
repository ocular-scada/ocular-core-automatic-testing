import time
from typing import Union, List, Optional, Tuple

from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.remote.webdriver import WebDriver

from Components.BasicComponent import BasicPerspectiveComponent
from OcularSCADA.Framework.FormItem import FormItem

class FormValueBased(BasicPerspectiveComponent):

    _COMPONENT_ITEM_ID_PREFIX = 'form-item__'



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


    def set_value(self, key, value):

        form_item = FormItem(locator=(By.ID, self._COMPONENT_ITEM_ID_PREFIX + key.replace('.', '-')), driver=self.driver, parent_locator_list=self.locator_list)
        form_item.set_value(value)
        


    def get_value(self, key, form_type):
        pass