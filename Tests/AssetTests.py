import unittest

from OcularSCADA.Framework.OcularPage import OcularPage
from OcularSCADA.Framework.SideBarMenu import SideBarMenu
from OcularSCADA import API

import Tests.util


class TestEditModel(unittest.TestCase):
	
    def setUp(self):
        API.rpc("ocular.asset_test.Setup.dropTables")
        API.rpc("ocular.asset_test.Setup.createTables")
        API.rpc("ocular.asset_test.Setup.initializeTypeTable")

        self.driver = Tests.util.open_browser()
        self.page_inst = OcularPage(self.driver, '', '')
        self.page_inst.open_menu_item("model")

		
    def tearDown(self):
        API.rpc("ocular.asset_test.Setup.dropTables")


	# Test calculated path and calculated children
    def test_add_asset(self):

        self.assertEqual(2,2)

        # add root asset


        # add child 1 asset



        # add child 2 asset
