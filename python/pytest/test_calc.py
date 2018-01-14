import sys
import pytest
from calc import some_complex_function

# Any function that has a test_ prefix will be discovered
# and test runner will execute it
def test_simple_test_case():
    assert some_complex_function(1, 2, 3) == 7

# You can mark a test to be skipped using @python.mark.skip
# decorator. While running your test suite, you can specify
# -rsx flag to check reasons for skipping test cases
# 
# Optionally you can also specify which version to skip test on
@pytest.mark.skipif(sys.version_info < (3,5), reason="obvious test on py < 3.5")
def test_obvious():
    assert some_complex_function(0, 0, 0) == 0

# Lets say you want to run all test that has keyword "simple" in them
# this can be done using -k flag. You simply pass flag -k <keyword> 
# python -m pytest -k simple -v
def test_simple_test_case_another():
    assert some_complex_function(2, 3, 4) == 11

# You can set tags to test and then selectively run those set of test3
# If you use tags you can run them using the -m flag
# python -m pytest -m universal -v
# pytest -m universal -v

# Negation of test is also possible
# pytest -m "not universal" -v
@pytest.mark.universal
def test_universal():
    assert some_complex_function(4, 5, 6) == 19

# You can parameterize your test cases

test_data = [
    (1, 2, 3, 7),
    (4, 5, 6, 19)
]

@pytest.mark.parametrize("a,b,c,expected_output", test_data)
def test_consolidated(a, b, c, expected_output):
    assert some_complex_function(a, b, c) == expected_output
                        