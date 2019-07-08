users = {

}

def start(bot, update):
    chat_id = update.effective_chat.id
    if not chat_id in users:
        bot.send_message(chat_id=chat_id, text="Benvenuto nuovo utente!")
        users[chat_id] = 0
    else:
        bot.send_message(chat_id=chat_id, text="Bentornato!")

def credit(bot, update):
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id, text="Diamanti: {}".format(
        users[chat_id]) if chat_id in users else "Non sei ancora registrato! Usa /start.")

