from datetime import datetime
from dateutil.relativedelta import relativedelta

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from vpn_bot import config
from vpn_bot.utils import MONTHS_RU


def get_monthly_analytics_keyboard(callback_prefix: str, current_date: datetime) -> InlineKeyboardMarkup:
    prev_date = current_date - relativedelta(months=1)
    next_date = current_date + relativedelta(months=1)

    keyboard = [
        [
            InlineKeyboardButton("<", callback_data=f"{callback_prefix}{prev_date.strftime(config.DATE_FORMAT)}"),
            
            InlineKeyboardButton(f"{MONTHS_RU[current_date.month - 1]} {current_date.year}", 
                                callback_data=" "),

            InlineKeyboardButton(">", callback_data=f"{callback_prefix}{next_date.strftime(config.DATE_FORMAT)}",),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

