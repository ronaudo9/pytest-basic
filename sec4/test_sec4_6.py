# テストのスキップpytest sec4/test_sec4_6.py -vで実行
import pytest

def test_hello():
    print("hello")

@pytest.mark.skip(reason="write reason")
def test_goodmorning():
    print("goodmorning")

def test_goodafternonn():
    print("goodafternoon")
