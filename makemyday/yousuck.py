from random import randint

expressions = [
    "you're terrible",
    "you're awful",
    "you're lousy",
    "you're dreadful",
    "you're abysmal",
    "you're pathetic",
    "you're horrendous",
    "you're garbage",
    "you're a disaster",
    "you're a failure",
    "you're a mess",
    "you're incompetent",
    "you're a letdown",
    "you're worthless",
    "you're a disappointment",
    "you're a joke",
    "you're hopeless",
    "you're pitiful",
    "you're useless",
    "you're a waste"
]


def yousuck(name):
    num = randint(1,len(expressions))
    return f'{name} {expressions[num]}'


