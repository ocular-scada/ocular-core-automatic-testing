import unittest
import time

from OcularSCADA.Framework.OcularPage import OcularPage
from OcularSCADA.Framework.SideBarMenu import SideBarMenu
from OcularSCADA.Model.ModelEditorPage import ModelEditorPage
import OcularSCADA.API

import Tests.util

# print(OcularSCADA.API.rpc("ocular.asset.Asset.getIndexPath", [6]))
# print(OcularSCADA.API.rpc("ocular.asset.Asset.getNamePath", [6]))

class TestAssetModel(unittest.TestCase):
	
    def setUp(self):
        OcularSCADA.API.rpc("ocular.asset_test.Setup.dropTables")
        OcularSCADA.API.rpc("ocular.asset_test.Setup.createTables")
        OcularSCADA.API.rpc("ocular.asset_test.Setup.initializeTypeTable")

        self.driver = Tests.util.open_browser()
        self.model_editor = ModelEditorPage(self.driver, '', '')
        self.model_editor.open_menu_item("model")
        self.model_editor.clickModelEditorTab()
		
    def tearDown(self):
        OcularSCADA.API.rpc("ocular.asset_test.Setup.dropTables")


	# Test calculated path and calculated children
    def test_add_asset(self):



        new_assets = [  ("", {'editAsset.name': "SIM City", 'editAsset.description': "Root description", 'editAsset.type': "WaterAsset/Container/WaterSystem"}),
                        ("0", {'editAsset.name': "Wells", 'editAsset.description': "Wells description", 'editAsset.type': "WaterAsset/Container/ProcessStage"}),
                        ("0", {'editAsset.name': "Treatment", 'editAsset.type': "WaterAsset/Container/ProcessStage"}),
                        ("0", {'editAsset.name': "Distribution", 'editAsset.type': "WaterAsset/Container/ProcessStage"}),
                        ("0/0", {'editAsset.name': "Well 1", 'editAsset.type': "WaterAsset/Container/Process"}),
                        ("0/0", {'editAsset.name': "Well 2", 'editAsset.type': "WaterAsset/Container/Process"}),
                        ("0/0/0", {'editAsset.name': "Well Pump", 'editAsset.type': "WaterAsset/Component/Device/Motor", 'editAsset.path': "Custom/Tag/Path"}),
                        ("0/0/1", {'editAsset.name': "Well Pump", 'editAsset.type': "WaterAsset/Component/Device/Motor"})
                        ]

        
        for asset in new_assets:

            self.model_editor.add_asset(asset[0], asset[1])

            time.sleep(.5)

            # todo - check if correct

