import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class E2ETests(unittest.TestCase):

    
    def setUp(self):
        options = self.get_default_chrome_options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://127.0.0.1:5000")  # Adjust URL as needed
        
    def tearDown(self):
        self.driver.quit()
    
    def get_default_chrome_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        return options        
    
    def test_browser_title_contains_app_name(self):
        self.assertIn("Named Entity", self.driver.title)
        
    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("heading").text
        self.assertEqual("Named Entity Finder", heading)
        
    def test_page_has_input_for_text(self):
        input_element = self._find('input-text')
        self.assertIsNotNone(input_element)
        
    def test_page_has_button_for_submitting_text(self):
        submit_button = self._find('find-button')
        self.assertIsNotNone(submit_button)
        
    def test_page_has_ner_table(self):
        input_element = self._find('input-text')
        submit_button = self._find('find-button')
        input_element.send_keys("Barack Obama was born in Hawaii.")
        submit_button.click()
        table = self._find('ner-table')
        self.assertIsNotNone(table)
        
        
    def _find(self, val):
        return self.driver.find_element(By.CSS_SELECTOR, (f'[data-test-id="{val}"]'))