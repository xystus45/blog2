import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Quote class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        
        self.new_quote = Quote("python", "It works")
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))
