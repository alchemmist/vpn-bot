import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")

DATE_FORMAT = "%m.%Y"

# Callback patterns
MONTHLY_ANALYTICS_CALLBACK_PATTERN = "monthly_analytics_"
PAYMENT_CALLBACK_PATTERN = "monthly_analytics_"

