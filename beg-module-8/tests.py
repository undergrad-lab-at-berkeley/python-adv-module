import math
import random
import __main__
import datetime
import unittest
import numpy as np
import pandas as pd
from IPython.display import Markdown, display
import os

pi = np.pi
g = 9.81

########## TESTS ##########
class Tests(unittest.TestCase):

    def test_1a(self, cols):
        self.assertTrue(np.allclose(cols, np.load('tests/1a.npy')))

    def test_1b(self, df):
        self.assertTrue(df.equals(pd.read_pickle('tests/1b.pkl')))

    def test_1d(self, df):
        self.assertTrue(df.equals(pd.read_pickle('tests/1d.pkl')))

    def test_1e(self, df):
        self.assertTrue(df.equals(pd.read_pickle('tests/1e.pkl')))

    def test_1f(self, df):
        self.assertTrue(df.equals(pd.read_pickle('tests/1f.pkl')))

    def test_1g(self, df):
        self.assertTrue(df.equals(pd.read_pickle('tests/1g.pkl')))

    def test_1h(self):
        self.assertTrue('my_hr.png' in os.listdir(os.getcwd()))    

    def test_2a(self, df):
        self.assertTrue(df.equals(pd.read_pickle('tests/2a.pkl')))
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
