import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "26058816"))

API_HASH = getenv("API_HASH", "495a770d78d37f01d00031b4c1a0a6a4")

BOT_TOKEN = getenv("BOT_TOKEN", "")

Muntazer = getenv("muntazer", "Mvhmed")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2097152))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "20971520")
)

LOGGER_ID = int(getenv("LOGGER_ID", "6308685423"))

OWNER_ID = int(getenv("OWNER_ID", "6308685423"))

BOT_USERNAME = getenv("BOT_USERNAME" , "@Gor_Genabot")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/mvhaamed/gero11",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/mvhmed")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/mvhmed")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 20971520000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 209715200000))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
STATS_IMG_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/5ee75c8b81172a947c9eb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 2000**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
