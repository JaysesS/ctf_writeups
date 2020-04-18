from telethon import TelegramClient, events, sync
import hashlib
import config

api_id = config.api_id
api_hash = config.api_hash

client = TelegramClient('new_task', api_id, api_hash)
client.start()
client.log_out()

@client.on(events.NewMessage(chats='Botcha'))
async def handler(event):
    if 'sha256' in event.text:
        get = str(event.text).split(':')[1].replace('`', '').replace(' ', '')
        ready = hashlib.sha256(get.encode()).hexdigest()
        await client.send_message('@spbctf_botcha_bot', ready)

client.add_event_handler(handler)

print('(Press Ctrl+C to stop this)')
client.run_until_disconnected()