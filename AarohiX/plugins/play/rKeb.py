import asyncio
from pyrogram import Client, filters
from strings import get_string
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



REPLY_MESSAGE = "<b>- اهلا بك عزيزي اليك قائمه الاوامر</b>"




REPLY_MESSAGE_BUTTONS = [

          [

             ("‹ سورس ›"),

             ("‹ المطور ›")
          ],
          [

             ("‹ غنيلي ›"),

             ("‹ شعر ›")
          ],

          [

             ("‹ صور ›"),

             ("‹ انمي ›")

          ],

          [

             ("‹ متحركة ›"),

             ("‹ اقتباسات ›")

          ],

          [

             ("‹ افتارات شباب ›"),

             ("‹ افتار بنات ›")

          ],

          [

             ("‹ هيدرات ›"),

             ("‹ قران ›")

          ],
    
          [

            ("‹ جداريات ›"),

            ("‹ لوكيت ›")
              
          ],
          
          [
            ("‹ افلام ›")             
          ],
          
          [
             ("‹ اخفاء الكيبورد ›")

          ]

]




  

@app.on_message(filters.regex("/start") & filters.private)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("‹ اخفاء الكيبورد ›") & filters.private)
async def down(client, message):
          m = await message.reply("<b>- تم اغلاق الكيبورد.</b>", reply_markup= ReplyKeyboardRemove(selective=True))
