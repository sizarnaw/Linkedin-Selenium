from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set the path to your Chrome webdriver executable
def read_credentials_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the contents of the file and return it as a string
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error occurred while reading the file: {e}")


# Open the Chrome browser
file_path = 'Credentials.txt'
credentials = read_credentials_file(file_path)
if len(credentials) == 2:
    print("Contents of credentials.txt:")
    email = credentials[0]
    password = credentials[1]
    print(email)
    print(password)
else:
    exit("Credentials not correct please put first line email second line password")
email = credentials[0]
password = credentials[1]


driver = webdriver.Chrome()

print(driver)
print("2222")
# Navigate to the LinkedIn login page
driver.get('https://www.linkedin.com')

# # Find the username and password input fields, and submit the credentials
WebDriverWait(driver, 20).until(EC.title_contains('LinkedIn'))
try:
    
    username_field = driver.find_element(By.ID, 'session_key')
    username_field.send_keys(email)
except webdriver.common.exceptions.NoSuchElementException:
        print("SDFSDF")

password_field = driver.find_element(By.ID, 'session_password')
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# # Wait for the login process to complete

# Navigate ts the Jobs page
driver.get('https://www.linkedin.com/jobs')

#need to fdix here !!!! 
empty = ''
jobsearch = driver.find_element(By.ID, 'jobs-search-box-keyword-id-ember386')
jobsearch.send_keys(empty)
jobsearch.send_keys(Keys.RETURN)


#click on data posted and click on past 24 hours
date_posted_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'ember690')))
date_posted_button.click()
last_24_hours_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'timePostedRange-r86400')))
last_24_hours_option.click()

#click on show results


show_results = driver.find_element(By.ID, 'ember1049')
show_results.click()


# # Perform a job search by entering keywords and location
# search_keywords = 'Python Developer'
# search_location = 'New York'

# search_input = driver.find_element(By.XPATH, '//input[@aria-label="Search jobs"]')
# search_input.send_keys(search_keywords)
# search_input.send_keys(Keys.RETURN)

# location_input = driver.find_element(By.XPATH, '//input[@aria-label="Search location"]')
# location_input.clear()
# location_input.send_keys(search_location)
# location_input.send_keys(Keys.RETURN)

# # Wait for the job search results to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//ul[contains(@class, "jobs-search-results__list")]')))

# # Extract the job details from the search results
# job_elements = driver.find_elements(By.XPATH, '//li[contains(@class, "job-search-card")]')

# for job_element in job_elements:
#     title = job_element.find_element(By.XPATH, './/h3').text
#     company = job_element.find_element(By.XPATH, './/h4').text
#     location = job_element.find_element(By.XPATH, './/span[contains(@class, "job-search-card__location")]').text

#     print("Title:", title)
#     print("Company:", company)
#     print("Location:", location)
#     print("--------")

# Close the browser
driver.quit()