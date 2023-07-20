# Bot para aumentar visualizações no YouTube

from selenium import webdriver

def iniciar_driver():
  driver = webdriver.Firefox()
  return driver

