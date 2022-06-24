# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 21:58:20 2022
This instagram bot was created for the purpose of automating instagram's basic functions.
This paticular bot will be able to follow people or unfollow (does this either to one person or a list of people)
It will be able to send messages and likes. It will even be able to count the number of followers a user has 

YOU MUST INPUT YOUR LOGIN CREDENTIALS FOR THIS SCRIPT TO WORK

BE SURE TO COMMENT OUT PARTS OF THE CODE YOU DON'T NEED OR ELSE IT WILL RUN IT AND MESS UP!'
@author: irvin
"""
#importations
from instabot import bot

#create a bot variable
bot = bot()

#Login credentials
bot.login(username="your_username_id", password="your_password")

#to follow a list of users (you must have ids already at hand, also works with 1 user)
list_of_user = ["user1", "user2", "user3", "....etc"]
bot.follow_users(list_of_user)

#to unfollow a list of users ( list must be at hand, also works with 1 user)
#unfollow_list = ["user1", "user2", "user3", "...etc"]
#bot.unfollow_users(unfollow_list)

#to unfollow everyone you have
#bot.unfollow_everyone()

#to count the number of followers a user has
followers = bot.get_user_followers("insert_user_here")
print("The number of followers are: ")
print(len(followers))

#to send messages to a list of users (must have list at hand)
message = "Your message"
list_of_users = ["user1", "user2", "user3", "...etc"]
bot.send_messages(message, list_of_users)

#send likes to people on a list
send_like_list = ["user1", "user2", "user3", "...etc"]
bot.send_like(send_like_list)

#to post a photo (acceptable image ratio 90:47, 4:5, 1:1 square image)
bot.upload_photo("filename.jpg", caption="write your caption here")