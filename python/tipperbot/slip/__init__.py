slips = {

}

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from tipperbot.utils.log import get_logger

def viewSlip(bot, update):
    try:
        chat_id = update.effective_chat.id

        if chat_id not in slips:
            bot.send_message(chat_id=chat_id, text="Non hai creato nessuna schedina!")
        else:
            for match, info in slips[chat_id].items():
                keyboard = [
                    [InlineKeyboardButton("Delete", callback_data="del#{}".format(match))]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)

                update.message.reply_text("{} {} {}".format(match, info["event"], info["quote"]),
                                          reply_markup=reply_markup)

    except Exception as e:
        get_logger().error(e)
