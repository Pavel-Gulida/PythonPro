from django.db.models.expressions import result


class frange:

    def __init__(self, start, end=None, step=1):
        self.step = step
        self.reverse = False
        if end == None:
            self.start = 0
            self.end = start
        else:
            if start > end:
                self.reverse = True
            self.start = start
            self.end = end


    def __next__(self):
        if (self.reverse and self.step>0)or self.step==0:
            raise StopIteration("Error")
        if not self.reverse:
            if self.start >= self.end:
                raise StopIteration("Error")
        else:
            if self.start <= self.end:
                raise StopIteration("Error")

        result = self.start
        self.start += self.step
        return result

    def __iter__(self):
        return self


for i in frange(1, 100, 3.5):
    print(i)


assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])


print('SUCCESS!')