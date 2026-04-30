from telethon import TelegramClient, events

# 🔐 Sening ma'lumotlaring
api_id = 20453287
api_hash = "9bce9c6acef9fe618f80e4c383cf35e5"

# 📁 session fayl (1 marta login qiladi)
client = TelegramClient("session", api_id, api_hash)

# 💬 Javob matni
REPLY_TEXT = "Assalomu alaykum 👋 bu Shohjahonning avto javob boti 😉"

@client.on(events.NewMessage)
async def handler(event):
    # o'zing yozgan xabarlarga ham javob bermasligi uchun:
    if event.out:
        return

    if event.message and event.raw_text:
        await event.reply(REPLY_TEXT)


client.start()
client.run_until_disconnected()