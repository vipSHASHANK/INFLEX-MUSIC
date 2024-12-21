from pyrogram.types import InlineKeyboardButton

import config
from SHUKLAMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="▪️ʜᴇʟᴘ▪️", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="▪️sᴇᴛ▪️", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="▪️sᴜᴘᴘᴏʀᴛ▪️", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="📺 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 📺",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="⌨️ ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅ ⌨️", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="▪️ᴜᴘᴅᴀᴛᴇs▪️", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="▪️sᴜᴘᴘᴏʀᴛ▪️", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="▪️ᴏᴡɴᴇʀ▪️", user_id=config.OWNER_ID),
        ],
    ]
    return buttons