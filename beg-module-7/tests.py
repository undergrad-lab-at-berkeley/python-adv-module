import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display


########## TESTS ##########
class Tests(unittest.TestCase):
        
    def test_1(self, arr, final_arr):
        self.assertTrue(np.allclose(arr, [1,2,3,4,5,6,7,8,9,10,11]))
        self.assertTrue(np.allclose(final_arr, [1,3,5,7,9,11]))

    def test_2a(self, st):
        a = np.arange(10).reshape(2,-1)
        b = np.repeat(1, 10).reshape(2,-1)
        forward = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
        backward = np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])


    def test_2b(self, st):
        a = np.arange(10).reshape(2,-1)
        b = np.repeat(1, 10).reshape(2,-1)
        forward = np.array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],[5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
        backward = np.array([[1, 1, 1, 1, 1, 0, 1, 2, 3, 4],[1, 1, 1, 1, 1, 5, 6, 7, 8, 9]])
        self.assertTrue(np.allclose(forward, st(a,b)))
        self.assertTrue(np.allclose(backward, st(b,a)))

    def test_3a(self, f):
        self.assertEquals(f(8,9), 18)
        self.assertEquals(f(14,3), 28)

    def test_3b(self, f):
        a = [1,2,3]
        b = [2,2,2]
        c = [1,3,2]
        self.assertTrue(np.allclose(f(a,b), [4, 4, 6]))
        self.assertTrue(np.allclose(f(a,c), [2, 6, 6]))
        self.assertTrue(np.allclose(f(b,c), [4, 6, 4]))


    def test_4(self, g):
        grey = np.load('tests/grey.npy')
        self.assertTrue(np.allclose(grey, g))
        # np.testing.assert_array_almost_equal(f([[1,2,3],[0,1,4],[5,6,0]]), [[-24,18,5],[20,-15,-4],[-5,4,1]])

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