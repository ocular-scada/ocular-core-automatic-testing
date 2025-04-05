import unittest

from OcularSCADA.Framework.OcularPage import OcularPage
from OcularSCADA.Framework.SideBarMenu import SideBarMenu
from OcularSCADA.Model.ModelEditorPage import ModelEditorPage
from OcularSCADA import API

import Tests.util

# print(OcularSCADA.API.rpc("ocular.asset.Asset.getIndexPath", [6]))
# print(OcularSCADA.API.rpc("ocular.asset.Asset.getNamePath", [6]))

class TestAssetModel(unittest.TestCase):
	
    def setUp(self):
        API.rpc("ocular.asset_test.Setup.dropTables")
        API.rpc("ocular.asset_test.Setup.createTables")
        API.rpc("ocular.asset_test.Setup.initializeTypeTable")

        self.driver = Tests.util.open_browser()
        self.page_inst = OcularPage(self.driver, '', '')
        self.page_inst.open_menu_item("model")
        self.page_inst = ModelEditorPage(self.driver, '', '')

		
    def tearDown(self):
        API.rpc("ocular.asset_test.Setup.dropTables")



    def _add_asset(self, parent_item_path, details):
        pass

	# Test calculated path and calculated children
    def test_add_asset(self):


        new_assets = [  ("", {'name': "SIM City", 'description': "Root description", 'type': "WaterAsset/Container/WaterSystem", 'tag_path': ""}),
                        ("0", {'name': "Wells", 'description': "Wells description", 'type': "WaterAsset/Container/ProcessStage", 'tag_path': ""}),
                        ("0", {'name': "Treatment", 'type': "WaterAsset/Container/ProcessStage", 'tag_path': ""}),
                        ("0", {'name': "Distribution", 'type': "WaterAsset/Container/ProcessStage", 'tag_path': ""}),
                        ("0/0", {'name': "Well 1", 'type': "WaterAsset/Container/Process", 'tag_path': ""}),
                        ("0/0", {'name': "Well 2", 'type': "WaterAsset/Container/Process", 'tag_path': ""}),
                        ("0/0/0", {'name': "Well Pump", 'type': "WaterAsset/Component/Device/Motor", 'tag_path': "Custom/Tag/Path"}),
                        ("0/0/1", {'name': "Well Pump", 'type': "WaterAsset/Component/Device/Motor", 'tag_path': ""})
                        ]

        
        # add root asset

        self.page_inst.clickAssetControlIcon("add")
        self.assertTrue(self.page_inst.isSlideOutOpen())

        # TODO  - edit the slideout
        #       - hit save


        #       - check asset exists in tree by parent_item_path and name



        






        # add child 1 asset



        # add child 2 asset
