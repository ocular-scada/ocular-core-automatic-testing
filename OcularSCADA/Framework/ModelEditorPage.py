
from selenium import webdriver
from selenium.webdriver.common.by import By


from OcularSCADA.Framework.OcularPageObject import OcularPageObject

class ModelEditorPage(OcularPageObject):

    def __init__(self, driver, gateway_address, page_config_path):
        super().__init__(driver=driver, gateway_address=gateway_address, page_config_path=page_config_path)


    # clickAddIcon()

    # clickEditIcon()

    # isTreeItemExpanded(path) recursive on path

    # clickTreeItem(path)  recursive on path


    # clickModelEditorTab()

    # clickTypeEditorTab()