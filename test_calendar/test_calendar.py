import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import globalConstants as c
from selenium.webdriver.support import expected_conditions as ec 

class TestCalendar():
  
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.get(c.BASE_URL)
    self.driver.maximize_window()
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_filter_calendar(self):

    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME,c.EMAIL_NAME))).send_keys(c.EMAIL)
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.NAME,c.PASSWORD_NAME))).send_keys(c.PASSWORD)
    self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH).click()
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.LINK_TEXT,"Takvim"))).click()
    WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.ID,c.CALENDAR_SEARCH_EVENT_ID ))).send_keys("yazılım kalite ve test")
    courses = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR,c.CALENDAR_COURSES_ITEM_CSS)))
    assert "Yazılım Kalite ve Test Uzmanı" in courses.text
  
