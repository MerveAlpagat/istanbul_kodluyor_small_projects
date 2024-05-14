Pytest Decoratorleri

import pytest

 @pytest.fixture
 Bu decorator, testlerde kullanılacak veri veya durumları sağlamak için kullanılır.
 Fixture'lar, test fonksiyonları arasında veri paylaşımını sağlar ve testlerin tekrar kullanılabilirliğini artırır.

@pytest.fixture
def my_fixture():
    data = "Bu bir örnek veridir"
    return data

def test_example(my_fixture):
    assert my_fixture == "Bu bir örnek veridir"


@pytest.mark.parametrize
 Bu decorator, aynı test fonksiyonunu farklı parametrelerle çalıştırmak için kullanılır.
 Her bir parametre seti için ayrı bir test çalıştırılır.

@pytest.mark.parametrize("input, expected_output", [
    (1, 2),
    (5, 10),
    (10, 20)
])
def test_multiply_by_two(input, expected_output):
    assert input * 2 == expected_output


 @pytest.mark.skip
 Bu decorator, bir testin atlanmasını sağlar. Test henüz hazır değilse veya belirli bir koşulu karşılamıyorsa kullanılabilir.

@pytest.mark.skip(reason="Bu test henüz hazır değil")
def test_incomplete_function():
    pass

 @pytest.mark.skipif
 Bu decorator, belirli bir koşul sağlandığında bir testin atlanmasını sağlar.
 Örneğin, belirli bir Python sürümünde çalışmıyorsa testi atlamak için kullanılabilir.

import sys

@pytest.mark.skipif(sys.version_info < (3, 6), reason="Python 3.6'dan önce çalışmaz")
def test_functionality():
    assert True


 @pytest.mark.xfail
 Bu decorator, bir testin bilerek veya geçici bir süre için başarısız olmasını beklediğimizi belirtmek için kullanılır.

@pytest.mark.xfail
def test_something():
    assert False  # Bu test bilerek başarısız olacak şekilde yapılmıştır
