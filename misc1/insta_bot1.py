from instabot import Bot
bot=Bot()
bot.login(username="doingstuffswithpython",password="qwertyasdzx1234")
#bot.send_message(" Follow mypage @doingstuffswithpython","doingstuffswithpython")
#l=bot.following
#n=bot.followers

#u=bot.get_media_id_from_link("https://www.instagram.com/p/CGHTI7_gaEs/?utm_source=ig_web_copy_link")
#print("following="+str(len(l)))
#print("followers="+str(len(n)))

f=bot.get_user_followers()
for i in f:
    name=(bot.get_username_from_user_id(int(i)))
    bot.send_message("plz follow @doingstuffswithpython",name)


    