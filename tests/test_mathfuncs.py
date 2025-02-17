import pytest
from mypackage.mathfuncs import addnums

def test_add():
    assert addnums(1,2) == 3
    assert addnums(2,2) == 4
    assert addnums(10,2000) == 2010
