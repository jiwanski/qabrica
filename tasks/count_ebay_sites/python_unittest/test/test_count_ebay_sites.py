import unittest
from selenium import webdriver


class EbayTests(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_language_change(self):
        d = self.driver
        d.get("http://www.ebay.com")
        el = d.find_element_by_id("gf-fbtn")
        d.execute_script("return arguments[0].scrollIntoView();", el)
        els_langs = d.find_elements_by_xpath("//div[@id = 'gf-f']/descendant::li")
        lang_count = len(els_langs)
        assert lang_count == 48

    @classmethod
    def tearDown(self):
        self.driver.close()
        pass
