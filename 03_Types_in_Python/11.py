from random import choice
import random
import string


lst = [
    {
        ''.join([choice(string.ascii_uppercase) for j in range(random.randint(1, 5))]): [
            {
                'required': random.randint(1, 5), 'selected': random.randint(1, 10)
            } for k in range(random.randint(1, 5))
        ]
    } for i in range(10)
]

print(lst)