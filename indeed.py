from selenium import webdriver
import time
import pandas as pd 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/")

# Search Indeed on google 
search = driver.find_element(By.NAME, 'q')
search.send_keys('Indeed')
search.send_keys(Keys.RETURN)
indeed = driver.find_element(By.CLASS_NAME,'MBeuO').click()

# Search 'Python Entry' on Indeed.com
job_title = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
job_title.send_keys("Python Entry")
job_title.send_keys(Keys.RETURN)

# Click within 50 miles 
miles_range = driver.find_element(By.ID, 'filter-radius')
miles_range.click()
fifty_miles = driver.find_element(By.LINK_TEXT, "within 50 miles").click()

time.sleep(5)


# List of postings 

postings = driver.find_elements(By.CSS_SELECTOR, "div[class='slider_container css-g7s71f eu4oa1w0']")
print(len(postings))

posting_list = []

for posting in postings:
    title = posting.find_element(By.XPATH,('.//a[@class="jcs-JobTitle css-jspxzf eu4oa1w0"]')).text
    company_name = posting.find_element(By.XPATH,('.//span[@class="companyName"]')).text
    location = posting.find_element(By.XPATH,('.//*[@class="companyLocation"]')).text 
    posting_item = {
        'Title' : title,
        'Company Name' : company_name,
        'Location' : location
    }
    posting_list.append(posting_item)

df = pd.DataFrame(posting_list)
print(df)
