import os
from datetime import datetime
from selenium import webdriver

CURRENT_DIRECTORY = os.getcwd()

def archiveSite(site):
    if not os.path.exists('sites/' + site):
        os.makedirs('sites/' + site)
    dateString = datetime.now().strftime('%Y-%m-%d')
    folder = './sites/' + site + '/' + dateString
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

'''
with open('sites','r') as f:
     for site in f:
        archiveSite(site.strip())
'''

with open('repos','r') as f:
    for repo in f:
        repo = repo.strip()
        if not os.path.exists('github'):
            os.makedirs('github')
        if not os.path.exists('github/' + repo):
            os.makedirs('github/' + repo)
        os.chdir('github/' + repo)
        os.system('wget https://github.com/schollz/' + repo.strip() + '/archive/master.zip')
        os.chdir(CURRENT_DIRECTORY)
