#!/usr/bin/env python
from xboxapitools.api import XboxApi
from xboxapitools.clip import GameClip


def get_clips(apikey, gamertag, game_title_filter=None, automatic_clips=False, limit=None, share_count=None):
    api = XboxApi(apikey)
    xuid = api.get_xuid_by_gamertag(gamertag).data
    game_clips = [GameClip(clip, gamertag) for clip in api.get_user_gameclips(xuid).data]
    # Filter out any game_clips from games that do not match provided game filter
    if game_title_filter:
        game_clips = [clip for clip in game_clips if game_title_filter in clip.game_title]
    # Filter out automatic game_clips
    if not automatic_clips:
        game_clips = [clip for clip in game_clips if clip.type == "UserGenerated"]
    # Filter out any game_clips that don't meet the share threshold
    if share_count:
        game_clips = [clip for clip in game_clips if clip.share_count >= share_count]
    # Filter out any game_clips that have already been completely downloaded
    game_clips = [clip for clip in game_clips if clip.is_downloaded is False]
    # Only get top n results, after filtering
    if limit:
        game_clips = game_clips[0:limit]
    return game_clips

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Arg desc")
    parser.add_argument("gamertag", help="Gamertag of clip owner")
    parser.add_argument("-k", "--apikey", help="Your Xbox API key", default=None)
    parser.add_argument("-t", "--title-contains",
                        help="Filter clips by game title containing this value")
    parser.add_argument("-a", "--include-automatic", action="store_true", default=False,
                        help="Download automatically created clips, default %(default)s")
    parser.add_argument("-l", "--limit", type=int,
                        help="Limit number to clips to this amount")
    parser.add_argument("-s", "--shares", type=int,
                        help="Filter out clips without at least these many shares")
    args = parser.parse_args()
    print "Getting %s clips %sfrom %s%s..." % (args.limit if args.limit else "all",
                                               "containing \"%s\" " % args.title_contains if args.title_contains else "",
                                               args.gamertag,
                                               " (including automatic clips)" if args.include_automatic else "")
    for game_clip in get_clips(args.apikey, args.gamertag, game_title_filter=args.title_contains,
                               automatic_clips=args.include_automatic, limit=args.limit):
        game_clip.download_clip()
    print "Done! All selected clips downloaded."