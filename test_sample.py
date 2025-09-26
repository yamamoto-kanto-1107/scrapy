import pytest
from main import start
from selenium.common.exceptions import TimeoutException

class TestClass:
  def test_fouth(self,monkeypatch):
    class Dummy:
      def __init__(self,driver,time):
        pass
      def until(self,method):
        raise TimeoutException('no item')

    monkeypatch.setattr('main.WebDriverWait',Dummy)
    result = start()
    assert result == False


  def test_third(self,monkeypatch):
    def dummy(a,b):
      return False
    monkeypatch.setattr('main.sum_values',dummy)
    result = start()
    print(result)
    assert result == False



  @pytest.mark.description("ul がない場合は False を返す")
  def test_second(self,monkeypatch):
    class Dummy_func():
      def __init__(self,driver,timeout):
        pass

      def until(self,method):
        raise TimeoutException("ul not found")

    monkeypatch.setattr("main.WebDriverWait", Dummy_func)
    result = start()
    assert result == False

  def test_one(self):
    phone = "03-6859-8953"
    get_value = start()

    assert phone == get_value
