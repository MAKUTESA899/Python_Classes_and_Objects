import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exercises.exercise1_person import Person


def test_person_attiributes():
    """
    Test if the person object has been initialized correctly
    """
    person = Person("Alice", 30)
    assert person.name == "Alice"
    assert person.age == 30    

def test_person_greet():
    '''Test for the person greet method'''
    person = Person("Bob", 25)
    assert person.greet() == "Hello, my name is Bob!"