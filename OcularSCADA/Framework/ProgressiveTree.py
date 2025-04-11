
import time
from typing import Union, List, Optional, Tuple

from selenium.webdriver.common.by import By # type: ignore
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

from Components.BasicComponent import ComponentPiece
from Components.PerspectiveComponents.Common.Icon import CommonIcon
from Components.PerspectiveComponents.Displays.Tree import Tree


class ProgressiveTree(Tree):

    _RESPONCE_TIME = 0.4

    def __init__(self, locator, driver):
        Tree.__init__(self, locator=locator, driver=driver)



    def __init__(
            self,
            locator: Tuple[By, str],
            driver: WebDriver,
            parent_locator_list: Optional[List[Tuple[By, str]]] = None,
            wait_timeout: float = 3,
            description: Optional[str] = None,
            poll_freq: float = 0.5):
        super().__init__(
            locator=locator,
            driver=driver,
            parent_locator_list=parent_locator_list,
            wait_timeout=wait_timeout,
            description=description,
            poll_freq=poll_freq)


        self._expand_collapse_icons_by_path = {}





    def get_item_label_by_path(self, item_path):

        item_list = []

        if len(item_list) > 1:
            item_list = list(map(int, item_path.split('/')))
            self._expand_item_by_path("", item_list[:-1])
        

        tree_item = self._get_item_by_path(item_path)
        tree_item_label = tree_item.find().get_attribute(name="data-label")
        return tree_item_label



    def select_item_by_path(self, item_path):

        item_list = list(map(int, item_path.split('/')))

        if len(item_list) > 1:
            self._expand_item_by_path("", item_list[:-1])

        tree_item = self._get_item_by_path(item_path)

        label = ComponentPiece(
                locator=self._LABEL_LOCATOR,
                driver=self.driver,
                parent_locator_list=tree_item.locator_list,
                poll_freq=self.poll_freq)

        label.click()
        time.sleep(self._RESPONCE_TIME)




    def expand_item_by_path(self, item_path):

        if item_path:
            item_list = list(map(int, item_path.split('/')))
            self._expand_item_by_path("", item_list)



    def item_is_expanded_by_path(self, item_path: str) -> bool:

        try:
            return self._EXPANDED_ICON_CLASS in self._get_expansion_icon_by_path(
                item_path=item_path).find().get_attribute(name="class")
        except TimeoutException:
            return False



    def is_child(self, parent_item_path, name):
        children = self._get_children(parent_item_path)

        for child in children:
            if child.get_attribute("data-label") == name:
                return True
        
        return False
    
    def child_order(self, parent_item_path, name):
        children = self._get_children(parent_item_path)

        children_names = [child.get_attribute("data-label") for child in children]

        index = -1
        try:
            index = children_names.index(name)
        except:
            index = -1

        return index





    def paths_match(self, item_path, name_path):

        item_list = list(map(int, item_path.split('/')))
        name_list = name_path.split('/')

        if len(item_list) != len(name_list):
            return False
        else:
            return self._paths_match("", item_list, name_list)




    # overridding this becuase it was buggy in the base class
    def item_exists_in_tree(self, item_path: str, item_label: str, wait_timeout: int = 2) -> bool:

        try:
            return self._get_item_by_path(
                path=item_path, wait_timeout=wait_timeout).find().get_attribute(name="data-label") == item_label
        except TimeoutException:
            return False
    

    def item_path_exists_in_tree(self, item_path):

        try:
            if self._get_item_by_path(path=item_path):
                return True
            else:
                return False
        except TimeoutException:
            return False




    def path_exists_in_tree(self, item_path: str, wait_timeout: int = 2):
        try:
            return self._get_item_by_path(path=item_path, wait_timeout=wait_timeout).find()
        except TimeoutException:
            return False



    def _get_children(self, parent_item_path):
        
        self.expand_item_by_path(parent_item_path)
        items = []
        try:
            if parent_item_path:
                items = ComponentPiece(
                    locator=(By.CSS_SELECTOR, f'div[data-item-path="{parent_item_path}"] > div[data-item-path]'),
                    driver=self.driver,
                    parent_locator_list=None,
                    wait_timeout=1,
                    poll_freq=self.poll_freq).find_all()
            else:
                # root items
                items = ComponentPiece(
                    locator=(By.CSS_SELECTOR, f'.tree > .node-wrapper > div[data-item-path]'),
                    driver=self.driver,
                    parent_locator_list=None,
                    wait_timeout=1,
                    poll_freq=self.poll_freq).find_all()
        except TimeoutException:
            items = []

        return items



    def _get_expansion_icon_by_path(self, item_path: str) -> CommonIcon:
        """Obtain the icon which conveys the expansion status of the item."""
        icon = self._expand_collapse_icons_by_path.get(item_path)
        if not icon:
            icon = CommonIcon(
                locator=(By.CSS_SELECTOR, "svg.expand-icon"),
                driver=self.driver,
                parent_locator_list=self._get_item_by_path(path=item_path).locator_list,
                poll_freq=self.poll_freq)
            self._expand_collapse_icons_by_path[item_path] = icon
        return icon



    def _expand_item_by_path(self, item_path, item_list):

        if item_path:
            item_path = item_path + "/" + str(item_list[0])
        else:
            item_path = str(item_list[0])

        if self.item_path_exists_in_tree(item_path):

            if not self.item_is_expanded_by_path(item_path):

                tree_item = self._get_item_by_path(item_path)

                label = ComponentPiece(
                        locator=self._LABEL_LOCATOR,
                        driver=self.driver,
                        parent_locator_list=tree_item.locator_list,
                        poll_freq=self.poll_freq)

                label.click()

                time.sleep(self._RESPONCE_TIME)

            if len(item_list) > 1:
                self._expand_item_by_path(item_path, item_list[1:])


        else:
            print(f"Item path {item_path} does not exist in tree")





    




    def _paths_match(self, item_path, item_list, name_list):

        if item_path:
            item_path = item_path + "/" + str(item_list[0])
        else:
            item_path = str(item_list[0])
        
        if self.item_exists_in_tree(item_path, name_list[0]):

            if not self.item_is_expanded_by_path(item_path):
                item = self._get_item_by_path(item_path)
                item.click()
                time.sleep(self._RESPONCE_TIME)

            if len(item_list) > 1 and len(name_list) > 1:
                return self._paths_match(item_path, item_list[1:], name_list[1:])
            else:
                return True

        else:
            print(f'Item {name_list[0]} at path {item_path} does not exist in tree.')
            return False