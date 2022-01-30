import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display

pi = np.pi
g = 9.81

########## TESTS ##########
class Tests(unittest.TestCase):

    def test_1a(self, psi0):
        a = psi0(np.linspace(-25,25,100))
        b = np.load('tests/1a.npy')
        self.assertTrue(np.allclose(a,b))

    def test_1b(self, x, n, psi):
        self.assertTrue(np.allclose(np.load('tests/1b1.npy'),x))
        self.assertTrue(np.allclose(1500,n))
        self.assertTrue(np.allclose(np.load('tests/1b2.npy'),psi))

    def test_1c(self, V):
        self.assertTrue(np.allclose(np.load('tests/1c.npy'),V))

    def test_1d(self, H):
        self.assertTrue(type(H)==np.ndarray)
        self.assertTrue(np.allclose(np.load('tests/1d.npy'),H))

    def test_1e(self, CNO):
        self.assertTrue(np.allclose(np.load('tests/1e.npy'),CNO)) 

    def test_1g(self, norm):
        self.assertTrue(np.allclose(norm, 1))       
####################


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
