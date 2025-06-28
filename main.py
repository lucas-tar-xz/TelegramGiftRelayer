import asyncio
from telethon import TelegramClient, events, types

try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

api_id = pass # Your Api Id from my.telegram.org
api_hash = "" # Your Api Hash from my.telegram.org

client = TelegramClient('GiftRelayer', api_id, api_hash)

@client.on(events.Raw)
async def handler(event):
    event = event.update
    if isinstance(event, types.UpdateNewMessage):
        if isinstance(event.message, types.MessageService) and isinstance(event.message.action, types.MessageActionStarGiftUnique) and isinstance(event.message.action.gift, types.StarGiftUnique):
            gift = event.message.action.gift
            print("Получен новый подарок:")
            print(f"От кого: {event.message.peer_id.user_id}")
            print(f"Название: {gift.title}")
            print(f"Номер: {gift.num}")
            print(f"Модель: {gift.attributes[0].name}")
            print("\n\n\n")


async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
