# web-archiver
A tiny Python clone of https://archive.org/web/ for your own personal websites.

To use simply install

```
$ pip install -r requirements.txt
```

and then add your sites into the file ```sites```. Then to run just used

```
$ python run.py
```

To check out your files, goto the ```output``` directory and use

```
$ python3 -m http.server
```

# To-do

- Archive site with ```wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows --domains DOMAIN.COM  http://DOMAIN.COM/ with date```
- Take screenshot with
```
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.google.com/')
browser.save_screenshot('screenshot.png')
browser.quit()
```
- Generate site to be able to traverse the sites easily. Index page for all pages. One index page for each web archive with screenshots/dates that take you to the actual page.
