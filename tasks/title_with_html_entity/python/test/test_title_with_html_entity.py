from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://www.wordpress.org")
title_actual = driver.title.encode('ascii', 'xmlcharrefreplace')
title_expected = 'Blog Tool, Publishing Platform, and CMS &#8212; WordPress'
assert title_expected == title_actual
driver.close()
