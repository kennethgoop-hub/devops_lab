from app import sumar

def test_sumar():
    assert sumar(3, 4) == 7
    assert sumar(-1, 1) == 0