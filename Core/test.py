import pytest
def test():
    pytest.assume(1==2)
    pytest.assume(2==3)
    pytest.assume(4==4)
if __name__=="__main__":
    pytest.main(["-sq",__file__])