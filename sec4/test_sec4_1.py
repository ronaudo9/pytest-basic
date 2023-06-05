# fixtureの利用(自分の選択した関数に前処理、後処理をすることができる)
import pytest

@pytest.fixture()
def setup_processing(request):
    print("setup_processing")
    def teardown_processing():
        print("teardown_processing")
    request.addfinalizer(teardown_processing)

def test_hello(setup_processing):
    print("hello")

def test_goodmorning():
    print("goodmorning")

def test_goodafternoon(setup_processing):
    print("goodafternoon")
