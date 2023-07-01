import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = False
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


def otomatikinstagramdoldurucu():  
    email = fakemailbulma()
    ad = fakeisimbulma()
    namesurname = "{} {}".format(ad[0], ad[2])
    password = "akfiadsa"
    url = "https://www.instagram.com/accounts/emailsignup/"
    driver.get(url)
    time.sleep(2) 
    
    # Enter email, name, and password
    a = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input')
    b = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input')
    c = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input') 
    a.send_keys(email)
    b.send_keys(namesurname)   
    c.send_keys(password)
    time.sleep(0.25)
    
    # Click Sign Up button
    d = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div[2]/form/div[5]/div/div/div/button/span')
    d.click()
    time.sleep(0.1)
    
    # Click Next button
    e = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button')
    e.click()
    time.sleep(2)
    
    # Select birthdate
    f = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select')
    select = Select(f)
    select.select_by_index(random.randint(1, 11))
    
    g = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select')
    select2 = Select(g)
    select2.select_by_index(random.randint(1, 29))
    
    h = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select')
    select3 = Select(h)
    select3.select_by_index(random.randint(22, 42))
    
    # Click Next button
    i = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button')
    i.click()
    time.sleep(2)  
    
    # Open new tab and switch to it
    driver.execute_script("window.open('');")
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    
    # Perform mail verification
    onaykodu = mailonayla()
    
    # Switch back to the original tab
    driver.switch_to.window(driver.window_handles[0])
    
    # Enter verification code and click Next
    j = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')
    kod = "{}".format(onaykodu[0])
    j.send_keys(kod)
    k = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
    k.click()
    
    # Wait for the process to complete (adjust the sleep duration based on your needs)
    time.sleep(10)
    
    # Close the browser
    driver.quit()


def mailonayla():
    ayrilmis_isim = []
    driver.get("https://www.fakemail.net/window/id/2")
    try:
        driver.find_element("xpath",'/html/body/div[1]/div[3]/div/div[1]/div[2]/span[4]').text
        
    except:
        time.sleep(3)
        mailonayla()
    a = driver.find_element("xpath",'/html/body/div[1]/div[3]/div/div[1]/div[2]/span[4]').text
    ayrilmis_isim = a.split()
    return ayrilmis_isim


def fakemailbulma():
    driver.get("https://www.fakemail.net/")
    a = driver.find_element("xpath",'/html/body/div[2]/div[2]/div[1]/div[1]/span[1]').text
    return a


def fakeisimbulma():
    driver.get("https://www.fakenamegenerator.com/")
    a = driver.find_element("xpath",'/html/body/div[2]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div[1]/h3').text
    ayrilmis_isim = a.split()
    return ayrilmis_isim


otomatikinstagramdoldurucu()
