from selenium import webdriver

def chk_homepage_tabs():
    driver.find_element_by_id('menu_projects').click()
    driver.find_element_by_id('menu_download').click()
    driver.find_element_by_id('menu_documentation').click()
    driver.find_element_by_id('menu_support').click()
    driver.find_element_by_id('menu_about').click()


driver = webdriver.Firefox()
driver.get('http://www.google.com')
driver.set_page_load_timeout(15)
driver.maximize_window()
driver.implicitly_wait(150)

driver.find_element_by_id('lst-ib').send_keys('Selenium Webdriver')
driver.find_element_by_name('btnK').click()
driver.implicitly_wait(1000)
driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/h3/a').click()
#if assert 'Selenium WebDriver' in driver.title:
if driver.title == 'Selenium WebDriver':
    print('You are on page: ' + driver.title)
    chk_homepage_tabs()
else:
    print('***ERROR You are on the wrong page!')

driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/h3[4]/a').click()
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/p[2]/a').click()   #Selenium Sponsors

driver.get_screenshot_as_file('GoogleOpen.png')
driver.quit()