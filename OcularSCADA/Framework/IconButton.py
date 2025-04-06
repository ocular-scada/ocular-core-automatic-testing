
import time
from typing import Union, List, Optional, Tuple

from selenium.webdriver.common.by import By # type: ignore
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

from Components.BasicComponent import ComponentPiece
from Components.PerspectiveComponents.Common.Icon import CommonIcon
from Components.BasicComponent import BasicPerspectiveComponent


class IconButton(BasicPerspectiveComponent):

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



    def is_enabled(self):
        pass

    def get_icon_path(self):
        pass