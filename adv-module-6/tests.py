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

    def test_1a(self, det):
    	self.assertTrue(det([5])==5)
    	self.assertTrue(det([1])==1)
    	self.assertTrue(det([[1,2],[3,4]])==-2)
    	self.assertTrue(det([[-1,5],[6,-8]])==-22)

    def test_1b(self, det):
    	self.assertTrue(det([[3,2,1],[4,5,5],[7,8,9]])==10)
    	self.assertTrue(det([[1,2,3,4,5],[6,7,4,9,0],[11,72,13,14, 15],[16,17,18,19,20],[1,2,2,4,25]])==-243000)
   
    def test_2a(self, mass):
    	self.assertTrue(np.allclose(mass("H2"), 2.016))
    	self.assertTrue(np.allclose(mass("OH"), 17.007))
    	self.assertTrue(np.allclose(mass("UO2"), 270.027))
    	self.assertTrue(np.allclose(mass("C6H14"), 86.178))

    def test_2b(self, mass):
    	self.assertTrue(np.allclose(mass("H2"), 2.016))
    	self.assertTrue(np.allclose(mass("OH"), 17.007))
    	self.assertTrue(np.allclose(mass("UO2"), 270.027))
    	self.assertTrue(np.allclose(mass("C6H14"), 86.178))
    	self.assertTrue(np.allclose(mass("Cs2O"), 281.810))
    	self.assertTrue(np.allclose(mass("NaOH"), 39.997))

    def test_2c(self, mass):
    	self.assertTrue(np.allclose(mass("H2"), 2.016))
    	self.assertTrue(np.allclose(mass("OH"), 17.007))
    	self.assertTrue(np.allclose(mass("UO2"), 270.027))
    	self.assertTrue(np.allclose(mass("C6H14"), 86.178))
    	self.assertTrue(np.allclose(mass("Cs2O"), 281.810))
    	self.assertTrue(np.allclose(mass("NaOH"), 39.997))
    	self.assertTrue(np.allclose(mass("Ca(OH)2"), 74.092))
    	self.assertTrue(np.allclose(mass("(NH4)2SO4"), 132.134))
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
