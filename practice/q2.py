
import hashlib
import random
import string

def score(x):
  if type(x) == str:
    x = x.encode()
  h = hashlib.sha256(x).digest()
  return 10000 - sum(h)

nickname = b'???????'

print(f"hi {nickname}!")

T = 10000000

my_score = score(nickname)

for i in range(T):
  computer_score = score(''.join(sorted(random.sample(string.ascii_uppercase, k=6))))
  if my_score < computer_score:
    print("you loooose :(")
    exit(-1)

  if i % 100000 == 0:
    print(f"{i//100000}%...")

print("clear!!!!")