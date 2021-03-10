import threading as t
threadobj=t.Thread(target=print , args=['cats','dogs','frogs'],kwargs={'sep':'&'})
threadobj.start()
