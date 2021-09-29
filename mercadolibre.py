import unittest
from selenium import webdriver
from time import sleep

class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://www.mercadolibre.com.ar')
        driver.maximize_window()

    
    def test_search_ps5(self):
        driver = self.driver

        
        search_field = driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('iphone 11 pro')
        search_field.submit()
        sleep(3)

        
        
        condition=driver.find_element_by_partial_link_text('Nuevo')
        driver.execute_script("arguments[0].click();", condition)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        
        higher_price = driver.find_element_by_partial_link_text('Mayor precio')
        driver.execute_script("arguments[0].click();", higher_price)
        sleep(3)

        productos = {}

        for i in range(5):
            article_name= driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i+1}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-item__group.ui-search-item__group--title > a > h2').text
            
            
            article_price= driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i+1}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-result__content-columns > div.ui-search-result__content-column.ui-search-result__content-column--left > div.ui-search-item__group.ui-search-item__group--price > a > div > div > span.price-tag.ui-search-price__part > span.price-tag-amount > span.price-tag-fraction').text
            productos[article_name]=article_price
        
        for key in productos:
            print("-",key, " : " , productos[key]) 
        

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity = 2)