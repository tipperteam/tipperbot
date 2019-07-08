from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from tipperbot.utils.log import get_logger
from tipperbot.db import append,get, Tables

SLIP_TABLE = Tables.CUR_SLIP

def addSlip(chat_id,match,event,quote):
    append(SLIP_TABLE,{"user_id":chat_id,"match":match,"event":event,"quote":quote})

def delSlipMatch(chat_id,match):
    append(SLIP_TABLE,{"user_id":chat_id,"match":match,"event":None,"quote":None})

def viewSlip(bot, update):
    try:
        chat_id = update.effective_chat.id
        slips = get(SLIP_TABLE)
        if slips is None:
            bot.send_message(chat_id=chat_id, text="Schedina vuota!")
        else:
            slips = slips.drop_duplicates(["user_id", "match"], keep="last").dropna()
            if chat_id not in slips["user_id"].unique():
                bot.send_message(chat_id=chat_id, text="Schedina vuota!")
            else:
                for slip_line in slips[slips["user_id"]==chat_id].to_dict('records'):
                    keyboard = [
                        [InlineKeyboardButton("Delete", callback_data="del#{}".format(slip_line["match"]))]
                    ]

                    reply_markup = InlineKeyboardMarkup(keyboard)

                    update.message.reply_text("{} {} {}".format(slip_line["match"], slip_line["event"], slip_line["quote"]),
                                              reply_markup=reply_markup)

    except Exception as e:
        get_logger().error(e)
