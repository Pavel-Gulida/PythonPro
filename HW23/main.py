import string
import random

class custom_map:

    def __init__(self, dictionary:dict, func1, func2):
        self.keys = list(dictionary.keys())
        self.values = list(dictionary.values())
        self.func1 = func1
        self.func2 = func2
        self.step=-1

    def __next__(self):
        self.step += 1
        if self.step==len(self.keys):
            raise StopIteration("Error")

        return (self.func1(self.keys[self.step]), self.func2(self.values[self.step]))

    def __iter__(self):
        return self

print(list(custom_map({"1":1,"2":2},lambda x : x+"^2", lambda x : x**2)))

def gen_words(count):
    if count > 10000:
        raise ValueError("Max count is 10000")
    for i in range(count):
        len = random.randint(5,15)
        word=""
        for j in range(len):
            word += random.choice(string.ascii_letters)
        yield word

print(len(set(gen_words(10000))))
