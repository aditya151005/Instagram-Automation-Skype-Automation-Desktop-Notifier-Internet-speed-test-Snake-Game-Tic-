from instabot import Bot 
bot=Bot()
bot.login(username="username",password="password")
# bot.follow("Duniyaindia")
# bot.upload_photo("C:/Users/Aditya Ranjan/Pictures/Screenshots/1.png",caption="I love python")
# bot.unfollow("Duniyaindia)
# bot.send_message("Hi testing",["sonukumar"])
# followers=bot.get_user_followers("adityaranjan")
# for follower in followers:
#     print(bot.get_user_info(follower))
followings=bot.get_user_following("adityaranjan")
for following in followings:
    print(bot.get_user_info(following))