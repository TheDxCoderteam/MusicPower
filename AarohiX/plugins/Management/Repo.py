from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AarohiX import app as bot
import requests
from config import BOT_USERNAME
from AarohiX.utils.errors import capture_err

start_txt = """**
➤ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴡᴏʀʟᴅ ᥫᩣ
 
 ⦿ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ɴ ᴠᴘs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ !
 
 ⦿ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ !
 
 ⦿ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ !
 
 ⦿ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴅᴍ ᴍᴇ !
**"""

@bot.on_message(filters.command(["repo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("⦿ ᴀᴅᴅ ᴍᴇ ⦿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/NeoUpdatess"),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/dx_Coder"),
        ],
        [
          InlineKeyboardButton("ᴠ1 ᴋɪᴅ ᴍᴜsɪᴄ", url=f"https://t.me/KidMusicBot?startgroup=true"),
          InlineKeyboardButton("︎ᴠ2 ʙᴀʙʏ ᴍᴜsɪᴄ", url=f"https://t.me/Baby_Music_Robot?startgroup=true"),
        ],
        [
          InlineKeyboardButton("ᴍᴀñᴀɢᴇᴍᴇɴᴛ", url=f"https://t.me/Kid_Management_Bot"),
          InlineKeyboardButton("ᴄʜᴀᴛ ʙᴏᴛ", url=f"https://t.me/Baby_ChatsBot"),
        ],
        [
          InlineKeyboardButton("sᴛʀɪɴɢ ʙᴏᴛ", url=f"https://t.me/The_StringRobot"),
          InlineKeyboardButton("ᴅᴘᴢ sᴛᴏʀᴇ", url=f"https://t.me/The_F2F_Dpz"),
        ],
        [
          InlineKeyboardButton("sʜʏᴀʀɪ ", url="https://t.me/The_F2F_Shayri"),
          InlineKeyboardButton("ᴀʟᴏɴᴇ ɢʀᴏᴜᴘ", url=f"https://t.me/FRIENDS2FAMILY00"),
        ],
        [
          InlineKeyboardButton("ʟᴀᴛᴇ ɴɪɢʜᴛ︎", url=f"https://t.me/NeoMusicSupport"),
          InlineKeyboardButton("ᴅᴜɴɪʏᴀ", url=f"https://t.me/F2F_STYLISH_NAME"),
        ],
        [
          InlineKeyboardButton("ᴅɪʟ ғᴇᴇʟɪɴɢs", url=f"https://t.me/The_F2F_Networks"),
          InlineKeyboardButton("ʟᴏᴠᴇ ғᴇᴇʟɪɴɢs", url=f"https://t.me/ll_SpIcY_ll"),
        ],
        [
          InlineKeyboardButton("ᴅɪʟ sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/The_Cute_Boy_Op"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/20b4818b485658abaa47c.jpg",
        caption=start_txt,
        reply_markup=reply_markup,
    )



#-------------------------------------------------------#


@bot.on_message(filters.command("repo", prefixes="@"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/stkeditz/AAROHIxMUSICv2/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[ʀᴇᴘᴏ](https://t.me/princymusicbot?startgroup=true/) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/NeoUpdatess)
| ᴄᴏɴᴛʀɪʙᴜᴛᴏʀs |
----------------
{list_of_users}"""
        await bot.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await bot.send_message(message.chat.id, text="Failed to fetch contributors.")

