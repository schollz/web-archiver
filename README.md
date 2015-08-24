# web-archiver
A tiny Python clone of https://archive.org/web/ for your own personal websites.

# To-do

1. Archive site with ```wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains DOMAIN.COM  http://DOMAIN.COM/ with date```
2. Take screenshot with
```
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.google.com/')
browser.save_screenshot('screenie.png')
browser.quit()
```
3. Generate site to be able to traverse the sites easily
