import telebot
import json
from pathlib import Path
import random

API_TOKEN = "8221026755:AAFuLGyHe25g36_exPgcAgb8czWOvjU-k6I"
data_cannabis_people = Path('smoked_people.json')

bot = telebot.TeleBot(API_TOKEN)





@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Шмаль викурити /smoke, допомога /help, Статистика /statistics")
    print(message)

@bot.message_handler(commands=['smoke'])
def handler_smoke(message):
    gram = random.randint(1, 10)
    user_id = str(message.from_user.id)
    data = json.loads(data_cannabis_people.read_text())
    if user_id not in data:
        a = {
            "Name": message.from_user.username,
            "Gram": data.get("Gram", 0)
        }
        data[user_id] = (data.get(user_id, a))
    data[user_id]["Gram"] += gram

    data_cannabis_people.write_text(json.dumps(data))
    bot.reply_to(message, f"Щойно викурено {gram} грамів шмалі. Загалом — вже {data[user_id]["Gram"]} грамів!"
)
    
@bot.message_handler(commands=['statistics'])
def send_statistics(message):
    stasc = json.loads(data_cannabis_people.read_text())
    data = []
    for i in stasc:
        data.append({"Name":  stasc[i]["Name"], 'Gram': stasc[i]["Gram"]})
        # data['Name'] = stasc[i]["Name"]
        # data['Gram'] = stasc[i]["Gram"]
    bot.reply_to(message, data)

bot.infinity_polling()

