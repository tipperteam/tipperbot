from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from tipperbot.utils.env import get_property
from tipperbot.account import start, credit
from tipperbot.market import market
from tipperbot.odds import odds
from tipperbot.slip import viewSlip
from tipperbot.command import handler

if __name__=="__main__":
    updater = Updater(get_property("BOT_TOKEN"))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('credit',credit))
    dp.add_handler(CommandHandler('market',market))
    dp.add_handler(CommandHandler('odds',odds))
    dp.add_handler(CommandHandler('viewSlip',viewSlip))
    dp.add_handler(CallbackQueryHandler(handler))
    updater.start_polling()
    updater.idle()
