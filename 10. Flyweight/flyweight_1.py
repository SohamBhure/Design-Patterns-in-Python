import random
import string
from unicodedata import name


class User:

    def __init__(self):
        self.name = name


class User2:

    strings = []

    def __init__(self, full_name):

        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings)-1

        self.names = [get_or_add(x)
                      for x in full_name.split(' ')]
        
    def __str__(self):
        return ' '.join(
            [self.strings[x] for x in self.names]
        )


def random_string():
    chars = string.ascii_lowercase
    return ''.join(
        [random.choice(chars) for x in range(8)]
    )


users = []

first_names = [random_string() for x in range(100)]
last_names = [random_string() for x in range(100)]

for f in first_names:
    for l in last_names:
        users.append(User2(f'{f} {l}'))

print(users[0])