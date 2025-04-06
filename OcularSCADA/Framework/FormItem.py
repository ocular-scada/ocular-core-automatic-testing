
import time
from typing import Union, List, Optional, Tuple

from selenium.webdriver.common.by import By # type: ignore
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver


from Components.BasicComponent import BasicPerspectiveComponent
from Components.PerspectiveComponents.Inputs.TextField import TextField
from Components.PerspectiveComponents.Inputs.TextArea import TextArea
from Components.PerspectiveComponents.Inputs.Dropdown import Dropdown
from Components.PerspectiveComponents.Inputs.Checkbox import Checkbox


class FormItem(BasicPerspectiveComponent):

    _RESPONCE_TIME = 0.6
    _CSS_CLASS_NAME = "psc-os-controlIcon"

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



    def get_type(self):
        return self.find().get_attribute(name="data-component")


    def set_value(self, value):
        data_component = self.get_type()

        if data_component == 'ia.input.text-field':
            form_item = TextField(locator=self._locator, driver=self.driver)
            form_item.set_text(value)
        elif data_component == 'ia.input.text-area':
            form_item = TextArea(locator=self._locator, driver=self.driver)
            form_item.set_text(value)
        elif data_component == 'ia.input.dropdown':
            form_item = Dropdown(locator=self._locator, driver=self.driver)
            form_item.select_option_by_text_if_not_selected(value)
        elif data_component == 'ia.input.checkbox':
            form_item = Checkbox(locator=self.locator, driver=self.driver)
            form_item.set_state(value)
