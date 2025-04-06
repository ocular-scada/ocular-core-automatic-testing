import time
from typing import Union, List, Optional, Tuple

from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.remote.webdriver import WebDriver

from Components.BasicComponent import BasicPerspectiveComponent
from Components.PerspectiveComponents.Inputs.Button import Button
from OcularSCADA.Framework.FormValueBased import FormValueBased


class ModelEditorSlideout(BasicPerspectiveComponent):



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


        self.form = FormValueBased(locator=(By.CLASS_NAME, 'psc-os-formContainer'), driver=self.driver, parent_locator_list=self.locator_list)


    def is_open(self):

        try:
            element = self.driver.find_element(By.CSS_SELECTOR, ".psc-os-page__rightSlideout.psc-os-isOpened")
            return True
        except:
            return False
    


    def click_save(self):
        button = Button(locator=(By.ID, "model-slideout__save"), driver=self.driver, parent_locator_list=self.locator_list)
        button.click()


    def click_cancel(self):
        button = Button(locator=(By.ID, "model-slideout__cancel"), driver=self.driver, parent_locator_list=self.locator_list)
        button.click()