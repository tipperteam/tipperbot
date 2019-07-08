from tipperbot.account import credit
from tipperbot.market import buy, spend
from tipperbot import slip

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
        if chat_id not in slip.slips:
            slip.slips[chat_id] = {}
        slip.slips[chat_id][match] = {
            "event": event,
            "quote": quote
        }
    elif query.data[:3] == "del":
        del slip.slips[chat_id][query.data.split("#")[1]]
        query.edit_message_text(text="Evento eliminato.")
    else:
        query.edit_message_text(text=query.data)
