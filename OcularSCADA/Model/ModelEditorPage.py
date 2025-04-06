
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time


from OcularSCADA.Framework.OcularPage import OcularPage
from OcularSCADA.Model.ModelEditorTree import ModelEditorTree
from OcularSCADA.Model.ModelEditorSlideout import ModelEditorSlideout


ADD_ICON_ID = "ocular-scada__asset-tree__add-icon"
EDIT_ICON_ID = "ocular-scada__asset-tree__edit-icon"
UP_ICON_ID = "ocular-scada__asset-tree__up-icon"
DOWN_ICON_ID = "ocular-scada__asset-tree__down-icon"
MOVE_ICON_ID = "ocular-scada__asset-tree__move-icon"
DELETE_ICON_ID = "ocular-scada__asset-tree__delete-icon"
ADVANCED_ICON_ID = "ocular-scada__asset-tree__advanced-icon"


MODEL_EDITOR_TREE_ID = "ocular-scada__model-editor-tree"
MODEL_EDITOR_SLIDEOUT_ID = "ocular-scada__model-editor-slideout"

_RESPONCE_TIME = 0.6


class ModelEditorPage(OcularPage):

    def __init__(self, driver, gateway_address, page_config_path):
        super().__init__(driver=driver, gateway_address=gateway_address, page_config_path=page_config_path)

        self.tree_editor = ModelEditorTree(locator=(By.ID, MODEL_EDITOR_TREE_ID), driver=self.driver)
        self.slideout_editor = ModelEditorSlideout(locator=(By.ID, MODEL_EDITOR_SLIDEOUT_ID), driver=self.driver)



    def clickModelEditorTab(self):
        super().select_tab_by_label("Model Editor")

    def clickTypeEditorTab(self):
        super().select_tab_by_label("Type Editor")




    def add_asset(self, parent_item_path, details):

        assert(self.tree_editor.tree.item_path_exists_in_tree(parent_item_path))

        if parent_item_path:
            print(f"Selecting parent_item_path {parent_item_path}")
            time.sleep(.5)
            self.tree_editor.tree.select_item_by_path(parent_item_path)
            time.sleep(.5)
        
        self.tree_editor.add_icon.click()

        time.sleep(.5)

        assert(self.slideout_editor.is_open())

        for key in details.keys():

            self.slideout_editor.form.set_value(key=key, value=details[key])

        time.sleep(.5)

        self.slideout_editor.click_save()
