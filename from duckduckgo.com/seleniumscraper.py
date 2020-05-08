from selenium.webdriver import Chrome


browser = Chrome('/web-scrapers/chromedriver_win32/chromedriver.exe')

browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('python')
search_form.submit()

results = browser.find_elements_by_class_name('result')
print(results[0].text)

browser.close()
quit()
