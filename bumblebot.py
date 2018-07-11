import telebot
import random
from telebot import types
from secret_vars import TOKEN

bot = telebot.TeleBot(TOKEN)
correct_response_ratio = .8 #will respond correctly 80% of the time

f = open("bumblebee.barks")
barks = [line.strip() for line in f.readlines()]
f.close()

commands = {
        "sit": lambda : "bumblebee sits",
        "speak": lambda : random.choice(barks),
        "good girl": lambda : "bumblebee wags her tail excitedly and runs around in a little circle",
        "kill": lambda : kill 
        }

def kill():
    return "bumblebee enters a blood frenzy. her eyes turn red and roll back into her head. she'll be back in an hour"

@bot.message_handler(func=lambda message: True)
def respond_to_command(message):
    #determine if bumble bee responds correctly
    if random.random() <= correct_response_ratio:
        for key, correct_func in commands.items():
            if key in message.text:
                bot.reply_to(message, correct_func())
    else: #bumblebee selects a random command
        bot.reply_to(message, random.choice(list(commands.values()))())

bot.polling()
