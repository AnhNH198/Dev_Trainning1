import requests
from selenium.webdriver import Firefox
from bs4 import BeautifulSoup

driver = Firefox()
target = "http://45.79.43.178/source_carts/wordpress/wp-admin/"
log = "http://45.79.43.178/source_carts/wordpress/wp-login.php"

def get_current_username_requests():
    s = requests.Session()
    r = s.get(target, auth=('admin', '123456aA'))
    print(r.status_code)
    key = {'log': 'admin', 'pwd': '123456aA', 'wp-submit': 'Log in',
           'redirect_to': target, 'testcookie': '1'}
    res = requests.post(log, data=key)
    text = BeautifulSoup(res.text)
    mydivs = text.findAll
    print(mydivs)

def get_current_username_selenium():
    # Connect to target
    driver.get(target)

    # Get username and password input
    username = driver.find_element_by_id("user_login")
    password = driver.find_element_by_id("user_pass")

    # Send value to input form
    username.send_keys("admin")
    password.send_keys("123456aA")

    # Submit form
    driver.find_element_by_name("wp-submit").click()


if __name__ == '__main__':
    get_current_username_requests()
    #get_current_username_selenium()