import telebot
import random
import os
from telebot.types import Message

bot = telebot.TeleBot("7741243649:AAG5jBSAsVn6o1F7EuAz1ol8LW8rmI-Qtw0", parse_mode="HTML")


@bot.message_handler(commands=['start'])
def cmd_start(message: Message):
    bot.reply_to(message, "Hi, im a <b>bot for education</b> on the environment. Write /help to give you the commands this bot has")
    with open("otherphotos/recycle.png","rb") as file:
        bot.send_photo(message.chat.id,photo=file)


@bot.message_handler(commands=['help'])
def cmd_help(message: Message):
    bot.reply_to(message, "here's a list of commands:"
                 "\n/ideas - here you can suggest your ideas to save the planet"
                 "\n/recycablematerials - view a recycable material"
                 "\n/nonrecycablematerials - view a non recycable material"
                 "\n/yteducationalvid - get a link to an educational video about the environment"
                 "\n/read - view your suggestions")


@bot.message_handler(commands=['ideas'])
def cmd_ideas(message: Message):
    bot.reply_to(message, "write an idea to save the planet")
    bot.register_next_step_handler(message, add_task)

def add_task(message: Message):
    task = message.text
    with open("ideas.txt", "a", encoding="utf-8") as file:
        file.write(task + "\n")
        bot.reply_to(message, "your task has been added")


@bot.message_handler(commands=['recycablematerials'])
def cmd_recycablematerials(message: Message):
    mats = ["paper","cardboard","glass","aluminium","steel","tin","plastic","textiles","electronics","batteries","printer cartridges","copper","brass","iron","wood"]

    ran = random.choice(mats)
    bot.reply_to(message, ran)
    ranp= "recycablematerials/"+ran+".png"
    with open (ranp,"rb") as file:
        bot.send_photo(message.chat.id,photo=file)


@bot.message_handler(commands=['nonrecycablematerials'])
def cmd_nonrecycablematerials(message: Message):
    mats = ["styrofoam","plastic film","ceramic","mirror","used paper towels","chip bags","toothpaste tubes","plastic utensils","garden hoses","clothing hangers","broken toys made of mixed materials"]

    ran = random.choice(mats)
    bot.reply_to(message, ran)
    ranp= "nonrecycablematerials/"+ran+".png"
    with open (ranp,"rb") as file:
        bot.send_photo(message.chat.id,photo=file)


@bot.message_handler(commands=['yteducationalvid'])
def cmd_yteducationalvid(message: Message):
    bot.send_message(message, "[video here](https://www.youtube.com/watch?v=B-nEYsyRlYo)", disable_web_page_preview=True)


@bot.message_handler(commands=['read'])
def cmd_read(message: Message):
    with open("tasks.txt", "r", encoding="utf-8") as file:
        text = file.read()
        bot.reply_to(message, text)



bot.polling()
