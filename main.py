from selenium.webdriver.common.by import By # type: ignore
import unittest
import time

import OcularSCADA.API
import Tests.util
import Tests.AssetTests

from OcularSCADA.Model.ModelEditorPage import ModelEditorPage
from OcularSCADA.Framework.OcularPage import OcularPage
from OcularSCADA.Framework.ProgressiveTree import ProgressiveTree



print(OcularSCADA.API.rpc("ocular.asset.Asset.getIndexPath", [6]))
print(OcularSCADA.API.rpc("ocular.asset.Asset.getNamePath", [6]))

# run asset unit tests
#OcularSCADA.API.unit_tests('asset')


# run asset ui component tests
# loader = unittest.TestLoader()
# asset_suite = loader.loadTestsFromModule(Tests.AssetTests)

# with open("/home/nate/Documents/test_results_UI", "w") as stream:
#     unittest.TextTestRunner(stream=stream, verbosity=2).run(asset_suite)


# driver = Tests.util.open_browser()
# page_inst = OcularPage(driver, '', '')
# page_inst.open_menu_item("model")


# page_inst = ModelEditorPage(driver, '', '')
# slideOutOpen = page_inst.isSlideOutOpen()
# print("Model page opened. Is slideout opened? " + str(slideOutOpen))


# page_inst.clickAssetControlIcon("add")
# time.sleep(1)
# slideOutOpen = page_inst.isSlideOutOpen()
# print("Add icon clicked. Is slideout opened? " + str(slideOutOpen))


# page_inst.clickAssetControlIcon("advanced")

# page_inst.clickTypeEditorTab()
# page_inst.clickModelEditorTab()

#tree = ProgressiveTree(driver=driver, locator=(By.ID, "ocular-scada__asset-tree"))


#tree.expand_item_by_path(item_path="0/0/1")
#tree.select_item_by_path(item_path="0/0/1/0")
# print(tree.paths_match(item_path="0/0/1/0", name_path="SIM City/Wells/Well 2/Well Pump"))
# print(tree.paths_match(item_path="0/0", name_path="SIM City/Wells"))
# print(tree.paths_match(item_path="0/0/1/0", name_path="SIM City/Wells/Well 1/Well Pump"))



#tree.find().screenshot("/home/nate/Pictures/Screenshots/asset-tree.png")


# print("all items: ")
# print(tree.get_text_of_all_items_in_tree())
# print("SIM City exists:")
# print(tree.item_exists_in_tree("0", "SIM City"))
# print("Treatment exists:")
# print(tree.item_exists_in_tree("0/1", "Treatment"))
# print("SIM City expanded:")
# print(tree.item_is_expanded("SIM City"))
# tree.click_item_label("SIM City")
# time.sleep(1)
# print("SIM City expanded after click")
# print(tree.item_is_expanded("SIM City"))
# print("all items after SIM City click: ")
# print(tree.get_text_of_all_items_in_tree())
# print("SIM City exists:")
# print(tree.item_exists_in_tree("0", "SIM City"))
# print("SIM City index:")
# print(tree._get_index_of_item_in_tree("SIM City"))
# print("Treatment exists:")
# print(tree.item_exists_in_tree("0/1", "Treatment"))
# print("Treatment index:")
# print(tree._get_index_of_item_in_tree("Treatment"))
# print("Treatment Icon:")
# print(tree._get_item_icon("Treatment").get_icon_name())
# print("Treatment Expansion Icon classes:")
# print(tree._get_expansion_icon(item_label="Treatment").find().get_attribute(name="class"))
# print("SIM City Expansion Icon classes:")
# print(tree._get_expansion_icon(item_label="SIM City").find().get_attribute(name="class"))
# print("SIM City expanded:")
# print(tree.item_is_expanded("SIM City"))
# print("Items by path")
# print(tree._items_by_path)
# print("Icons")
# print(tree._item_icons)
# print("Items")
# print(tree._items)

#click_item_label(self, item_label: str, binding_wait_time: float = 0) -> None:
#expansion_icon_is_present_for_item(self, item_label: str) -> bool
#get_text_of_all_items_in_tree(self, wait_timeout: float = 5) -> List[str]:
#item_label_exists_in_tree(self, item_label: str, wait_timeout: int = 5) -> bool:
#item_is_expanded(self, item_label: str) -> bool:
#select_item_in_tree(self, item_label: str, wait_timeout: int = 5, binding_wait_time: int = 1)

#item_exists_in_tree(self, item_path: str, item_label: str, wait_timeout: int = 2) -> bool: