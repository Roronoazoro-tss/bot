class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6861906489"
    sudo_users = ["6861906489"]
    GROUP_ID = "-1002337505439"
    TOKEN = "7750984175:AAHM4dviLfW500P37q1GfUkSP8X6VCCK8W8"
    mongo_url = "mongodb+srv://naruto:hinatababy@cluster0.rqyiyzx.mongodb.net/"
    PHOTO_URL = ["https://telegra.ph/file/7e5398823512d307128a3.jpg", "https://telegra.ph/file/c45dcb207d81e97cb4f6a.jpg", "https://telegra.ph/file/0bc6d65878e8300fbf0f8.jpg", "https://telegra.ph/file/0afb45203ff162ee7227b.jpg"]
    SUPPORT_CHAT = "lustsupport"
    UPDATE_CHAT = "lustxUpdate"
    BOT_USERNAME = "lustXcatcherrobot"
    CHARA_CHANNEL_ID = "-1002023474262"
    api_id = "20457610"
    api_hash = "b7de0dfecd19375d3f84dbedaeb92537"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
