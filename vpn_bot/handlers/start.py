from telegram import Update
from telegram.ext import ContextTypes

from vpn_bot import handlers
from vpn_bot import exceptions


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        raise exceptions.UpdateHaventMessage("Can't get message from update in start command handler")
    
    await update.message.reply_text("Вы попали в VPN бот!")

    is_admin = True
    if is_admin:
        await handlers.monthly_analytics(update, context)



