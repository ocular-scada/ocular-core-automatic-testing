from selenium.webdriver.common.by import By # type: ignore
import unittest
import time
import HtmlTestRunner # type: ignore

import OcularSCADA.API
import Tests.util
import Tests.ModelTests

from OcularSCADA.Model.ModelEditorPage import ModelEditorPage
from OcularSCADA.Framework.OcularPage import OcularPage
from OcularSCADA.Framework.ProgressiveTree import ProgressiveTree
from OcularSCADA.Framework.FormValueBased import FormValueBased



# ---- RPC examples ----
# print(OcularSCADA.API.rpc("ocular.asset.Asset.getIndexPath", [6]))
# print(OcularSCADA.API.rpc("ocular.asset.Asset.getNamePath", [6]))



# ---- run unit tests ----
OcularSCADA.API.unit_tests('asset')


# ---- run ui functional tests ----
loader = unittest.TestLoader()
asset_suite = loader.loadTestsFromModule(Tests.ModelTests)
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="FunctionalTestReport", report_title="UI Functional Tests", add_timestamp=False).run(asset_suite)


