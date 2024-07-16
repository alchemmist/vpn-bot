import logging
from datetime import datetime, date

from prettytable import PrettyTable

from telegram.constants import ParseMode
from telegram import Update
from telegram.ext import ContextTypes

from vpn_bot import exeptions, config
from vpn_bot.handlers.keyboards import get_monthly_analytics_keyboard


async def monthly_analytics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        logging.error("Can't get message from update")
        raise exeptions.UpdateHaventMessageError()

    today = datetime.today()
    data = get_analytics_data(today)
    analytics_table = create_analytics_table(data)
    
    await update.message.reply_text(
        analytics_table, 
        reply_markup=get_monthly_analytics_keyboard(config.MONTHLY_ANALYTICS_CALLBACK_PATTERN, today),
        parse_mode=ParseMode.MARKDOWN_V2
    )


async def monthly_analytics_button(update: Update, _: ContextTypes.DEFAULT_TYPE):
    if not (query := update.callback_query):
        logging.error("Can't get query from update")
        raise exeptions.UpdateHaventQueryError()

    new_date = _get_datetime_by_callback(str(query.data))
    data = get_analytics_data(new_date)
    analytics_table = create_analytics_table(data)
    await query.edit_message_text(
        analytics_table, 
        reply_markup=get_monthly_analytics_keyboard(config.MONTHLY_ANALYTICS_CALLBACK_PATTERN, new_date),
        parse_mode=ParseMode.MARKDOWN_V2
    )


def get_analytics_data(date: datetime) -> list[list]:
    # TODO: rewrite to work with SQLite DB
    data = {
        "07.2024": [
            ["32", "@alex", "✓"],
            ["33", "@vova", "✓"],
            ["33", "@misha", "✗"],
        ],
        "08.2024": [
            ["32", "@alex", "✗"],
            ["33", "@vova", "✗"],
            ["33", "@misha", "✗"],
            ["34", "@anton", "✓"],
        ]
    }
    
    if date.strftime(config.DATE_FORMAT) in data:
        return data[date.strftime(config.DATE_FORMAT)]
    else:
        return []



def create_analytics_table(data: list[list]) -> str:
    users_table = PrettyTable()

    users_table.field_names = ["Byte", "Username", "Payed"]

    for user in data:
        users_table.add_row(user)

    return "```\n{}```".format(users_table.get_string())


def _get_datetime_by_callback(collback: str) -> datetime:
    month, year = map(int, collback.split("_")[-1].split("."))
    return datetime(year, month, 1)

