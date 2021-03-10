
'''          SENDING MESSAGES ON
             INSTAGRAM USING PYTHON 
             
     SENDING MESSAGE TO ONLY CODING/PROGRAMMING PAGES FROM MY FOLLOWERS
             -----------------------
                                     @doingstuffswithpython   '''

from instabot import Bot
import re

bot=Bot()
bot.login(username="username",password="pass")

coders=["python","code","coding","programming","developers"]

list_of_followers=bot.get_user_followers(40212364045)    
                                           #user ID
for i in list_of_followers:
    uname=bot.get_username_from_user_id(int(i)) #converts userID
                                                #into username
    
    for substr in coders:

        if re.search(substr,uname):
            print(name) #to whom the message is being sent

            bot.send_message("Hey greetings
            \nPlease checkout my profile @doingstuffswithpython
            \n and if you like it then please do leave a like\n
            it means a lot to me...thanks....:)",uname)














