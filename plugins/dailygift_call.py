from pyrogram import Client as app, filters
from pyrogram.types import InlineKeyboardButton as btn, InlineKeyboardMarkup as mk
import time
from kvsqlite.sync import Client

db = Client("data.sqlite", 'fuck')
def check_user(user_id):
    users = db.get(f"user_{user_id}_gift")
    now = time.time()    
    WAIT_TIME = 24 * 60 * 60
    if  db.exists(f"user_{user_id}_gift"):
        last_time = users['time']
        elapsed_time = now - last_time
        if elapsed_time < WAIT_TIME:
            remaining_time = WAIT_TIME - elapsed_time
            return int(remaining_time)
        else:
            
            users['time'] = now
            db.set(f'user_{user_id}_gift', users)
            return None
    else:
        users = {}
        users['time'] = now
        db.set(f'user_{user_id}_gift', users)
        return None

@app.on_callback_query(filters.regex("^dailygift$"))
async def dailygiftt(app,query):
    import datetime
    keys = mk(
        [
            [btn(text='رجوع', callback_data='back_invite')]
        ]
    )
    x = check_user(query.from_user.id)
    
    if x !=None:
        duration = datetime.timedelta(seconds=x)
        now = datetime.datetime.now()
        target_datetime = now + duration
        date_str = target_datetime.strftime('%Y/%m/%d')
        await query.edit_message_text(f"عذرا صديقي، انت استلمت الهدية اليومية. تعال {date_str}.", reply_markup=keys)
        return
    else:
        info = db.get(f'user_{query.from_user.id}')
        info['coins'] = int(info['coins']) + 150
        db.set(f"user_{query.from_user.id}", info)
        await query.edit_message_text("- اخذت الهدية اليومية 150 أرصده!!\nهديتك الي بعدها باجر .", reply_markup=keys)
        return