from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 شروع ساخت سشن 🔥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 صفحه اصلی 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("آموزش استفاده ❔", callback_data="help"),
            InlineKeyboardButton("🎪 درباره 🎪", callback_data="about")
        ],
    ]

    START = """
✨ سلام {} به ربات {} خوش اومدی.

💭 کار من ساختن استرینگ سشن پایروگرام و تلتونه.
🔖 از دکمه های زیر استفاده کن.
    """

    HELP = """
✨ **دستورات** ✨

/about - درباره ربات
/help - این پیام
/start - استارت ربات
/generate - ساخت سشن
/cancel - لغو عملیات
/restart - لغو عملیات
"""

    ABOUT = """
**درباره ربات** 

رباتی برای ساختن استرینگ سشن پایروگرام و تلتون

فریمورک : [Pyrogram](https://docs.pyrogram.org)

زبان : [Python](https://www.python.org)

سازنده: @M4hbod
"""
