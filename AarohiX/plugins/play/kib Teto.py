import asyncio
from pyrogram import Client, filters
from strings import get_string
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "**اختار ما تريد من القائمه 🧚‍♀️**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("المطور"),
        ("السورس")
    ],
    
    [
        ("اقتباس")
    ],
    [
        ("صور")
    ],
   
    [
        ("هيدرات")
    ],
    [
        ("صور شباب"),
        ("صور بنات")
    ],
    ],
    [
        ("تلاوات")
    ],
    [
        ("الشيخ نقشبندي"),
        ("متحركه")
        
    ],
 [
        
             ("اضـف البـوت لمجموعـتك ⚡")
        
    ],    
  
]

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اضـف البـوت لمجموعـتك ⚡") & filters.group)
async def down(client, message):
          m = await message.reply("**- بخدمتك حجي خفيت الازرار\n- اذا تريد تطلعها مرة ثانية اكتب الاوامر**", reply_markup= ReplyKeyboardRemove(selective=True))





