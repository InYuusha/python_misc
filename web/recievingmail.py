import imapclient as i
imapobj=i.IMAPClient('imap.gmail.com',ssl=True)
imapobj.login('asuse975@gmail.com','qwertyasdzx1234')
imapobj.select_folder('INBOX', readonly=True)
uid=imapobj.search(['SINCE 8-AUG-2020'])
print(uid)
