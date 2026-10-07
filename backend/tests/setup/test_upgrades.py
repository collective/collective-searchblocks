from collective.searchblocks import PACKAGE_NAME
from plone import api


PROFILE_ID = f"{PACKAGE_NAME}:default"


class TestUpgrades:
    def test_1001_adds_user_action(self, portal):
        """Test that upgrading to 1001 adds the search blocks user action."""
        actions = api.portal.get_tool("portal_actions")
        del actions.user["collective-searchblocks"]
        setup_tool = api.portal.get_tool("portal_setup")
        setup_tool.setLastVersionForProfile(PROFILE_ID, "1000")

        setup_tool.upgradeProfile(PROFILE_ID)

        assert "collective-searchblocks" in actions.user
        assert setup_tool.getLastVersionForProfile(PROFILE_ID) == ("1001",)
