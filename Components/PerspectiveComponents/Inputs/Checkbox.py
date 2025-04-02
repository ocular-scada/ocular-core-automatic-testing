from typing import List, Optional, Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Components.BasicComponent import BasicPerspectiveComponent
from Components.PerspectiveComponents.Common.Checkbox import CommonCheckbox


class Checkbox(CommonCheckbox, BasicPerspectiveComponent):
    """A Perspective Checkbox Component."""

    def __init__(
            self,
            locator: Tuple[By, str],
            driver: WebDriver,
            parent_locator_list: Optional[List[Tuple[By, str]]] = None,
            wait_timeout: float = 3,
            description: Optional[str] = None,
            poll_freq: float = 0.5):
        CommonCheckbox.__init__(
            self, locator=locator,
            driver=driver,
            parent_locator_list=parent_locator_list,
            wait_timeout=wait_timeout,
            description=description,
            poll_freq=poll_freq)
        BasicPerspectiveComponent.__init__(
            self, locator=locator,
            driver=driver,
            parent_locator_list=parent_locator_list,
            wait_timeout=wait_timeout,
            description=description,
            poll_freq=poll_freq)
