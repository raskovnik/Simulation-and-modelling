import random

number = random.random()
print(number)

rand = random.randint(50, 60)
print(rand)

randrange = random.randrange(100, 190, 2)
print(randrange)

randfloat = random.uniform(100, 200)
print(randfloat)

randsample = random.sample(range(10, 20), 5)
print(randsample)

random.shuffle(randsample)
print(randsample)

randchoice = random.choice(randsample)
print(randchoice)