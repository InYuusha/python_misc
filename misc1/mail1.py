import smtplib as s
sm=s.SMTP('smtp.gmail.com', 587)
sm.starttls()
sm.login('asuse975@gmail.com','qwertyasdzx1234')
sm.sendmail('asuse975@gmail.com','mercerd975@gmail.com','this is gonna be fun')
sm.quit()
