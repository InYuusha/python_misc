import smtplib as s
mail=str(input('Enter your Mail Address :'))
pas=str(input('Enter your Password :'))
mail1=str(input('Enter recievers Mail'))
para=str(input('Enter Message'))
sm=s.SMTP('smtp.gmail.com',587)
sm.starttls()

sm.login(mail,pas)
sm.sendmail(mail,mail1,para)
sm.quit()
