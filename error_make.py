class MyError(Exception):
    def __str__(self):
        return "Not allowed."

def nick(nick):
    if nick == 'idiot':
        raise MyError()
    print(nick)

try:
    nick('angel')
    nick('idiot')
except MyError as e:
    print(e)