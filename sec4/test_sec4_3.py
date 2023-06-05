# fixtureを使ってクラスに対する前処理＆後処理
import pytest

@pytest.fixture(scope="class") # scopeはフィクスチャ関数が実行される粒度を指定
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

class TestExample():
    def test_example1(self, setup_processing):
        print("hello world!")

    def test_example2(self, setup_processing):
        print("pytest!")
