"""_summary_"""
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_scraper() -> webdriver.Chrome:
    """Setup the webdriver for selenium

    Returns:
        webdriver.Chrome: The webdriver to be used to open linkedin pages
    """
    # prep the webdriver
    # Set the chrome options (so browser window doesn't close)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument("--headless")

    # open the driver
    browser = webdriver.Chrome(options=chrome_options)
    # NOTE - optional window size setting
    browser.set_window_size(1800, 900)
    return browser


# depreciated
def open_linkedin_search(browser: webdriver.Chrome):
    """Open linkedin in the given web driver, log in if needed, and go to
    the /search page to prep for future search URLS"""

    # TODO - figure out a better place for this or way to do auth
    # open config json to get linkedin username and pw
    config_file = open("config.json", encoding="utf-8")
    config_json = json.load(config_file)
    linkedin_username = config_json["linkedin_username"]
    linkedin_password = config_json["linkedin_password"]

    browser.get("https://linkedin.com/uas/login")
    # waiting for the page to load
    # TODO - find a way to test for elements to continue
    # --- Or make this a slightly random number in case this raises alerts
    time.sleep(2)
    # entering username
    username = browser.find_element(By.ID, "username")
    username.send_keys(linkedin_username)
    # entering password
    pword = browser.find_element(By.ID, "password")
    pword.send_keys(linkedin_password)
    # Clicking on the log in button
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    # TODO - find a way to test for elements to continue
    # --- Or make this a slightly random number in case this raises alerts
    time.sleep(2)
    browser.get(

        "https://www.linkedin.com/jobs/search?keywords=software&geoId=103039849&f_WT=1%2C2%2C3&f_TPR=r86400"
    )


def scrape_linkedin_page(browser: webdriver.Chrome, url: str) -> list[dict]:
    # TODO - update doc string
    """Open a single linkedin search page form URL in a given webdriver.
    Returns a list of jobs from that search page.

    Args:
        browser (webdriver.Chrome): Selenium webdriver to open linkedIn
        url (str): URL string of LinkedIn search page

    Returns:
        list[dict]: List of jobs from the returned search page.
                - TODO define the dict format of the job info
    """
    # TODO - figure out a better place for this or way to do auth
    # open config json to get linkedin username and pw
    config_file = open("config.json", encoding="utf-8")
    config_json = json.load(config_file)
    linkedin_username = config_json["linkedin_username"]
    linkedin_password = config_json["linkedin_password"]

    browser.get("https://linkedin.com/uas/login")
    # waiting for the page to load
    # TODO - find a way to test for elements to continue
    # --- Or make this a slightly random number in case this raises alerts
    time.sleep(2)
    # entering username
    username = browser.find_element(By.ID, "username")
    username.send_keys(linkedin_username)
    # entering password
    pword = browser.find_element(By.ID, "password")
    pword.send_keys(linkedin_password)
    # Clicking on the log in button
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    # TODO - find a way to test for elements to continue
    # --- Or make this a slightly random number in case this raises alerts
    time.sleep(2)
    browser.get(url)

    job_list = []
    # click into each job

    # scrape each job 

    # format each job date scrape to the dict
    # TODO look for the most pythonic way to do this
    return job_list


def scrape_linkedin_pages(urls: list[str]) -> list:
    """_summary_

    Args:
        url (str): _description_

    Returns:
        list: _description_
    """
    browser = setup_scraper()
    open_linkedin_search(browser=browser)

    all_jobs = []
    for url in urls:
        new_jobs = scrape_linkedin_page(browser=browser, url=url)
        # TODO add all unique new_jobs jobs to all_jobs
        all_jobs.append(new_jobs)
