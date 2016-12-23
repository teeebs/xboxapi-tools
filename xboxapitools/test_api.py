import unittest
from api import XboxApi

gamertag = "Major Nelson"
major_xuid = 2584878536129841
title_id = 252034287  # Skyrim Special Edition
xboxapi = XboxApi()
me = xboxapi.get_xuid()
my_gamertag, my_xuid = me.data["gamertag"], me.data["xuid"]


class TestXboxApi(unittest.TestCase):
    def setUp(self):
        self.xboxapi = xboxapi
        self.me = me

    def test_get_profile(self):
        self.assertTrue(type(self.xboxapi.get_profile()) == dict)

    def test_get_profile(self):
        self.assertEqual(self.xboxapi.get_profile().status_code, 200)

    def test_get_xuid(self):
        self.assertEqual(self.xboxapi.get_xuid().status_code, 200)

    def test_get_messages(self):
        self.assertEqual(self.xboxapi.get_messages().status_code, 200)

    def test_get_conversations(self):
        self.assertEqual(self.xboxapi.get_conversations().status_code, 200)

    def test_get_xuid_by_gamertag(self):
        self.assertEqual(self.xboxapi.get_xuid_by_gamertag(gamertag).status_code, 200)

    def test_get_gamertag_by_xuid(self):
        self.assertEqual(self.xboxapi.get_gamertag_by_xuid(major_xuid).status_code, 200)

    def test_get_user_profile(self):
        self.assertEqual(self.xboxapi.get_user_profile(major_xuid).status_code, 200)

    def test_get_user_gamercard(self):
        self.assertEqual(self.xboxapi.get_user_gamercard(major_xuid).status_code, 200)

    def test_get_user_presence(self):
        self.assertEqual(self.xboxapi.get_user_presence(major_xuid).status_code, 200)

    def test_get_user_activity(self):
        self.assertEqual(self.xboxapi.get_user_activity(major_xuid).status_code, 200)

    def test_get_user_activity_recent(self):
        self.assertEqual(self.xboxapi.get_user_activity_recent(major_xuid).status_code, 200)

    def test_get_user_friends(self):
        self.assertEqual(self.xboxapi.get_user_friends(major_xuid).status_code, 200)

    def test_get_user_followers(self):
        self.assertEqual(self.xboxapi.get_user_followers(my_xuid).status_code, 200)

    def test_get_recent_players(self):
        self.assertEqual(self.xboxapi.get_recent_players().status_code, 200)

    def test_get_user_gameclips(self):
        self.assertEqual(self.xboxapi.get_user_gameclips(major_xuid).status_code, 200)

    def test_get_user_saved_gameclips(self):
        self.assertEqual(self.xboxapi.get_user_saved_gameclips(major_xuid).status_code, 200)

    def test_get_user_saved_gameclips_by_title(self):
        self.assertEqual(self.xboxapi.get_user_saved_gameclips_by_title(major_xuid, title_id).status_code, 200)

    def test_get_saved_gameclips(self):
        self.assertEqual(self.xboxapi.get_saved_gameclips(title_id).status_code, 200)

    def test_get_user_screenshots(self):
        self.assertEqual(self.xboxapi.get_user_screenshots(major_xuid).status_code, 200)

    def test_get_user_saved_screenshots(self):
        self.assertEqual(self.xboxapi.get_user_saved_screenshots(major_xuid, title_id).status_code, 200)

    def test_get_saved_screenshots(self):
        self.assertEqual(self.xboxapi.get_saved_screenshots(title_id).status_code, 200)

    def test_get_user_game_stats(self):
        self.assertEqual(self.xboxapi.get_user_game_stats(major_xuid, title_id).status_code, 200)

    def test_get_user_xbox360games(self):
        self.assertEqual(self.xboxapi.get_user_xbox360games(major_xuid).status_code, 200)

    def test_get_user_xboxonegames(self):
        self.assertEqual(self.xboxapi.get_user_xboxonegames(major_xuid).status_code, 200)

    def test_get_user_achievements(self):
        self.assertEqual(self.xboxapi.get_user_achievements(major_xuid, title_id).status_code, 200)

    def test_get_game_info_hex(self):
        self.assertEqual(self.xboxapi.get_game_info_hex(title_id).status_code, 200)

    # def test_get_game_info(self):
    #     self.assertEqual(self.xboxapi.get_game_info().status_code, 200)

    # def test_get_game_addons(self):
    #     self.assertEqual(self.xboxapi.get_game_addons().status_code, 200)

    # def test_get_game_related(self):
    #     self.assertEqual(self.xboxapi.get_game_related().status_code, 200)

    def test_get_latest_xbox360games(self):
        self.assertEqual(self.xboxapi.get_latest_xbox360games().status_code, 200)

    def test_get_latest_xboxonegames(self):
        self.assertEqual(self.xboxapi.get_latest_xboxonegames().status_code, 200)

    def test_get_latest_xboxoneapps(self):
        self.assertEqual(self.xboxapi.get_latest_xboxoneapps().status_code, 200)

    def test_get_xboxone_gold(self):
        self.assertEqual(self.xboxapi.get_xboxone_gold().status_code, 200)

    def test_get_xbox360games(self):
        self.assertEqual(self.xboxapi.get_xbox360games().status_code, 200)

    def test_get_xboxonegames(self):
        self.assertEqual(self.xboxapi.get_xboxonegames().status_code, 200)

    def test_get_xboxoneapps(self):
        self.assertEqual(self.xboxapi.get_xboxoneapps().status_code, 200)

    def test_get_user_activity_feed(self):
        self.assertEqual(self.xboxapi.get_user_activity_feed().status_code, 200)

    def test_get_user_titlehub_achievements(self):
        self.assertEqual(self.xboxapi.get_user_titlehub_achievements(major_xuid).status_code, 200)


if __name__ == "__main__":
    unittest.main()
