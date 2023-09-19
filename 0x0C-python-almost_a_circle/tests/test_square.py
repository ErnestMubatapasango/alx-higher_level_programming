#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    # ----------------- Tests for #2 ------------------------

    def test_A_class(self):
        '''Tests Square class type.'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        '''Tests if Square inherits Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
