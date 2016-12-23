import requests
import datetime
import os
from tqdm import tqdm


class GameClip(object):
    def __init__(self, json_data, gamertag, download_root=os.getcwd()):
        self.json_data = json_data
        self.game_title = json_data["titleName"]  # Name of game clips is from, i.e. "Battlefield 4"
        self.clip_id = json_data["gameClipId"]  # Unique GUID of clip
        self.date_recorded_str = json_data["dateRecorded"]
        self.date_recorded = datetime.datetime.strptime(self.date_recorded_str, "%Y-%m-%d %H:%M:%S")
        self.type = json_data["type"]  # UserGenerated (GameDVR) or DeveloperInitiated (automatic)
        self.share_count = json_data["shareCount"]
        self.download_root = download_root
        self.gamertag = gamertag

        # Clips can have several uris for streaming or download, we only care about the download uri
        for uri in json_data["gameClipUris"]:
            if uri["uriType"] == "Download":
                self.download_uri = uri["uri"]
                self.filesize = uri["fileSize"]
                self.uri_expiration_date = datetime.datetime.strptime(uri["expiration"], "%Y-%m-%d %H:%M:%S")

    @property
    def local_filename(self):
        filename_date = self.date_recorded_str.replace(" ", "-").replace(":", "-")
        return "%s-%s-%s.mp4" % (self.game_title, filename_date, self.clip_id)

    @property
    def download_uri_expired(self):
        return self.uri_expiration_date < datetime.datetime.now()

    @property
    def download_path(self):
        """Download clips to <root_clip_directory>/<gamertag>/<game_title>/<type>/"""
        return os.path.join(self.download_root, self.gamertag, self.game_title, self.type)

    @property
    def full_path(self):
        return os.path.join(self.download_path, self.local_filename)

    @property
    def is_downloaded(self):
        """Compare local and remote file sizes to determine if clip is already completely downloaded"""
        if os.path.isfile(self.full_path) and os.path.getsize(self.full_path) == self.filesize:
            return True
        return False

    def download_clip(self):
        chunk_size = 1024
        if not os.path.isdir(self.download_path):
            os.makedirs(self.download_path)
        if self.is_downloaded:
            print "Skipping %s" % self.local_filename
            return
        r = requests.get(self.download_uri, stream=True)
        print "Downloading %s..." % self.local_filename
        with open(self.full_path, "wb") as f:
            for chunk in tqdm(iterable=r.iter_content(chunk_size=chunk_size), desc="Downloading",
                              total=self.filesize/chunk_size, unit="KB", unit_scale=False, leave=False):
                f.write(chunk)
        r.close()
