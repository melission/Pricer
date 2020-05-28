import random


def get_s_key():
    secret_key = ''.join(random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
                         for i in range(50))
    return secret_key
# print(secret_key)



