from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary as cdb
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time
import svg_captcha_solver

##Set values
parkname = ["Book a pass for Garibaldi Provincial Park","Book a pass for Golden Ears Provincial Park","Book a pass for Joffre Lakes Provincial Park"]
park_index = 0 # 0 for Garibaldi, 1 for Golden Ears, 2 For Joffre
day = "Friday, July 14, 2023"
passtypes = ['Rubble Creek - Parking','Alouette Lake Boat Launch Parking - Parking','Joffre Lakes - Trail']
#############
def setdate():
    clear_cal = driver.find_element(By.CLASS_NAME, "date-input__clear-btn")
    driver.execute_script("arguments[0].click();", clear_cal)
    select_cal = driver.find_element(By.XPATH, "/html/body/app-root/div/div[2]/app-registration/div/div[2]/div/div/div[2]/app-facility-select/form/div/app-date-picker/fieldset/button[1]")
    driver.execute_script("arguments[0].click();", select_cal)
    time.sleep(1)
    select_date = driver.find_element(By.CSS_SELECTOR, '[aria-label="'+day+'"]')
    driver.execute_script("arguments[0].click();", select_date)

def select_passtype(park_index):
    select_pass_type = Select(driver.find_element(By.ID, "passType"))
    select_pass_type.select_by_visible_text(passtypes[park_index])

def select_visittime():
    select_visit_time = driver.find_element(By.ID, "visitTimeDAY")
    driver.execute_script("arguments[0].click();", select_visit_time)

def hit_next():
   hit_next = driver.find_element(By.XPATH, "/html/body/app-root/div/div[2]/app-registration/div/div[2]/div/div/div[2]/app-facility-select/div/button")
   driver.execute_script("arguments[0].click();", hit_next)
   time.sleep(1)
   

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://reserve.bcparks.ca/dayuse/")


select_park = driver.find_element(By.CSS_SELECTOR, '[aria-label="'+parkname[park_index]+'"]')
driver.execute_script("arguments[0].click();", select_park)
setdate()
select_passtype(park_index)

for i in range(0,4):
    try:
        print(f"Iteration #{i}")
        i=i+1
        if i==4:
            break
        select_visittime()
        if park_index==2:
         Select(driver.find_element(By.ID, "passCount")).select_by_visible_text('4')
    except:
        driver.refresh()
        setdate()
        select_passtype(park_index)
        continue
    break

hit_next()

for i in range(0,4):
    try:
        i=i+1
        if i==4:
            break
        captcha2 = driver.find_element(By.XPATH, "//*[name()='svg']").get_attribute('outerHTML')
        svg_answer = svg_captcha_solver.solve_captcha(captcha2)
    except:
        driver.refresh()
        driver.refresh()
        setdate()
        select_passtype(park_index)
        select_visittime()
        if park_index==2:
         Select(driver.find_element(By.ID, "passCount")).select_by_visible_text('4')
        hit_next()
        continue
    break

driver.find_element(By.ID, "answer").send_keys(svg_answer)
time.sleep(1)

select_checkbox = driver.find_element(By.XPATH, "/html/body/app-root/div/div[2]/app-registration/div/app-contact-form/div/div/div[2]/div[1]/div/label/input")
driver.execute_script("arguments[0].click();", select_checkbox)

driver.find_element(By.ID, "firstName").send_keys('John')
driver.find_element(By.ID, "lastName").send_keys('Doe')
driver.find_element(By.ID, "email").send_keys('j.d@gmail.mail.ca')
driver.find_element(By.ID, "emailCheck").send_keys('j.d@gmail.mail.ca')


submit_finally = driver.find_element(By.XPATH, "/html/body/app-root/div/div[2]/app-registration/div/app-contact-form/div/div/div[2]/div[3]/button")
#driver.execute_script("arguments[0].click();", submit_finally)
time.sleep(4)
