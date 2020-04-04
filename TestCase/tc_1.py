import pytest

@pytest.fixture()
def beforeAndafterTest():
    print("To Run Before Every TestCases")
    yield
    print("To Run After Every TestCases")

def test_tc_testcase1(beforeAndafterTest):
    print("This is execution of TestCase1")

def test_tc_testcase2(beforeAndafterTest):
    print("This is execution of TestCase2")