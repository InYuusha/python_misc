Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'hello'.rjust(10)
'     hello'
>>> 'hello'.ljust(10)
'hello     '
>>> 'hello'.ljust(10,*)
SyntaxError: invalid syntax
>>> 'hello'.ljust(10,'*')
