import xmltodict, json
import requests
from tipperbot.utils.log import get_logger

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_odds():
    ## TODO: Change this
    URL = "http://xml.cdn.betclic.com/odds_en.xml"

    response = requests.get(URL)
    data = response.content.decode()
    o = xmltodict.parse(data)
    data_json = json.loads(json.dumps(o))  # '{"e": {"a": ["text", "text"]}}'

    m_data = {}

    for sport in data_json["sports"]["sport"]:
        for event in sport["event"]:
            event_name = event["@name"]
            m_data[event_name] = {}
            matches = event["match"]
            if type(matches) == dict:
                matches = [matches]
            for match in matches:
                try:
                    match_name = match["@name"],
                    match = {
                        "start_date": match["@start_date"],
                        "bets": {
                            bet["@name"]: {
                                choice["@name"].replace("%", "").replace("Draw", "X"): choice["@odd"] for choice in
                                bet["choice"]
                            } for bet in match["bets"]["bet"]
                        }
                    }
                    m_data[event_name][match_name] = match
                except Exception as e:
                    pass
        break
    return m_data

odds_df = get_odds()

def odds(bot, update):
    try:
        chat_id = update.effective_chat.id

        for event, matches in odds_df.items():
            bot.send_message(chat_id=chat_id, text=event)
            for match, info in matches.items():
                keyboard = [
                    [InlineKeyboardButton("{} ({})".format(c_n, c_v),
                                          callback_data="bet#{}#{}#{}".format(match, c_n, c_v)) for c_n, c_v in
                     choices.items()]
                    for bet, choices in info["bets"].items()
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)

                update.message.reply_text("{} {}".format(info["start_date"], match), reply_markup=reply_markup)
            break
    except Exception as e:
        get_logger().error(e)