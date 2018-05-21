import os, sys,platform,stat,random

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sa = []
for i in range(99999):
    sa.append(random.choice(seed))
salt = ''.join(sa)
print salt