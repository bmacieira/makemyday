from random import randint

compliments = [
    "you're amazing!",
    "you're incredible!",
    "you're outstanding!",
    "you're phenomenal!",
    "you're exceptional!",
    "you're fantastic!",
    "you're impressive!",
    "you're a superstar!",
    "you're a champion!",
    "you're the best!",
    "you're a legend!",
    "you're brilliant!",
    "you're talented!",
    "you're remarkable!",
    "you're a rockstar!",
    "you're outstanding!",
    "you're extraordinary!",
    "you're a powerhouse!",
    "you're a genius!",
    "you're a shining star!"
]

def yourock(name):
    num = randint(0,len(compliments))
    return f'{name} {compliments[num]}'

def makemehappy(num):
    list=[]
    try:
        for i in range(num):
            r = randint(0, len(compliments)-1)
            list.append(compliments[r])
    except Exception as e:
        return e
    else:
        return list
