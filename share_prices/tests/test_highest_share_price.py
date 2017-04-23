import os
import unittest

from share_prices import highest_share_price


class TestHighestSharePrice(unittest.TestCase):

    def setUp(self):
        self.f_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_share_prices.csv')
        self.response = highest_share_price(self.f_path)

    def test_highest_share_price_response_length(self):
        self.assertEqual(len(self.response), 10)

    def test_highest_share_price_data(self):
        self.assertDictEqual(self.response['Wipro'], {'Price': '998', 'Month': 'November', 'Year': '2011'})
        self.assertDictEqual(self.response['IndiGo'], {'Price': '966', 'Month': 'December', 'Year': '2012'})
        self.assertDictEqual(self.response['BankBazaar'], {'Price': '990', 'Month': 'October', 'Year': '2012'})
        self.assertDictEqual(self.response['MphasiS'], {'Price': '986', 'Month': 'September', 'Year': '2013'})
        self.assertDictEqual(self.response['IDFC'], {'Price': '994', 'Month': 'December', 'Year': '2014'})
        self.assertDictEqual(self.response['GAIL'], {'Price': '995', 'Month': 'September', 'Year': '2012'})
        self.assertDictEqual(self.response['Infosys'], {'Price': '983', 'Month': 'April', 'Year': '2014'})
        self.assertDictEqual(self.response['CEAT'], {'Price': '997', 'Month': 'March', 'Year': '2012'})
        self.assertDictEqual(self.response['Snapdeal'], {'Price': '963', 'Month': 'April', 'Year': '2011'})
        self.assertDictEqual(self.response['Flipkart'], {'Price': '996', 'Month': 'February', 'Year': '2013'})


if __name__ == '__main__':
    unittest.main()
