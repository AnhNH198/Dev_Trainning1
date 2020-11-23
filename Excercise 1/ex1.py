import requests
from selenium.webdriver import Chrome

driver = Chrome(executable_path='C:\\chromedriver.exe')
target = "http://45.79.43.178/source_carts/wordpress/wp-admin"


def get_current_username_requests():
    s = requests.Session()
    r = s.get(target, auth=('admin', '123456aA'))
    print(r.status_code)
    print(r.headers)


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
    # get_current_username_selenium()