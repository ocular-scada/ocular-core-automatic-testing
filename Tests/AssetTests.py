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
        self.model_editor.clickAssetEditorTab()
		
    def tearDown(self):
        OcularSCADA.API.rpc("ocular.asset_test.Setup.dropTables")


	# Test calculated path and calculated children
    def test_add(self):

        new_assets = [  ("", {'editAsset.name': "SIM City", 'editAsset.description': "Root description", 'editAsset.type': "WaterAsset/Container/WaterSystem"}),
                        ("0", {'editAsset.name': "Wells", 'editAsset.description': "Wells description", 'editAsset.type': "WaterAsset/Container/ProcessStage"}),
                        ("0", {'editAsset.name': "Treatment", 'editAsset.type': "WaterAsset/Container/ProcessStage"}),
                        ("0", {'editAsset.name': "Distribution", 'editAsset.type': "WaterAsset/Container/ProcessStage"}),
                        ("0/0", {'editAsset.name': "Well 1", 'editAsset.type': "WaterAsset/Container/Process"}),
                        ("0/0", {'editAsset.name': "Well 2", 'editAsset.type': "WaterAsset/Container/Process"}),
                        ("0/0/0", {'editAsset.name': "Well Pump", 'editAsset.type': "WaterAsset/Component/Device/Motor", 'editAsset.path': "Custom/Tag/Path"}),
                        ("0/0/1", {'editAsset.name': "Well Pump", 'editAsset.type': "WaterAsset/Component/Device/Motor"})
                        ]

        orders = []
        item_path = None
        index = 0
        for asset in new_assets:
            if asset[0] != item_path:
                item_path = asset[0]
                index = 0
                orders.append(index)
            else:
                index = index + 1
                orders.append(index)
                


        for i, asset in enumerate(new_assets):

            self.model_editor.add_asset(asset[0], asset[1])

            time.sleep(.5)

        for i, asset in enumerate(new_assets):

            # is child
            self.assertTrue(self.model_editor.tree_editor.tree.is_child(parent_item_path=asset[0], name=asset[1]['editAsset.name']))
            # correct child order
            self.assertEqual(self.model_editor.tree_editor.tree.child_order(parent_item_path=asset[0], name=asset[1]['editAsset.name']), orders[i])





class TestTypeModel(unittest.TestCase):
	
    def setUp(self):
        OcularSCADA.API.rpc("ocular.asset_test.Setup.dropTables")
        OcularSCADA.API.rpc("ocular.asset_test.Setup.createTables")

        self.driver = Tests.util.open_browser()
        self.model_editor = ModelEditorPage(self.driver, '', '')
        self.model_editor.open_menu_item("model")
        self.model_editor.clickTypeEditorTab()
		
    def tearDown(self):
        OcularSCADA.API.rpc("ocular.asset_test.Setup.dropTables")


	# Test calculated path and calculated children
    def test_add(self):

        new_assets = [  ("", {'editType.name': "WaterAsset", 'editType.description': "Root description", 'editType.type': "WaterAsset/Container/WaterSystem"}),
                        ("0", {'editType.name': "Wells", 'editType.description': "Wells description", 'editType.type': "WaterAsset/Container/ProcessStage"}),
                        ("0", {'editType.name': "Treatment", 'editType.type': "WaterAsset/Container/ProcessStage"}),
                        ("0", {'editType.name': "Distribution", 'editType.type': "WaterAsset/Container/ProcessStage"}),
                        ("0/0", {'editType.name': "Well 1", 'editType.type': "WaterAsset/Container/Process"}),
                        ("0/0", {'editType.name': "Well 2", 'editType.type': "WaterAsset/Container/Process"}),
                        ("0/0/0", {'editType.name': "Well Pump", 'editType.type': "WaterAsset/Component/Device/Motor", 'editType.path': "Custom/Tag/Path"}),
                        ("0/0/1", {'editType.name': "Well Pump", 'editType.type': "WaterAsset/Component/Device/Motor"})
                        ]

        orders = []
        item_path = None
        index = 0
        for asset in new_assets:
            if asset[0] != item_path:
                item_path = asset[0]
                index = 0
                orders.append(index)
            else:
                index = index + 1
                orders.append(index)
                


        for i, asset in enumerate(new_assets):

            self.model_editor.add_asset(asset[0], asset[1])

            time.sleep(.5)

        for i, asset in enumerate(new_assets):

            # is child
            self.assertTrue(self.model_editor.tree_editor.tree.is_child(parent_item_path=asset[0], name=asset[1]['editAsset.name']))
            # correct child order
            self.assertEqual(self.model_editor.tree_editor.tree.child_order(parent_item_path=asset[0], name=asset[1]['editAsset.name']), orders[i])