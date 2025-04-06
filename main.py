from selenium.webdriver.common.by import By # type: ignore
import unittest
import time

import OcularSCADA.API
import Tests.util
import Tests.AssetTests

from OcularSCADA.Model.ModelEditorPage import ModelEditorPage
from OcularSCADA.Framework.OcularPage import OcularPage
from OcularSCADA.Framework.ProgressiveTree import ProgressiveTree
from OcularSCADA.Framework.FormValueBased import FormValueBased



# print(OcularSCADA.API.rpc("ocular.asset.Asset.getIndexPath", [6]))
# print(OcularSCADA.API.rpc("ocular.asset.Asset.getNamePath", [6]))

# run asset unit tests
#OcularSCADA.API.unit_tests('asset')


# run asset ui component tests
loader = unittest.TestLoader()
asset_suite = loader.loadTestsFromModule(Tests.AssetTests)

with open("/home/nate/Documents/test_results_UI", "w") as stream:
    unittest.TextTestRunner(stream=stream, verbosity=2).run(asset_suite)


# driver = Tests.util.open_browser()
# model_editor = ModelEditorPage(driver, '', '')
# model_editor.open_menu_item("model")
# model_editor.clickModelEditorTab()
# model_editor.add_asset("0/0", {'editAsset.name': "Well 3", 'editAsset.description':"Description of this well", 'editAsset.type': "WaterAsset/Container/Process"})
# time.sleep(2)