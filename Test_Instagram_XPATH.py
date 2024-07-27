from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_instagram_followers_following():
    # Set up the Edge WebDriver
    options = Options()
    # Comment out headless mode for debugging purposes
    # options.add_argument("--headless")
    service = Service(executable_path='C:\\Users\\PREMA\\msedgedriver.exe')  # Specify your path to msedgedriver
    driver = webdriver.Edge(service=service, options=options)

    try:
        # Open the Instagram profile page
        driver.get("https://www.instagram.com/guviofficial/")

        # Adjust these relative XPaths according to the actual structure
        followers_xpath = "//ul/li[2]//span"
        following_xpath = "//ul/li[3]//span"

        # Wait for the elements to be present and visible
        followers = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, followers_xpath))
        ).text

        following = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, following_xpath))
        ).text

        print(f"Followers: {followers}")
        print(f"Following: {following}")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_instagram_followers_following()


#Output:

#Testing started at 17:16 ...
#Launching pytest with arguments C:\Users\PREMA\PAT-28\pythonProject\Test_Instagram_XPATH.py --no-header --no-summary -q in C:\Users\PREMA\PAT-28\pythonProject

#============================= test session starts =============================
#collecting ... collected 1 item

#Test_Instagram_XPATH.py::test_instagram_followers_following PASSED       [100%]
#Followers: 172K
#Following: 5


#============================= 1 passed in 14.51s ==============================

#Process finished with exit code 0
