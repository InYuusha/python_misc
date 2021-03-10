import smtplib as s
sm=s.SMTP('smtp.gmail.com',587)
sm.starttls()
for i in range(10):
    
    sm.login('asuse975@gmail.com','qwertyasdzx1234')

    sm.sendmail('asuse975@gmail.com','singhkajol955@gmail.com','Subject: Chatter')
