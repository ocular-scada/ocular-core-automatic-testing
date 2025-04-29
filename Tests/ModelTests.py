import unittest
import time

from OcularSCADA.Framework.OcularPage import OcularPage
from OcularSCADA.Framework.SideBarMenu import SideBarMenu
from OcularSCADA.Model.ModelEditorPage import ModelEditorPage
import OcularSCADA.API

import Tests.util

# print(OcularSCADA.API.rpc("ocular.asset.Asset.getIndexPath", [6]))
# print(OcularSCADA.API.rpc("ocular.asset.Asset.getNamePath", [6]))



class HierarchicalModel(unittest.TestCase):


    def add_items(self, new_items, name_key='editAsset.name'):

        # get child order from item_path
        orders = []
        item_path = None
        index = 0
        for item in new_items:
            if item[0] != item_path:
                item_path = item[0]
                index = 0
                orders.append(index)
            else:
                index = index + 1
                orders.append(index)
                
        for i, item in enumerate(new_items):

            self.model_editor.add_item(item[0], item[1])

        for i, item in enumerate(new_items):

            # is child
            self.assertTrue(self.model_editor.tree_editor.tree.is_child(parent_item_path=item[0], name=item[1][name_key]))
            # correct child order
            self.assertEqual(self.model_editor.tree_editor.tree.child_order(parent_item_path=item[0], name=item[1][name_key]), orders[i])





class TestAssetModel(HierarchicalModel):
	
    def setUp(self):
        OcularSCADA.API.rpc("ocular.asset_test.Setup.dropTables")
        OcularSCADA.API.rpc("ocular.asset_test.Setup.createTables")
        OcularSCADA.API.rpc("ocular.asset_test.Setup.initializeTypeTable")

        self.driver = Tests.util.open_browser()
        self.model_editor = ModelEditorPage(self.driver, '', '')
        self.model_editor.open_menu_item("/dash-layout/model")
        self.model_editor.clickAssetEditorTab()
		
    def tearDown(self):
        OcularSCADA.API.rpc("ocular.asset_test.Setup.dropTables")







	# Test calculated path and calculated children
    def test_add(self):

        new_items = [  ("", {'editAsset.name': "SIM City", 'editAsset.description': "Root description", 'editAsset.type': "WaterAsset/Container/WaterSystem"}),
                        ("0", {'editAsset.name': "Wells", 'editAsset.description': "Wells description", 'editAsset.type': "WaterAsset/Container/ProcessStage"}),
                        ("0", {'editAsset.name': "Treatment", 'editAsset.type': "WaterAsset/Container/ProcessStage"}),
                        ("0", {'editAsset.name': "Distribution", 'editAsset.type': "WaterAsset/Container/ProcessStage"}),
                        ("0/0", {'editAsset.name': "Well 1", 'editAsset.type': "WaterAsset/Container/Process"}),
                        ("0/0", {'editAsset.name': "Well 2", 'editAsset.type': "WaterAsset/Container/Process"}),
                        ("0/0/0", {'editAsset.name': "Well Pump", 'editAsset.type': "WaterAsset/Component/Device/Motor", 'editAsset.path': "Custom/Tag/Path"}),
                        ("0/0/1", {'editAsset.name': "Well Pump", 'editAsset.type': "WaterAsset/Component/Device/Motor"})
                        ]

        self.add_items(new_items, name_key='editAsset.name')







class TestTypeModel(HierarchicalModel):
	
    def setUp(self):
        OcularSCADA.API.rpc("ocular.asset_test.Setup.dropTables")
        OcularSCADA.API.rpc("ocular.asset_test.Setup.createTables")

        self.driver = Tests.util.open_browser()
        self.model_editor = ModelEditorPage(self.driver, '', '')
        self.model_editor.open_menu_item("/dash-layout/model")
        self.model_editor.clickTypeEditorTab()
		
    def tearDown(self):
        OcularSCADA.API.rpc("ocular.asset_test.Setup.dropTables")



	# Test calculated path and calculated children
    def test_add(self):

        new_items = [  ("", {'editType.name': "WaterAsset", 'editType.description': "Root type description", 'editType.path': "OcularScada/WaterAsset", 'editType.container':True}),
                        ("0", {'editType.name': "Container", 'editType.description': "", 'editType.path': "OcularScada/WaterAsset/Container", 'editType.container':True}),
                        ("0", {'editType.name': "Component", 'editType.path': "OcularScada/WaterAsset/Component/Component", 'editType.container':False}),
                        ("0/0", {'editType.name': "Process", 'editType.path': "OcularScada/WaterAsset/Container/Process", 'editType.container':True}),
                        ("0/1", {'editType.name': "Device", 'editType.path': "OcularScada/WaterAsset/Component/Device/Device", 'editType.container':False}),
                        ("0/1", {'editType.name': "Control", 'editType.path': "OcularScada/WaterAsset/Component/Control/Control", 'editType.container':False}),
                        ("0/1", {'editType.name': "Alarm", 'editType.path': "OcularScada/WaterAsset/Component/Alarm/Alarm", 'editType.container':False}),
                        ("0/1/0", {'editType.name': "Motor", 'editType.path': "OcularScada/WaterAsset/Component/Device/Motor/Motor", 'editType.container':False})
                        ]
    
        self.add_items(new_items, name_key='editType.name')

        # todo - add path that does not exist
