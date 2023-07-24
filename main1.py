# Bot para aumentar visualizações no YouTube

from selenium import webdriver 
from random import randint
from multiprocessing import Process
import time

url = input("Informe a URL: ")

contador = 0

def view_video():
  
  global contador

  options = webdriver.FirefoxOptions()
  options.headless = True
  driver = webdriver.Firefox(options=options)
  

  print("iniciando driver...")

  driver.get(url)
  driver.minimize_window()

  duration = int(driver.execute_script("return document.getElementById('movie_player').getDuration()"))

while True:

  time.sleep(randint(3,5))
  webdriver.refresh()

  contador += 1

if contador % 10 == 0:
  print(f"Views: {contador}")
    
  print("Finalizando driver...")

  watched = 0
  while watched < duration * randint(25, 100) / 100:
    
    time.sleep(randint(3,5))
    driver.refresh()

    watched += randint(3, duration)

  driver.quit()

if __name__ == "__main__":

  while True:

    drivers = []

    for i in range(5):
      p = Process(target=view_video)
      p.start()
      drivers.append(p)

    # aguarda drivers finalizarem
    for driver in drivers:
      driver.join()
    
print(f"Total views: {contador}")

time.sleep(60)
