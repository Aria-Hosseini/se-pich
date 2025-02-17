import telebot
import openai

bot = telebot.TeleBot("Your Bot API token")

@bot.message_handler(content_types=['new_chat_members'])
def newMember (message):
    for member in message.new_chat_members:
        welcomeText= f'کاربر {message.from_user.first_name}خوش اومدی به گپ ما'
        bot.send_message(message.chat.id, text=welcomeText)
# تشخیص ادمین ها
def check_admins (chat_id , user_id):
    admins = bot.get_chat_administrators(chat_id)
    for  admin in admins:
        if admin.user.id == user_id:
            return  True
    return  False

# پین کردن پیام توسط ادمین 
@bot.message_handler( func= lambda message: message.text and message.text.strip().lower() in ["pin", "پین"] )
def pin_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if check_admins(chat_id, user_id):
        if message.reply_to_message:
            bot.pin_chat_message(chat_id , message.reply_to_message.message_id)
            bot.reply_to(message.reply_to_message , "پیام پین شد")
        else :
            bot.reply_to (message , "لطفا روی پیامی که میخواهید پین کنید ریپلای بزنید")
    else:
        bot.send_message(message.chat.id , "⚠️ فقط ادمین ها میتونن پیام ها رو پین کنن")

#  برداشتن پین توسط ادمین
@bot.message_handler( func= lambda message: message.text and message.text.strip().lower() in ["unpin", "آن پین","آنپین","un pin"] )
def unpin_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    if check_admins(chat_id, user_id):
        if message.reply_to_message:
            bot.unpin_chat_message(chat_id , message.reply_to_message.message_id)
            bot.reply_to(message.reply_to_message , "پیام آن پین شد")
        else :
            bot.reply_to (message , "لطفا روی پیامی که میخواهید از پین بردارید ریپلای بزنید")
    else:
        bot.send_message(message.chat.id , "⚠️ فقط ادمین ها میتونن پیام ها رو از پین بردارن")

#    بن کردن اعضا
@bot.message_handler(func= lambda message: message.text and message.text.strip().lower() in ["ban","بن","سیکتیر","بیرون","سیکش بزن","سیک","سیک تیر"])
def ban_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if check_admins(chat_id, user_id):  
        if message.reply_to_message:  
            banned_user_id = message.reply_to_message.from_user.id  
            bot.ban_chat_member(chat_id, banned_user_id)  
            bot.reply_to(message, f'🚫 کاربر {message.reply_to_message.from_user.first_name} سیکش زده شد!')
            
        else:
            bot.reply_to(message, "لطفاً روی پیام فردی که می‌خواهید بن کنید ریپلای بزنید!")
    else:
        bot.send_message(chat_id, "⚠️ فقط ادمین‌ها می‌توانند اعضا را بن کنند.")

# سکوت اعضا
@bot.message_handler(func= lambda message : message.text and message.text.strip().lower() in ["خفه" , "ساکت" , "mute","سکوت"])
def mute_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if check_admins(chat_id , user_id):
        if message.reply_to_message:
            muted_user_id = message.reply_to_message.from_user.id  

            bot.restrict_chat_member(
                chat_id,
                muted_user_id,
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False
            )
            bot.reply_to(message, f'🤐 کاربر {message.reply_to_message.from_user.first_name} ساکت شد!')
        else:
            bot.reply_to(message , "لطفاً روی پیام فردی که می‌خواهید ساکت کنید ریپلای بزنید!")
    else:
        bot.send_message(message.chat.id , "⚠️ فقط ادمین ها میتونن اعضا رو ساکت کنن")

# برداشتن سکوت اعضا
@bot.message_handler(func= lambda message : message.text and message.text.strip().lower() in ["آزاد" , "ازاد", "unmute"])
def unmute_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if check_admins(chat_id , user_id):
        if message.reply_to_message:
            unmuted_user_id = message.reply_to_message.from_user.id  

            bot.restrict_chat_member(
                chat_id,
                unmuted_user_id,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True
            )
            bot.reply_to(message, f'🔊 کاربر {message.reply_to_message.from_user.first_name} از سکوت درومد!')
        else:
            bot.reply_to(message , "لطفاً روی پیام فردی که می‌خواهید از سکوت خارج کنید ریپلای بزنید!")
    else:
        bot.send_message(message.chat.id , "⚠️ فقط ادمین ها میتونن اعضا رو از سکوت خارج کنن")

# حذف پیام 
@bot.message_handler(func= lambda message : message.text and message.text.strip().lower() in  ["del" , "حذف" , "پاک"])
def delete_message(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if check_admins(chat_id , user_id):
        if message.reply_to_message:
            bot.delete_message(chat_id, message.reply_to_message.message_id)
            bot.reply_to(message, "🗑 پیام حذف شد!")
        else:
            bot.reply_to(message , "لطفا روی پیامی که میخواهید حذف کنید ریپلای بزنید")
    else:
        bot.send_message(message.chat.id , "فقط ادمین ها میتوانند از دستور حذف استفاده کنند")

# قفل کردن گروه
@bot.message_handler(commands=["lock"])
def lock_group(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if check_admins(chat_id , user_id):
        bot.set_chat_permissions(chat_id, telebot.types.ChatPermissions(can_send_messages=False))
        bot.send_message(chat_id, "🔒 گروه قفل شد! فقط ادمین‌ها میتونن پیام ارسال کنند.")
    else:
        bot.send_message(message.chat.id , "فقط ادمین ها میتونن گروه رو قفل کنن")
# باز کردن قفل گروه
@bot.message_handler(commands=["unlock"])
def unlock_group(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if check_admins(chat_id , user_id):
        bot.set_chat_permissions(chat_id, telebot.types.ChatPermissions(can_send_messages=True))
        bot.send_message(message.chat.id , "قفل گروه باز شد🔓")
    else:
        bot.send_message(message.chat.id , "فقط ادمین ها میتونن قفل گروه رو باز کنن")

# تعامل با ربات
@bot.message_handler(func=lambda message: "سه پیچ" in message.text.lower())
def reply_to_se_pich(message):
    bot.reply_to(message , "جونم")


bot.polling()
