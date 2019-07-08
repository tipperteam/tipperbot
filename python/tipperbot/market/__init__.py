from tipperbot import account
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def buy(bot, update):
    chat_id = update.effective_chat.id
    account.users[chat_id] += 1


def spend(bot, update):
    chat_id = update.effective_chat.id
    account.users[chat_id] -= 1

def market(bot,update):
    keyboard = [[InlineKeyboardButton("Buy 1 Diamond", callback_data='buy'),
             InlineKeyboardButton("Spend 1 Diamond", callback_data='spend')],

            [InlineKeyboardButton("Controlla credito", callback_data='credit')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Cosa vuoi fare?', reply_markup=reply_markup)
