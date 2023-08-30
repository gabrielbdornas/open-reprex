from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

load_dotenv()

# Replace these with actual values
login_url = 'https://prenotami.esteri.it/Services/Booking/2391'
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
search_text = "Stante l'elevata richiesta i posti disponibili per il servizio scelto sono esauriti."

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
chrome_options.add_argument(f'user-agent={user_agent}')


# Initialize the Selenium webdriver with the configured options
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(3)

# Open the login page
driver.get(login_url)
driver.get_screenshot_as_file("1_login_page.png")

# Find the login and password input fields and fill them
login_field = driver.find_element('name', 'Email')
password_field = driver.find_element('name', 'Password')
login_field.send_keys(login)
password_field.send_keys(password)

# Submit the form (you can replace this with actual form submission method if needed)
password_field.send_keys(Keys.RETURN)

# Allow some time for the page to load and the login to complete
time.sleep(3)
driver.get_screenshot_as_file("2_message_page.png")

# Check page message
if search_text in driver.page_source:
    print('Closed appointment')
else:
    print("Open appointment")

# Close the browser when done
driver.quit()