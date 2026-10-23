from simple_intrest import simple_interest

def test_simple_intrest():
    assert simple_interest(1000,3,5) == 150

def test_simple_intrest_zero():
    assert simple_interest(500,0,3) == 0