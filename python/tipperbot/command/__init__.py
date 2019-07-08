from tipperbot.account import credit
from tipperbot.market import buy, spend
from tipperbot.slip import addSlip, delSlipMatch

def handler(bot, update):
    query = update.callback_query
    chat_id = update.effective_chat.id

    if query.data == "credit":
        credit(bot, update)
    elif query.data == "buy":
        buy(bot, update)
    elif query.data == "spend":
        spend(bot, update)
    elif query.data[:3] == "bet":
        match, event, quote = query.data.split("#")[1:]
        query.edit_message_text(text="Hai puntato sull'evento {} con quota {}".format(*query.data.split("#")[2:]))
        addSlip(chat_id,match,event,quote)
    elif query.data[:3] == "del":
        delSlipMatch(chat_id,query.data.split("#")[1])
        query.edit_message_text(text="Evento eliminato.")
    else:
        query.edit_message_text(text=query.data)
