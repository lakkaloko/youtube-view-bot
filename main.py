# Bot para aumentar visualizações no YouTube

from selenium import webdriver

def iniciar_driver():
  
  driver = webdriver.Firefox()
  
  driver.get("https://www.youtube.com")
  
  print("Página aberta!")
  
  return driver


def verificar_url(url):

  if not url.startswith("https://www.youtube.com"):
    print("URL inválida!")
    
  else:
    print("URL válida.")


def assistir_video()
  for i in range(10):
   # assiste video
   driver.refresh()
   

def main():

  driver = iniciar_driver()
  
  verificar_url("https://www.google.com")


main()
