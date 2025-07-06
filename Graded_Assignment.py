
# Graded Assignment (20): Create an AI agent that automates tasks of creating posts on social media platforms 
# like X.com (formerly Twitter), LinkedIn, Pinterest, Telegram (etc) using Python.


# AI Agent for Social Media Automation
#This AI agent automatically creates and posts motivational messages
# on Telegram social media platform using Python.
#Features:
# - Daily automated posts at 9:00 AM
# - Different messages for each day of the week
# - Asynchronous message handling
# - Error handling and logging


import schedule
import time
import asyncio
from datetime import datetime
from telegram import Bot

# for bot token and chat ID
TELEGRAM_TOKEN = '7956501403:AAGing1ll16Ccx_WmkzMaso2niF6MdiYoCg'
CHAT_ID = '5416115934'  # Can be group ID or user ID

bot = Bot(token=TELEGRAM_TOKEN)

messages = [
    "Monday Motivation: Start your week with a positive mindset! #MondayMotivation",
    "Tuesday Tips: Did you know that consistency is key to success? #TuesdayTips",
    "Wednesday Wisdom: Keep pushing forward, you're halfway through the week! #WednesdayWisdom",
    "Thursday Thoughts: Reflect on your progress and set new goals! #ThursdayThoughts",
    "Friday Fun: It's almost the weekend! What are your plans? #FridayFun",
    "Saturday Vibes: Take a break and enjoy some leisure time! #SaturdayVibes",
    "Sunday Reflections: Prepare for the week ahead and set your intentions! #SundayReflections"
]

async def post_daily_message():
    day_index = datetime.now().weekday()  # 0 = Monday, 6 = Sunday
    message = messages[day_index]
    try:
        print(f"Attempting to send message to chat ID: {CHAT_ID}")
        result = await bot.send_message(chat_id=CHAT_ID, text=message)
        print(f"Successfully sent message: {message}")
        print(f"Message ID: {result.message_id}")
    except Exception as e:
        print(f"Error sending message: {e}")
        print(f"Error type: {type(e).__name__}")

def run_post_daily_message():
    """Wrapper function to run the async function"""
    try:
        asyncio.run(post_daily_message())
    except Exception as e:
        print(f"Error in wrapper: {e}")

# Schedule the post every day at 09:00 AM
schedule.every().day.at("09:00").do(run_post_daily_message)

if __name__ == "__main__":
    print("�� Automated Telegram Bot Started!")
    print(f"📱 Bot: @InspireNowAgentBot")
    print(f"👤 Chat ID: {CHAT_ID}")
    print("⏰ Messages scheduled daily at 9:00 AM")
    print("🔄 Bot is running...")
    
    while True:
        schedule.run_pending()
        time.sleep(1)