from telethon import TelegramClient, events, sync
import logging

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 1111111
api_hash = '222222222222222222222222222222222'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   level=logging.INFO)

logger = logging.getLogger(__name__)

client = TelegramClient('session_name', api_id, api_hash)
client.start()
@client.on(events.NewMessage(incoming=True))
async def handler(event):
  if event.voice != None:
   await client.delete_messages(event.chat_id, [event.id])
   await event.respond('__Сервис голосовых сообщений в данный момент недоступен.__')
  elif event.text.lower() ==  'привет':
   await client.send_file(event.chat_id, 'https://neprivet.ru/img/bad-good.png')
client.run_until_disconnected()
