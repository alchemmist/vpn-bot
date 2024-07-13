from vpn_bot import config, handlers
from vpn_bot.data import db

import logging
from telegram.ext import ApplicationBuilder, CommandHandler


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    db.global_init()

    app = ApplicationBuilder().token(config.TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", handlers.start))
    app.run_polling()


if __name__ == "__main__":
    try:
        main()
    except Exception:
        import traceback

        logging.warning(traceback.format_exc())

