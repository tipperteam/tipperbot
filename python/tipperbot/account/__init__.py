from tipperbot.db import append,get, Tables
from tipperbot.utils.log import get_logger

USER_TABLE = Tables.USER.value
WALLET_TABLE = Tables.WALLET.value

logger = get_logger()

def is_user_registered(chat_id):
    users = get(Tables.USER)
    if users is None or chat_id not in users["user_id"].unique():
        return False
    return True

def add_user(chat_id):
    if not is_user_registered(chat_id):
        append(USER_TABLE,{"user_id":chat_id})
        append(WALLET_TABLE,{"user_id":chat_id,"amount":50,"reason":"Account created."})
        logger.info("Registered new user {}".format(chat_id))


def start(bot, update):
    chat_id = update.effective_chat.id
    if not is_user_registered(chat_id):
        bot.send_message(chat_id=chat_id, text="Benvenuto nuovo utente!")
        add_user(chat_id)
    else:
        bot.send_message(chat_id=chat_id, text="Bentornato!")

def credit(bot, update):
    chat_id = update.effective_chat.id
    if not is_user_registered(chat_id):

        bot.send_message(chat_id=chat_id, text="Non sei ancora registrato! Usa /start.")
    wallet = get(WALLET_TABLE)
    wallet = wallet[wallet["user_id"]==chat_id]
    bot.send_message(chat_id=chat_id, text="Diamanti: {}".format(int(wallet["amount"].sum())))

