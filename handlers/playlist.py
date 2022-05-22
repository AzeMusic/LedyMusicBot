from config import BOT_USERNAME

from pyrogram import Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from callsmusic.queues import QUEUE, get_queue
from callsmusic.callsmusic import command, other_filters


keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🗑 Bağla", callback_data="set_close")]]
)


@Client.on_message(command(["playlist", f"playlist@{BOT_USERNAME}", "novbe", f"novbe@{BOT_USERNAME}"]) & other_filters)
@check_blacklist()
async def playlist(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await m.reply(
                f"✨ **Hal Hazırda yayımlanır**`:`\n\n"
                f"➣ [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}`",
                reply_markup=keyboard, disable_web_page_preview=True)
        else:
            QUE = f"✨ **Hal Hazırda yayımlanır**`:`\n\n" \
                  f"➣ [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}` \n\n" \
                  f"**📖 Növbədə olan mahnı siyahısı**`:`\n"
            l = len(chat_queue)
            for x in range(1, l):
                han = chat_queue[x][0]
                hok = chat_queue[x][2]
                hap = chat_queue[x][3]
                QUE = QUE + "\n" + f"`#{x}` - [{han}]({hok}) | `{hap}`"
            await m.reply(QUE, reply_markup=keyboard, disable_web_page_preview=True)
    else:
        await m.reply("❌ **Hal hazırda heç nə yayımlanmır.**")
