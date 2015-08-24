import os
from datetime import datetime
from selenium import webdriver

CURRENT_DIRECTORY = os.getcwd()

def archiveSite(site):
    if not os.path.exists('output/' + site):
        os.makedirs('output/' + site)
    dateString = datetime.now().strftime('%Y-%m-%d')
    folder = './output/' + site + '/' + dateString
    if not os.path.exists(folder):
        os.makedirs(folder)
    os.chdir(folder)
    os.system('wget --recursive --no-clobber --page-requisites --html-extension --convert-links --restrict-file-names=windows ' + site)
    os.system('mv ' + site + '/* ./')
    os.system('rm -rf ' + site)
    browser = webdriver.Firefox()
    browser.get('http://' + site)
    browser.save_screenshot('screenshot.png')
    browser.quit()
    os.chdir(CURRENT_DIRECTORY)

with open('sites','r') as f:
	for site in f:
		archiveSite(site.strip())

