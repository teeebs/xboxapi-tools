import requests
import datetime
import json

__version__ = 0.1


class XboxApi(object):
    def __init__(self, api_key=None, language=None, base_url=""):
        self.api_key = api_key
        if not self.api_key:
            import os
            self.api_key = os.environ.get("XBOXAPIKEY", None)
        if not self.api_key:
            raise ValueError("You must provide an XboxAPI.com API key or set XBOXAPIKEY environment variable")
        self.language = language
        self.base_url = base_url
        if not self.base_url:
            self.base_url = "https://xboxapi.com/v2"

    def get(self, url):
        """
        Make a GET request to the Xbox API
        :param url: Endpoint and parameters to append to self.base_url
        :return: XboxApiResponse
        """
        # Build headers
        headers = {"X-AUTH": self.api_key}
        if self.language:
            headers["Accept-Language"] = self.language
        # Make request and build response
        response = requests.get("{}{}".format(self.base_url, url), headers=headers)
        return XboxApiResponse(self, url, response)

    def post(self, url, data):
        """
        Make POST request to the Xbox API for sending messages
        :param url: Endpoint and parameters to append to self.base_url
        :param data: Message payload to send
        :return: Success boolean
        """
        headers = {
            "X-AUTH": self.api_key,
            "Content-Type": "application/json"
        }
        response = requests.post("{}{}".format(self.base_url, url), headers=headers, data=json.dumps(data))

        return response.status_code == 200

    def get_profile(self):
        """This is your profile information"""
        return self.get("/profile")

    def get_xuid(self):
        """This is your account XUID (Xbox Account User ID)"""
        return self.get("/accountXuid")

    def get_messages(self):
        """These are your message with full preview"""
        return self.get("/messages")

    def get_conversations(self):
        """These are your conversations with full preview of the last message sent/received"""
        return self.get("/conversations")

    def get_xuid_by_gamertag(self, gamertag):
        """This is the XUID for a specified Gamertag (Xbox Account User ID)"""
        return self.get("/xuid/{}".format(gamertag))

    def get_gamertag_by_xuid(self, xuid):
        """This is the Gamertag for a specified XUID (Xbox Account User ID)"""
        return self.get("/gamertag/{}".format(xuid))

    def get_user_profile(self, xuid):
        """This is the Profile for a specified XUID"""
        return self.get("/{}/profile".format(xuid))

    def get_user_gamercard(self, xuid):
        """This is the Gamercard information for a specified XUID"""
        return self.get("/{}/gamercard".format(xuid))

    def get_user_presence(self, xuid):
        """This is the current presence information for a specified XUID"""
        return self.get("/{}/presence".format(xuid))

    def get_user_activity(self, xuid):
        """This is the current activity information for a specified XUID"""
        return self.get("/{}/activity".format(xuid))

    def get_user_activity_recent(self, xuid):
        """This is the recent activity information for a specified XUID"""
        return self.get("/{}/activity/recent".format(xuid))

    def get_user_friends(self, xuid):
        """This is the friends information for a specified XUID"""
        return self.get("/{}/friends".format(xuid))

    def get_user_followers(self, xuid):
        """This is the followers information for a specified XUID"""
        return self.get("/{}/followers".format(xuid))

    def get_recent_players(self):
        """This is accounts recent players information"""
        return self.get("/recent-players")

    def get_user_gameclips(self, xuid):
        """This is the game clips for a specified XUID"""
        return self.get("/{}/game-clips".format(xuid))

    def get_user_saved_gameclips(self, xuid):
        """This is the saved game clips for a specified XUID"""
        return self.get("/{}/game-clips/saved".format(xuid))

    def get_user_saved_gameclips_by_title(self, xuid, title_id):
        """This is the saved game clips for a specified XUID, and Game (titleId)"""
        return self.get("/{}/game-clips/{}".format(xuid, title_id))

    def get_saved_gameclips(self, title_id):
        """This is the saved game clips for a specified Game (titleId)"""
        return self.get("/game-clips/{}".format(title_id))

    def get_user_screenshots(self, xuid):
        """This is the screenshots for a specified XUID"""
        return self.get("/{}/screenshots".format(xuid))

    def get_user_saved_screenshots(self, xuid, title_id):
        """This is the saved screenshots for a specified XUID, and Game (titleId)"""
        return self.get("/{}/screenshots/{}".format(xuid, title_id))

    def get_saved_screenshots(self, title_id):
        """This is the saved screenshots for a specified Game (titleId)"""
        return self.get("/screenshots/{}".format(title_id))

    def get_user_game_stats(self, xuid, title_id):
        """This is the game stats for a specified XUID, on a specified game. (i.e. Driver Level on Forza etc.)"""
        return self.get("/{}/game-stats/{}".format(xuid, title_id))

    def get_user_xbox360games(self, xuid):
        """This is the Xbox 360 Games List for a specified XUID"""
        return self.get("/{}/xbox360games".format(xuid))

    def get_user_xboxonegames(self, xuid):
        """This is the Xbox One Games List for a specified XUID"""
        return self.get("/{}/xboxonegames".format(xuid))

    def get_user_achievements(self, xuid, title_id):
        """This is the Xbox Games Achievements for a specified XUID"""
        return self.get("/{}/achievements/{}".format(xuid, title_id))

    def get_game_info_hex(self, game_id):
        """This is the Xbox Game Information (using the game id in hex format)"""
        return self.get("/game-details-hex/{}".format(game_id))

    def get_game_info(self, product_id):
        """This is the Xbox Game Information (using the product id)"""
        return self.get("/game-details/{}".format(product_id))

    def get_game_addons(self, product_id):
        """This is the Xbox Game Information (using the product id)"""
        return self.get("/game-details/{}/addons".format(product_id))

    def get_game_related(self, product_id):
        """This is the Xbox Game Information (using the product id)"""
        return self.get("/game-details/{}/related".format(product_id))

    def get_latest_xbox360games(self):
        """This gets the latest Xbox 360 Games from the Xbox LIVE marketplace"""
        return self.get("/latest-xbox360-games")

    def get_latest_xboxonegames(self):
        """This gets the latest Xbox One Games from the Xbox LIVE marketplace"""
        return self.get("/latest-xboxone-games")

    def get_latest_xboxoneapps(self):
        """This gets the latest Xbox One Apps from the Xbox LIVE marketplace"""
        return self.get("/latest-xboxone-apps")

    def get_xboxone_gold(self):
        """These are the free "Games with Gold", and "Deals with Gold" from the Xbox LIVE marketplace"""
        return self.get("/xboxone-gold-lounge")

    def get_xbox360games(self):
        """Browse the Xbox LIVE marketplace for Xbox 360 content."""
        return self.get("/browse-marketplace/xbox360/1?sort=releaseDate")

    def get_xboxonegames(self):
        """Browse the Xbox LIVE marketplace for Xbox One Game content."""
        return self.get("/browse-marketplace/games/1?sort=releaseDate")

    def get_xboxoneapps(self):
        """Browse the Xbox LIVE marketplace for Xbox One App content."""
        return self.get("/browse-marketplace/apps/1?sort=releaseDate")

    def get_user_activity_feed(self):
        """Show your activity feed."""
        return self.get("/activity-feed")

    def get_user_titlehub_achievements(self, xuid):
        """Show your achievements list by game with friends who also play. (New TitleHub endpoint)"""
        return self.get("/{}/titlehub-achievement-list".format(xuid))

    def send_message(self, message, xuid=None, xuids=None):
        """Send a message from your account to other users"""
        payload = {
            "message": message,
            "to": []
        }

        if not xuid and not xuids:
            raise ValueError("You must provide an xuid or list of xuids to send a message to.")

        if not xuids:
            xuids = []

        if xuid:
            xuids.append(xuid)

        for xuid in xuids:
            payload["to"].append(xuid)

        return self.post("/messages", payload)

    def send_activity_feed(self, message):
        """Send a post to your activity feed"""
        payload = {
            "message": message
        }

        return self.post("activity-feed", payload)


class XboxApiResponse(object):
    def __init__(self, api, url, response):
        self.api = api
        self.url = url
        self.response = response
        try:
            json = response.json()
        except ValueError:
            json = response.content
        self.data = json
        self._set_metadata(response)

    def _set_metadata(self, response):
        self.next_url = None
        self.status_code = response.status_code
        self.continuation_token = response.headers.get("X-Continuation-Token")
        self.rate_limit = int(response.headers.get("X-RateLimit-Limit"))
        self.rate_remaining = int(response.headers.get("X-RateLimit-Remaining"))
        self.rate_reset = int(response.headers.get("X-RateLimit-Reset"))
        self.rate_reset_datetime = datetime.datetime.now() + datetime.timedelta(seconds=self.rate_reset)
        if self.continuation_token:
            self.next_url = "{}{}continuationToken={}".format(self.url,
                                                              "&" if "?" in self.url else "?",
                                                              self.continuation_token)

    def __iter__(self):
        return self

    def next(self):
        if self.continuation_token:
            return self.api.get(self.next_url)
        else:
            raise StopIteration()

    def fill_data(self, maximum=None):
        """
        Make additional API calls and aggregate subsequent records up to `maximum` or
        until no continuation token is returned.
        :param maximum: Maximum number of records to return
        :return: XboxApiResponse
        """
        while self.continuation_token and type(self.data) == list:
            next_response = self.next()
            # Merge new list with existing list
            self.data.extend(next_response.data)
            # Overwrite this responses metadata with latest
            self._set_metadata(next_response.response)
            if maximum and len(self.data) >= maximum:
                self.data = self.data[:maximum]
                break
