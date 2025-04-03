
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time


from OcularSCADA.Framework.OcularPage import OcularPage


ADD_ICON_ID = "ocular-scada__asset-tree__add-icon"
EDIT_ICON_ID = "ocular-scada__asset-tree__edit-icon"
UP_ICON_ID = "ocular-scada__asset-tree__up-icon"
DOWN_ICON_ID = "ocular-scada__asset-tree__down-icon"
MOVE_ICON_ID = "ocular-scada__asset-tree__move-icon"
DELETE_ICON_ID = "ocular-scada__asset-tree__delete-icon"
ADVANCED_ICON_ID = "ocular-scada__asset-tree__advanced-icon"




class ModelEditorPage(OcularPage):

    def __init__(self, driver, gateway_address, page_config_path):
        super().__init__(driver=driver, gateway_address=gateway_address, page_config_path=page_config_path)



    def clickAssetControlIcon(self, icon):

        control_icon = None
        id = ""
        if icon == 'add':
            id = ADD_ICON_ID
        elif icon == 'edit':
            id = EDIT_ICON_ID
        elif icon == 'up':
            id = UP_ICON_ID
        elif icon == 'down':
            id = DOWN_ICON_ID
        elif icon == 'move':
            id = MOVE_ICON_ID
        elif icon == 'delete':
            id = DELETE_ICON_ID
        elif icon == 'advanced':
            id = ADVANCED_ICON_ID

        control_icon = self.driver.find_element(By.ID, id)
        
        if control_icon:
            control_icon.click()
            time.sleep(2)



    def isSlideOutOpen(self):
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, ".psc-os-page__rightSlideout.psc-os-isOpened")
            return True
        except:
            return False



    # isTreeItemExpanded(path) recursive on path

    # clickTreeItem(path)  recursive on path


    def clickModelEditorTab(self):
        super().select_tab_by_label("Model Editor")

    def clickTypeEditorTab(self):
        super().select_tab_by_label("Type Editor")

