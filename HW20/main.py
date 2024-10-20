import unittest

class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


def formatted_name(first_name, last_name, middle_name=''):
   if len(middle_name) > 0:
       full_name = first_name + ' ' + middle_name + ' ' + last_name
   else:
       full_name = first_name + ' ' + last_name
   return full_name.title()


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_equal(self):
        f = Fibonacci()
        self.assertListEqual([f(0), f(1), f(2), f(3), f(4), f(5)],[0, 1, 1, 2, 3, 5])


class TestFormattedName(unittest.TestCase):
    def test_formatted_whit_middle_name(self):
        self.assertEqual(formatted_name("Alex","Potato","Richard"),
                         "Alex Richard Potato")

    def test_formatted_without_middle_name(self):
        self.assertEqual(formatted_name("Alex","Potato"), "Alex Potato")
