# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_gl(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_gl(self):
        success = True
        wd = self.wd
        wd.get("https://www.sputnik.ru/")
        wd.find_element_by_css_selector("span.b-w-weather-info__now-degree").click()
        wd.find_element_by_css_selector("div.b-w-now-temp").click()
        wd.find_element_by_xpath("//div[@class='b-w-now__other']/div[1]/span/i").click()
        wd.find_element_by_xpath("//div[@class='b-w-now__other']//span[.='Утром']").click()
        wd.find_element_by_css_selector("h2.b-w-title-h2").click()
        wd.find_element_by_xpath("//div[@class='b-w-select-days-wrap']//span[.='Утро']").click()
        wd.find_element_by_css_selector("i.b-w-conditions-small.b-w-conditions-small_2").click()
        wd.find_element_by_xpath("//div[@class='b-w-select-days-wrap']//span[.='21°']").click()
        wd.find_element_by_xpath("//div[@class='b-w-select-days-wrap']//dt[.='Влажность ']").click()
        wd.find_element_by_css_selector("div.b-promo-header").click()
        wd.find_element_by_css_selector("div.b-top-header.b-top-header_smi2").click()
        wd.find_element_by_css_selector("a.b-logo").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
