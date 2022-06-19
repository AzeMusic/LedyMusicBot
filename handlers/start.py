
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest
# aga tarafından düzenlendi. 


      
@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/84121d4d66583f22b508e.jpg",
                caption=(f"""✧═══════•❀•═══════✧
**Salam, {message.from_user.mention} Xoş gəldin!\n\n🍁 Mən {bot} Bot\n\n🎧 Səsli söhbətlərdə müsiqi yayınlamağı bacarıram.\n\n🧸 Mənim bir çox telegram özəlliklərimdə var.\n\n🖼️ Mənə media (yəni hər hansısa bir foto) göndərin mən onu telegraf sonuncusuna yukləyim.\n\n📚 Ayrı özəlliklər əmrlər bölməsində yerləşdirilib.\n\n✔️ Qrupda mənə admin hüquqları verməyi unutmayın.**     ✧═══════•❀•═══════✧
"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦅 ❰ Qrubuna Əlavə et ❱ 🦅", url=f"https://t.me/SSmusicLedy_bot?startgroup=start"
                    )
                ],
                [
                    InlineKeyboardButton( 
                       "🔊 Assistant", url="https://t.me/LedyMusicAssistant"
                    )
                ],
                [     
                    InlineKeyboardButton(
                        "🛠️ Dəstək", url="https://t.me/SOQrup"
                    ),
                    InlineKeyboardButton(
                        "📱 Rəsmi Kanal", url="https://t.me/ledyplaylist"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Əmrlər" , callback_data= "cbledy"
                    ),
                    InlineKeyboardButton(
                        "🍁 Ledy Bots", callback_data="ledybots"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["ledybots", f"ledybots@{BOT_USERNAME}"]))
async def bots(_, message: Message):
                await message.reply_photo(
                "https://telegra.ph/file/0daa006627da7af88b8fe.jpg",
                caption=(f"""✧═══════•❀•═══════✧
**Salam, 🦅 Ledy Botlar Aşağıdakılardır:\n\nLedy Botlar ən sürətli və güclü telegram botlarıdır.\n\nBu botlardan Rahat və təhlükəsiz istifadə edə bilərsiniz.**      ✧═══════•❀•═══════✧
"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Ledy Music Bot", url="https://t.me/SSmusicLedy_bot"
                    )
                ],
                [
                    InlineKeyboardButton( 
                       "Ledy Tagger Bot", url="https://t.me/LedyTaggerRobot"
                    )
                ],
                [     
                    InlineKeyboardButton(
                        "Ledy Robot", url="https://t.me/LedyRobot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Ledy App Scrapper Bot", url="https://t.me/ledyapiscrapperbot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑️ Bağla", callback_data="cls"
                    )
                ]
                
           ]
        ),
    )



@Client.on_message(command(["ledy", f"ledy@{BOT_USERNAME}", "help", f"help@{BOT_USERNAME}"]))
async def ledy(_, message: Message):
      await message.reply_text("\nBotun Aktiv işləməsi üçün aşağıdakı 3 yetkisi olmalıdır:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli söhbəti yönətmə yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🍁 User Özəlliyi", callback_data="herkes")  
                 ],[                
                     InlineKeyboardButton(
                         "🧑‍✈️ Admin Özəlliyi ", callback_data="owner")
                 ],[                     
                     InlineKeyboardButton(
                         "❄️ Tagger Özəlliyi", callback_data="tagger")
                 ],[
                     InlineKeyboardButton(
                         "🦅 LEDY BOTS", callback_data="ledybots")
                 ],[
                     InlineKeyboardButton(
                         "🏠 Ana menyu", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "🛠️ Dəstək", url="https://t.me/SOQrup")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbledy"))
async def cbledy(_, query: CallbackQuery):
    await query.edit_message_text("\nBotun Aktiv işləməsi üçün aşağıdakı 3 yetkisi olmalıdır:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli söhbəti yönətmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "🍁 User Özəlliyi 🍁", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "🧑‍✈️ Admin Özəlliyi 🧑‍✈️",callback_data ="owner")
        ],
        [
          InlineKeyboardButton(
            "❄️ Tagger Özəlliyi ❄️",callback_data ="tagger")
        ],
        [
          InlineKeyboardButton(
            "🦅 LEDY BOTS 🦅", callback_data="ledybots")
        ],
        [
          InlineKeyboardButton(
            "🏠 Ana Menyu", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "🛠️ Dəstək ", url="https://t.me/SOQrup")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün əmrlər menyusu:\n\n ▶️ /oynad <song name> - istədiyin musiqini dinlə\n  \n 🎵 /tap <song name> - istədiyin musiqini sürətli endir \n 🎥 /vtap istədiyin videonu sürətli endir\n 🔍 /axtar <query> - YouTube-dən video linkləri axtar\n 🎶 /lyric - Mahnı sözləri axtarar\n 🆔 /id - Sənin ID-in, Group ID-sı, Şəkil ID-si, Stickers ID-si, Media ID-si, File ID-si\n 📜 /info - Telegram User haqqında məlumat verər\n 💾 /git - <github_username> Github User Haqqında məlumat al\n ⚡ /ping - Bot pingi-ni göstərər\n ⏳ /speedtest - Bot'un Sürət Serverini göstərər\n ⏰ /uptime - Bot'un və Assistant'ın işləmə vaxtını göstərər\n 📼 /tts - Mətni səsə çevirər\n 💠 /alive - Bot'un canlı olub olmadığını göstərər.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🛠️ Dəstək", url="https://t.me/SOQrup")
                 ],
                 [
                     InlineKeyboardButton(
                         "« Geri", callback_data="cbledy")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("owner"))
async def owner(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu Botun Adminlər Üçün Əmrlər Menyusu:\n\n ⏸️ /dayandir - Yayınlanan musiqini dayandır\n ▶️ /davam - Musiqi yayınlamağa davam et\n 🔄 /otur - Musiqiyi növbəyə ötur\n ⏹ /son - Musiqi yayınlamağı sonlandır\n 🔼 /ver Kullancıya yetki ver\n 🔽 /al Yetki verilmiş Kullancının yetkisini al\n ❤️ /assistantqosul - Assistant Qrupa qoşular\n 🖤 /assistantcix - Assistant Qrupu tərk edər\n 👋 /ban - <yanıtla> Useri əbədilik ban edər və qrup həmin userdə görsənməz.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🛠️ Dəstək", url="https://t.me/SOQrup")                           
                 ],
                 [
                     InlineKeyboardButton(
                         "« Geri", callback_data="cbledy")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("tagger"))
async def tagger(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu özəllik hələ bot kodlarına yazılmayıb. Yaxın Zamanlarda Bu özəllik gerçəkləşəcək.\n\n /ledytag - Userləri Normal Şəkildə tağ edər.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🛠️ Dəstək", url="https://t.me/SOQrup")
                 ],
                 [
                     InlineKeyboardButton(
                         "« Geri", callback_data="cbledy")
                 ] 
             ]
         )
         )



@Client.on_callback_query(filters.regex("ledybots"))
async def ledybots(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>🦅 Ledy Botlar Aşağıdakılardır:\n\nLedy Botlar ən sürətli və güclü telegram botlarıdır.\n\nBu botlardan Rahat və təhlükəsiz istifadə edə bilərsiniz.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "Ledy Music Bot", url="https://t.me/SSmusicLedy_bot")
        ],
        [
          InlineKeyboardButton(
            "Ledy Tagger Bot", url="https://t.me/LedyTagRobot")
        ],
        [
          InlineKeyboardButton(
            "Ledy Robot", url="https://t.me/LedyRobot")
        ],
        [
          InlineKeyboardButton(
            "Ledy App Scrapper Bot", url="https://t.me/ledyapiscrapperbot")
        ],
        [
          InlineKeyboardButton(
            "🦅 Rəsmi Ledy Bots Kanalı", url="https://t.me/ledyplaylist")
        ],
        [
          InlineKeyboardButton(
            "🏠 Ana Menyu", callback_data="cbstart")
        ]
      ]
     ))



@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""✧═══════•❀•═══════✧     **Salam, {query.from_user.mention} Xoş gəldin!\n\n🍁 Mən {bot} Bot\n\n🎧 Səsli söhbətlərdə müsiqi yayınlamağı bacarıram.\n\n🧸 Mənim bir çox telegram özəlliklərimdə var.\n\n🖼️ Mənə media (yəni hər hansısa bir foto) göndərin mən onu telegraf sonuncusuna yukləyim.\n\n📚 Ayrı özəlliklər əmrlər bölməsində yerləşdirilib.\n\n✔️ Qrupda mənə admin hüquqları verməyi unutmayın.**    ✧═══════•❀•═══════✧""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦅 ❰ Qrubuna Əlavə et ❱ 🦅", url=f"https://t.me/SSmusicLedy_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton( 
                       "🔊 Assistant", url="https://t.me/LedyMusicAssistant"
                    )
                ],
                [     
                    InlineKeyboardButton(
                        "🛠️ Dəstək", url="https://t.me/SOQrup"
                    ),
                    InlineKeyboardButton(
                        "📱 Rəsmi Kanal", url="https://t.me/ledyplaylist"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📚 Əmrlər" , callback_data= "cbledy"
                    ),
                    InlineKeyboardButton(
                        "🍁 Ledy Bots", callback_data="ledybots"
                    )
                ]
                
           ]
        ),
    )




@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)

