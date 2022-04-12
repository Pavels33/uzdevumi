import bcrypt
import time

parole = b'abols'

starts = time.time()

salt = bcrypt.gensalt(rounds=12) #generējam salt

savienots = bcrypt.hashpw(parole,salt)

beigas = time.time()

print(beigas - starts)
print(parole)
print(salt)
print(savienots)