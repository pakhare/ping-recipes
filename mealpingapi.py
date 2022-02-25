# Install pyTelegramBotAPI using:
# pip install pyTelegramBotAPI

import requests
import telebot

API_KEY = "YOUR API TOKEN HERE"

bot = telebot.TeleBot(API_KEY)

base_mealdb_url = 'https://www.themealdb.com/api/json/v1/1/search.php'
rand_url = 'https://www.themealdb.com/api/json/v1/1/random.php'


@bot.message_handler(commands=['start'])
def msg(randomm):
         
          bot.send_message(randomm.chat.id, "Try typing:\nMatar Paneer\n\nOr /random")

@bot.message_handler(commands=['random'])
def msg(randomm):
          rand = requests.get(rand_url)
          rand_json = rand.json()
          
          for rnd in rand_json["meals"]:
                 data = "Making: {},\n\nSteps:\n {},\nImage: {}, \n\nYouTube Video: {}".format(
                 rnd["strMeal"],
                 rnd["strInstructions"],
                 rnd["strMealThumb"],
                 rnd["strYoutube"]
                )
          print(data)
          bot.send_message(randomm.chat.id, data)

def recipe_request(mssg):
   reqt = mssg.text.split()
   if reqt[0].lower():
     return True
   else:
     return 
         
@bot.message_handler(func=recipe_request)
def send_recipe(mssg):
  try:    
         reqt = mssg.text.split()
         listToStr = ' '.join([str(elem) for elem in reqt])

         query_params = "?s={}".format(listToStr)
         final_url = base_mealdb_url + query_params
         reps = requests.get(final_url)
         reps_json = reps.json()

         for meal in reps_json["meals"]:
                 data = "Making: {},\n\nSteps:\n {},\nImage: {}, \n\nYouTube Video: {}".format(
                 meal["strMeal"],
                 meal["strInstructions"],
                 meal["strMealThumb"],
                 meal["strYoutube"]
                )
         print(data)
         bot.send_message(mssg.chat.id, data)
    
  except:
         bot.send_message(mssg.chat.id, "Sorry, No Recipes Found :( \nTry /random")
         
bot.polling()
