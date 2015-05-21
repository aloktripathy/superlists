__author__ = 'AL299758'

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        print('setting up------------------------')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(time_to_wait=3)

    def tearDown(self):
        print('tearing down---------------------')
        self.browser.quit()

    def test_title(self):
        print('now testing----------------------')
        self.browser.get('http://localhost:8080')
        self.assertIn('To-Do', self.browser.title)
        # self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')