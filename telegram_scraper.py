from dotenv import load_dotenv
from telethon import TelegramClient
from datetime import datetime, timezone
import os
import asyncio
import pandas as pd

os.environ.clear()
load_dotenv(override=True)


api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")



channels = ['AJPalestine', 'MisbarFC', 'tibianps']

#Test Two month
# Date range: 1/5/2035 to 30/6/2025
#start_date = datetime(2025, 5, 1, 0, 0, 0, tzinfo=timezone.utc)
#end_date = datetime(2025, 6, 30, 23, 59, 59, tzinfo=timezone.utc)

#Test all remain month in 2025
# Date range: 1/1/2025 to 30/4/2025
#start_date = datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
#end_date = datetime(2025, 4, 30, 23, 59, 59, tzinfo=timezone.utc)

# Date range: All of 2024
#start_date = datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
#end_date = datetime(2024, 12, 31, 23, 59, 59, tzinfo=timezone.utc)

async def main():
    client = TelegramClient("my_session", api_id, api_hash)
    await client.start()
    print("Logged in successfully!\n")
    #await client.send_message("me","random message 20 Jan 19:30")
    all_messages = []

    for channel in channels:
        print(f"Fetching messages from: {channel}")
        
        try:
            async for message in client.iter_messages(channel, offset_date=start_date, reverse=True):
                if message.date < start_date:
                    break
              
                if message.text and start_date <= message.date <= end_date:
                    all_messages.append({
                        "date": message.date.strftime('%Y-%m-%d %H:%M:%S'),
                        "channel": channel,
                        "text": message.text
                    })
                    print(f"[{message.date.strftime('%Y-%m-%d %H:%M')}] {channel}: {message.text[:200]}")
        except Exception as e:
            print(f"Error fetching from {channel}: {e}")

    await client.disconnect()
    if all_messages:
        df = pd.DataFrame(all_messages, columns=["date", "channel", "text"])
        df.to_csv("telegram_news_2025.csv", index=False, encoding='utf-8-sig')
        print(f"\nDone! Saved {len(df)} messages to telegram_news_2025.csv")
    else:
        print("No messages found in the specified date range.")    

asyncio.run(main())