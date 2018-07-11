import telebot
import re
import random
from telebot import types
from secret_vars import TOKEN

bot = telebot.TeleBot(TOKEN)
correct_response_ratio = .8 #will respond correctly 80% of the time

f = open("bumblebee.barks")
barks = [line.strip() for line in f.readlines()]
f.close()


def sit():
    return "bumblebot sits" 

def bark():
    return random.choice(barks)

def good_girl():
    return "bumblebot wags her tail excitedly and runs around in a little circle"

def kill():
    return "bumblebot enters a blood frenzy. her eyes turn red and roll back into her head. she'll be back in an hour"

commands = {
        "sit": sit,
        "speak": bark,
        "good girl": good_girl,
        "kill": kill
        }

@bot.message_handler(func=lambda message: True)
def respond_to_command(message):
    #determine if bumble bee responds correctly
    if random.random() <= correct_response_ratio:
        for key, correct_func in commands.items():
            if key in message.text:
                bot.reply_to(message, correct_func())
    else: #bumblebot selects a random command
        bot.reply_to(message, random.choice(list(commands.values()))())

bot.polling()
