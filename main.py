
import unittest

import OcularSCADA.API
import Tests.util
import Tests.AssetTests


# run asset unit tests
OcularSCADA.API.unit_tests('asset')


# run asset ui component tests
loader = unittest.TestLoader()
asset_suite = loader.loadTestsFromModule(Tests.AssetTests)

with open("/home/nate/Documents/test_results_UI", "w") as stream:
    unittest.TextTestRunner(stream=stream, verbosity=2).run(asset_suite)
