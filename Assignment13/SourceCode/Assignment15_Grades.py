'''

CS 101 Lab
Program 13 - Unit Testing
Keagon Madison
kcmc2f@umkc.edu

PROBLEM:
Create a new python program, called Grades.py. Create another one called Assignment15_Grades.py.
Create multiple functions (total, average, and median) in Grades.py and then test those functions within Assignment15_Grades.py


ALGORITHM:
8 Unit testing cases will be defined within a class called Grade_Test.
Each of these testing cases will test different parts of functions in the Grades.py file.

ERROR HANDLING:
Unit testing will find possible errors from the Grades.py file.

OTHER COMMENTS:
There may be more unit testing I could add later on.

'''

import unittest
import Grades
import math

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grades.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33.")

    def test_total_returns_total_of_list(self):
        result = Grades.total([])
        self.assertEqual(result, 0, 'The total function should return 0 if the list is empty.')

    def test_average_one(self):
        result = Grades.average([2,5,9])
        self.assertAlmostEqual(result, 5.3333, 4, 'The average function should return 5.3333')

    def test_average_two(self):
        result = Grades.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12, 4, 'The average function should return 12.')

    def test_average_returns_nan(self):
        result = Grades.average([])
        self.assertIs(math.nan, result, 'The average function should return nan when passed an empty list.')
    
    def test_median_one(self):
        result = Grades.median([2, 5, 1])
        self.assertIs(result, 2, 'The median function should return 2')
    
    def test_median_two(self):
        result = Grades.median([5,2,1,3])
        self.assertAlmostEqual(result, 2.5, 4, 'The median function should return 2.5')
    
    def test_median_three(self):
        with self.assertRaises(ValueError):
            result = Grades.median([])




unittest.main()


