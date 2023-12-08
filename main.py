import pyrogram , pyromod

from pyromod import listen
from keep import alive
from pyrogram import Client, filters, enums
p = dict(root='plugins')
from kvsqlite.sync import Client

db = Client("data.sqlite", 'fuck')
if not db.exists("admin_list"):
    db.set('admin_list', [1485149817,5566795307])
if not db.exists("sessions"):
    db.set('sessions', [])
if not db.exists("ban_list"):
    db.set("ban_list", [])
x = Client(name='lossclhos', api_id=15102119, api_hash='3dfdcee3e3bedad4738f81287268180f', bot_token='6967330928:AAFnMC_T3vu66--S_zgox6H0JAi8pRs6mfE', workers=20, plugins=p, parse_mode=enums.ParseMode.DEFAULT)
alive()
x.run()
