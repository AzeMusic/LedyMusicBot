from asyncio.queues import QueueEmpty
from cache.admins import admins
from asyncio import sleep
from pyrogram import Client
from pyrogram.types import Message
from ledymusic import ledymusic
from pyrogram import filters

from config import BOT_NAME as BN
from helpers.filters import command
from helpers.decorators import errors, authorized_users_only
from ledymusic import ledymusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


ACTV_CALLS = []


@Client.on_message(command(["dayandir", f"dayandir@{BOT_USERNAME}", "pause"]))
@errors
@authorized_users_only
async def dayandir(_, message: Message):
    await ledymusic.pytgcalls.pause_stream(message.chat.id)
    a = await message.reply_text("▶️ **Müsiqi dayandırıldı!**\n\n• Müsiqini yayınlamağa davam etmək üçün **Əmr » davam**")
    await sleep(3)
    await a.delete()



@Client.on_message(command(["davam", f"davam@{BOT_USERNAME}", "resume"]))
@errors
@authorized_users_only
async def davam(_, message: Message):
    await ledymusic.pytgcalls.resume_stream(message.chat.id)
    a = await message.reply_text("⏸ **Müsiqi yayınlamağa davam edir!**\n\n• Müsiqi yayınlamağı dayandırmaq üçün **əmr » duyandir**")
    await sleep(3)
    await a.delete()
    


@Client.on_message(command(["son", f"son@{BOT_USERNAME}", "end"]))
@errors
@authorized_users_only
async def stop(_, message: Message):
    chat_id = message.chat.id 
    for x in ledymusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("🙄 **İndi müsiqi yayinlanmır**")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass
        await ledymusic.pytgcalls.leave_group_call(chat_id)
        await _.send_message(
            message.chat.id,
            "✅ **Müsiqi sonlandırıldı !**\n\n• **Assistant səsli söhbətdən ayrıldı.**"
        )
    
@Client.on_message(command(["otur", f"@otur{BOT_USERNAME}", "skip"]))
@errors
@authorized_users_only
async def otur(_, message: Message):
    global que
    chat_id = message.chat.id
    for x in ledymusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        a = await message.reply_text("Növbədə Heç birşey yoxdur!")
        await sleep(3)
        await a.delete()
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await ledymusic.pytgcalls.leave_group_call(chat_id)
        else:
            await ledymusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        ledymusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
            
        a = await message.reply_text("**Musiqi Növbəyə Ötutruldu.**")
        await sleep(3)
        await a.delete()

# Yetki Vermek için (ver) Yetki almak için (al) komutlarını ekledim.
# Gayet güzel çalışıyor. @Tenha055 Tarafından Eklenmiştir. 
@Client.on_message(command(["ver", f"ver@{BOT_USERNAME}]))
@authorized_users_only
async def authenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("Kullancıya Yetki Vermək üçün yanıtlayın!")
        return
    if message.reply_to_message.from_user.id not in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.append(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullancı yetkili.")
    else:
        await message.reply("✔ Kullancı Artıq Yetkili!")


@Client.on_message(command(["al", f"al@{BOT_USERNAME}]))
@authorized_users_only
async def deautenticate(client, message):
    global admins
    if not message.reply_to_message:
        await message.reply("✅ Kullancıyı yetkisizləşdirmək üçün yanıtlayın!")
        return
    if message.reply_to_message.from_user.id in admins[message.chat.id]:
        new_admins = admins[message.chat.id]
        new_admins.remove(message.reply_to_message.from_user.id)
        admins[message.chat.id] = new_admins
        await message.reply("kullanıcı yetkisiz")
    else:
        await message.reply("✅ Kullancının yetkisi alındı!")


# Sesli sohbet için 0-200 arası yeni komut eklenmiş oldu. 
@Client.on_message(command(["ses" f"ses@{BOT_USERNAME}]))
@authorized_users_only
async def change_ses(client, message):
    range = message.command[1]
    chat_id = message.chat.id
    try:
       ledymusic.pytgcalls.change_volume_call(chat_id, volume=int(range))
       await message.reply(f"✅ **ayarlandı:** ```{range}%```")
    except Exception as e:
       await message.reply(f"**xəta:** {e}")

@Client.on_message(command(["yenile", f"yenile@{BOT_USERNAME}", "reload"]))
@errors
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await client.send_message(
        message.chat.id,
        "✅ **Bot yenidən başladıldı!**\n✅ **Admin Siyahısı yeniləndi!**"
    )
