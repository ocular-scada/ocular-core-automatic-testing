
import unittest
import time

import OcularSCADA.API
import Tests.util
import Tests.AssetTests

from OcularSCADA.Model.ModelEditorPage import ModelEditorPage
from OcularSCADA.Framework.OcularPage import OcularPage

# # run asset unit tests
# OcularSCADA.API.unit_tests('asset')


# # run asset ui component tests
# loader = unittest.TestLoader()
# asset_suite = loader.loadTestsFromModule(Tests.AssetTests)

# with open("/home/nate/Documents/test_results_UI", "w") as stream:
#     unittest.TextTestRunner(stream=stream, verbosity=2).run(asset_suite)


driver = Tests.util.open_browser()
page_inst = OcularPage(driver, '', '')
page_inst.open_menu_item("model")


page_inst = ModelEditorPage(driver, '', '')
time.sleep(1)
slideOutOpen = page_inst.isSlideOutOpen()
print("Model page opened. Is slideout opened? " + str(slideOutOpen))


page_inst.clickAssetControlIcon("add")
time.sleep(1)
slideOutOpen = page_inst.isSlideOutOpen()
print("Add icon clicked. Is slideout opened? " + str(slideOutOpen))


page_inst.clickAssetControlIcon("advanced")

page_inst.clickTypeEditorTab()
page_inst.clickModelEditorTab()
