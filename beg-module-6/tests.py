import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display


########## TESTS ##########
class Tests(unittest.TestCase):
        
    def test_1(self, f):
        str1 = 'This is a test'
        str2 = 'My lymph nodes were swollen when I had mold poisioning'
        str3 = 'She told everyone I ran over a deer'
        a = 7
        b = 30
        c = 15
        self.assertEquals(f('This is a test'), 7)
        self.assertEquals(f('My lymph nodes were swollen when I had mold poisioning'), 30)
        self.assertEquals(f('She told everyone I ran over a deer'), 15)

    def test_2(self, f):
        self.assertEquals(f(20,5,2), 7)
        self.assertEquals(f(30,5,2), 11)
        self.assertEquals(f(40,5,2), 15)
        self.assertEquals(f(40,5,2), 15)


    def test_3(self, f):
        dic = {'o': 1, 's': 2, 'k': 3, 'i': 4, 'b': 5, 'e': 6, 'a': 7, 'r': 8}
        self.assertEquals(f, dic)

    def test_4(self, newton):
        a = lambda x: x**2-4
        b = lambda x: np.exp(x) - 5*x - 9
        c = lambda x: x**6 + 2*x**5 - 3

        self.assertTrue(np.allclose(newton(a), 2))
        b = newton(b)
        self.assertTrue(np.allclose(b, -1.76579) or np.allclose(b, 3.22358))
        c = newton(c)
        self.assertTrue(np.allclose(c, -2.07752) or np.allclose(c, 1))

########## TESTS ##########


def printmd(string):
    display(Markdown(string))

tests = Tests()

def run(test_name, *args, hint=False):
    dt = datetime.datetime.now()
    try:
        getattr(tests, test_name)(*args)
    except tests.failureException as e:
        printmd(f'**<span style="color: red;">Failed // {dt}</span>**')
        if hint:
            print('Hint:',  e)
        return
    printmd(f'**<span style="color: green;">Passed // {dt}</span>**')