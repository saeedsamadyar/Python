#pylenium liberary

from pylenium.driver import pylenium

def test_google(py: pylenium):
    py.visit('https://google.com')
    py.get('[name="q"]').type('puppies')
    py.get('[name="btnk"]').type('puppies').submit()
    assert py.should().contain_title('puppies')
