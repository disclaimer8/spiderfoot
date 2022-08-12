import pytest
import unittest

from modules.sfp_hackertarget import sfp_hackertarget
from sflib import SpiderFoot


@pytest.mark.usefixtures
class TestModuleHackertarget(unittest.TestCase):

    def test_opts(self):
        module = sfp_hackertarget()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        sf = SpiderFoot(self.default_options)
        module = sfp_hackertarget()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_hackertarget()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_hackertarget()
        self.assertIsInstance(module.producedEvents(), list)
