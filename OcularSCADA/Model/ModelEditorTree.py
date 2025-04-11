import time
from typing import Union, List, Optional, Tuple

from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.remote.webdriver import WebDriver

from Components.BasicComponent import BasicPerspectiveComponent
from OcularSCADA.Framework.ProgressiveTree import ProgressiveTree
from OcularSCADA.Framework.IconButton import IconButton


class ModelEditorTree(BasicPerspectiveComponent):

    _RESPONCE_TIME = 0.4


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


        self.tree = ProgressiveTree(locator=(By.ID, "ocular-scada__asset-tree"), driver=self.driver, parent_locator_list=self.locator_list, poll_freq=poll_freq)
        self.add_icon = IconButton(locator=(By.ID, "add-icon"), driver=self.driver, parent_locator_list=self.locator_list)
        self.edit_icon = IconButton(locator=(By.ID, "edit-icon"), driver=self.driver, parent_locator_list=self.locator_list)
        self.up_icon = IconButton(locator=(By.ID, "up-icon"), driver=self.driver, parent_locator_list=self.locator_list)
        self.down_icon = IconButton(locator=(By.ID, "down-icon"), driver=self.driver, parent_locator_list=self.locator_list)
        self.move_icon = IconButton(locator=(By.ID, "move-icon"), driver=self.driver, parent_locator_list=self.locator_list)
        self.delete_icon = IconButton(locator=(By.ID, "delete-icon"), driver=self.driver, parent_locator_list=self.locator_list)
        self.advanced_icon = IconButton(locator=(By.ID, "advanced-icon"), driver=self.driver, parent_locator_list=self.locator_list)




    def expand_tree_item(item_id):
        # get item_path from api

        pass

    def select_tree_item(item_id):
        # get item_path from api

        pass


    def select_advanced_function():
        pass


    def _is_advanced_menu_opened():
        pass

