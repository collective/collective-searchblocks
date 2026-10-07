from collective.searchblocks import PACKAGE_NAME
from plone import api


class TestSetupInstall:
    def test_addon_installed(self, installer):
        """Test if collective.searchblocks is installed."""
        assert installer.is_product_installed(PACKAGE_NAME) is True

    def test_browserlayer(self, browser_layers):
        """Test that IBrowserLayer is registered."""
        from collective.searchblocks.interfaces import IBrowserLayer

        assert IBrowserLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of default profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:default") == "1001"

    def test_user_action(self, portal):
        """Test that the user menu links to the search blocks page."""
        actions = api.portal.get_tool("portal_actions")
        action = actions.user["collective-searchblocks"]
        assert action.url_expr == "string:/controlpanel/search-blocks"
        assert action.permissions == ("collective.searchblocks: Search Blocks",)
