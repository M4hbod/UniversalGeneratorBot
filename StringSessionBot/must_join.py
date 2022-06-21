import contextlib
from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = f"https://t.me/{MUST_JOIN}"
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            with contextlib.suppress(ChatWriteForbidden):
                await msg.reply(
                    f"برای استفاده از ربات باید توی [این کانال]({link}) جوین شید!",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("✨ جوین شدن ✨", url=link)]
                    ])
                )
                await msg.stop_propagation()
    except ChatAdminRequired:
        print(f"من توی این کانال ادمین نیستم: {MUST_JOIN}!")
