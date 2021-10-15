from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, ""]
        API_HASH = [str, "abcdedf......"]
        API_ID = [int, 1234567]
        BOT_TOKEN = [str, "bot:token here"]
        COMPLETED_STR = [str, "■"]
        REMAINING_STR = [str, "□"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, True]
        AUTH_USERS = [list,[1664850827]]
        OWNER_ID = [int, 1664850827]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,""]
        FORCEJOIN_ID = [int, 0]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/showthumb"
        CLR_THUMB = "/delthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
