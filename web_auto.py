from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://youtube.com")

searchbox=driver.find_element_by_name("search_query")
searchbox.send_keys("ashish chanchlani vines")

searchButton=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
searchButton.click()
print(" Web Automation is done successfully ")


