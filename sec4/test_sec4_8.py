# テストのスキップ
#pytest sec4/test_sec4_8.py -k "hello" -s -kで文字列を指定し、指定した文字列のみテストを実行
def test_hello1():
    print("hello1")

def test_hello2():
    print("hello2")

def test_afternoon1():
    print("afternoon1")
