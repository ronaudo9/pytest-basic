# テストのスキップ
# pytest sec4/test_sec4_7.py -m "morning" -sでmorningのみテスト
# pytest sec4/test_sec4_7.py -m "not morning" -sでmorning以外をテスト
import pytest

def test_hello():
    print("hello")

@pytest.mark.morning
def test_goodmorning():
    print("goodmorning")

@pytest.mark.afternoon
def test_goodafternoon():
    print("goodafternoon")
