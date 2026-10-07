from collective.searchblocks import PACKAGE_NAME
from plone import api

import pytest


class TestSetupUninstall:
    @pytest.fixture(autouse=True)
    def uninstalled(self, installer):
        installer.uninstall_product(PACKAGE_NAME)

    def test_addon_uninstalled(self, installer):
        """Test if collective.searchblocks is uninstalled."""
        assert installer.is_product_installed(PACKAGE_NAME) is False

    def test_browserlayer_not_registered(self, browser_layers):
        """Test that IBrowserLayer is not registered."""
        from collective.searchblocks.interfaces import IBrowserLayer

        assert IBrowserLayer not in browser_layers

    def test_user_action_removed(self, portal):
        """Test that the user menu no longer links to the search blocks page."""
        actions = api.portal.get_tool("portal_actions")
        assert "collective-searchblocks" not in actions.user
