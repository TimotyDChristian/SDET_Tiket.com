from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path='C:/ProgramData/chocolatey/lib/chromedriver/tools/chromedriver.exe') #We need to specify the chromedriver path.
#Let's go to tiket.com website!
driver.get('https://tiket.com')

#Note that we always use the time.sleep() command, we need it to give delay to the website to load all the content first.
#First, let's find the Plane logo
link = driver.find_element_by_xpath('//*[@id="productWidget"]/div[1]/div[2]/div[1]/div/img')
link.click()

#Let's choose our departing & arrival airport, date, and passenger!

try:
#Choose "Sekali Jalan""
    oneway = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="productWidget"]/div[2]/div[1]/div[2]/div[1]/div/label'))
    )
    oneway.click()
#Choose our departing airport, let's fly from Jakarta!
    searchfrom = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, 'productSearchFrom'))
    )
    searchfrom.send_keys('Jakarta')
    time.sleep(2)
    searchfrom.send_keys(Keys.RETURN)
#Choose where do we want to go. Let's go to Surabaya!
    searchto = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, 'productSearchTo'))
    )
    searchto.send_keys('Surabaya')
    time.sleep(2)
    searchto.send_keys(Keys.RETURN)
#Departure Date
    departDate = driver.find_element_by_xpath('//*[@id="startDate"]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/table/tbody/tr[3]/td[3]')
    time.sleep(2)
    departDate.click()
#Passenger
    passenger = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="passengerCabin"]/div[2]/div/div/div[3]/div/span'))
    )
    time.sleep(2)
    passenger.click()
#Finish button
    finish = driver.find_element_by_xpath('//*[@id="productWidget"]/div[2]/div[3]/button')
    time.sleep(2)
    finish.click()
except:
    print('An error on choosing departure&arrival occured!')

#Choose plane
try:
    understand = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]'))
    )
    understand.click()
    time.sleep(2)

    choosePlane = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]'))
    )
    choosePlane.click()
    time.sleep(1)
    
except:
    print('An error occured when choosing plane!')

#Fill personal contact data
try:
    contactTitle = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By. XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[1]'))
    )
    contactTitle.click()
    time.sleep(1)

    cont_titleChoose = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By. XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div[3]/ul/li[1]'))
    )
    cont_titleChoose.click()
    time.sleep(1)

    contactName = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div[2]/div/input'))
    )
    contactName.click()
    contactName.send_keys('Timoty Des Christian')
    time.sleep(1)

    contactEmail = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[2]/div/input'))
    )
    contactEmail.click()
    contactEmail.send_keys('timothy.dch18@gmail.com')
    time.sleep(1)

    contactPhone = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[1]/div[3]/div[3]/div[2]/div/input'))
    )
    contactPhone.click()
    contactPhone.send_keys('08123456789')
    time.sleep(1)
#Choose passenger contact
    passengerTitle = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By. XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/input'))
    )
    passengerTitle.click()
    time.sleep(1)

    pass_titleChoose = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By. XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[3]/ul/li[1]'))
    )
    pass_titleChoose.click()
    time.sleep(1)

    passengerName = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/input'))
    )
    passengerName.click()
    passengerName.send_keys('Timoty Des Christian')
    time.sleep(1)

    contactContinue = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[2]/div/div[1]/div/div[7]/button'))
    )
    contactContinue.click()
    time.sleep(1)

    contactConfirm = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/div/div[3]/div/div/div/div/div[3]/button[2]'))
    )
    contactConfirm.click()
    time.sleep(1)

except:
    print('An error occured when filling personal data')

#Last step is the payment
try:
    bca = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div[4]/div/a[1]/div/div'))
    )
    bca.click()
    time.sleep(1)

except:
    lanjut = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div/div[3]/button'))
    )
    lanjut.click()
    time.sleep(1)
    print('An error occured when completing payment')
#script "lanjut" above works if there is a previous order that has not been processed.
