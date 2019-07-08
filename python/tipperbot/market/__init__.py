from tipperbot.account import user_credit
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from tipperbot.db import append,get, Tables, persist_tables

WALLET_TABLE = Tables.WALLET.value

def buy(bot, update):
    chat_id = update.effective_chat.id
    append(WALLET_TABLE,{"user_id":chat_id,"amount":1,"reason":"Bought on market."})


def spend(bot, update):
    chat_id = update.effective_chat.id
    if user_credit(chat_id)>0:
        append(WALLET_TABLE,{"user_id":chat_id,"amount":-1,"reason":"Spent on market."})
    else:
        bot.send_message(chat_id=chat_id, text="Non hai abbastanza fondi!")

def market(bot,update):
    chat_id = update.effective_chat.id
    keyboard = [[InlineKeyboardButton("Buy 1 Diamond", callback_data='buy')],

            [InlineKeyboardButton("Controlla credito", callback_data='credit')]]

    if user_credit(chat_id)>0:
        keyboard[0].append(InlineKeyboardButton("Spend 1 Diamond", callback_data='spend'))

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Cosa vuoi fare?', reply_markup=reply_markup)
