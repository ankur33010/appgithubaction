from src.Maths_Operations import add,sub

def test_add():
    assert add(3,4)==7 # assert is the functions which check whether the condition is True or False 
    assert add(9,41)==50


def test_sub():
    assert sub(8,3)==5
    assert sub(45,4)==41
    assert sub(45,5)==41