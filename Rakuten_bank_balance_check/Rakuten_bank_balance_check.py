"""Main module."""

###############################
# Remarks
###############################
# Module for creating and deleting folders for user profiles

###############################
# Import
###############################
import os
import logging
from Rakuten_bank_balance_check import _setup_logger
from Rakuten_bank_balance_check import _userprofilefolder as userprofilefolder
from Rakuten_bank_balance_check import _login as login
from Rakuten_bank_balance_check import _balance_check as balance_check
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Use common log settings
logger = logging.getLogger(__name__)

###############################
# Parameters
###############################
MAX_RETRIES = 3

CURRENT_DIR_PATH = os.path.dirname(__file__)
USER_PROFILE_PATH = CURRENT_DIR_PATH + r'\userdata'
DRIVER_PATH = CURRENT_DIR_PATH + r'\driver'
URLPATH = 'https://fes.rakuten-bank.co.jp/MS/main/RbS?CurrentPageID=START&&COMMAND=LOGIN'

#Chrome Options
options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--no-sandbox')
options.add_argument('--lang=ja')
options.add_argument('--user-data-dir=' + USER_PROFILE_PATH)
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument('--start-maximized')
#options.add_argument('--headless')
options.add_argument("--disable-popup-blocking")  

###############################
# Termination process
###############################
def Process_Exit(flag, balance = ''):
    # User profile folder deletion process
    userprofilefolder.userprofilefolder_remove(USER_PROFILE_PATH)

    if(flag == 'true'):
        logger.info ('successful termination')
        return balance
    else:
        logger.error ('abnormal termination')
        raise('abnormal termination')

###############################
# Main
###############################
def Rakuten_bank_balance_check(username, passwd, branch_number, account_number, secret_word_list):
    logger.info ('===Start===')
    # If the username or password value is invalid, the process will terminate.
    if username is None or passwd is None or str(username).strip() == "" or str(passwd).strip() == "":
        logger.error ('The username or password value is invalid.')
        Process_Exit('fail')
    userprofilefolder.userprofilefolder_create(USER_PROFILE_PATH)

    # Chrome Start
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.get(URLPATH)
        logger.info ('Chrome Start')
    except Exception as e:
            logger.error ('Chrome fails to start')
            logger.error ('=== Error Content ===')
            logger.error ('type:' + str(type(e)))
            logger.error ('args:' + str(e.args))
            logger.error ('e:' + str(e))
            Process_Exit('fail')

    # Web page transition timeout
    wait = WebDriverWait(driver, 5)

    try:
        login.Rakuten_bank_login(driver, wait, username, passwd, branch_number, account_number, secret_word_list)
    except Exception:
        driver.quit()
        Process_Exit('fail')

    try:
        balance = balance_check.balance_check(driver, wait, username, passwd)
        driver.quit()
        Process_Exit('true', balance)
    except Exception:
        driver.quit()
        Process_Exit('fail')

if __name__=="__main__":
    username = "test"
    passwd = "test"
    branch_number = "test"
    account_number = "test"
    secret_word_list = {
    '出身地は？（例：とうきょうとしながわく）':'test',
        '卒業した小学校は？（例：ひがししょうがっこう）':'test',
        '卒業した中学校は？（例：だいいちちゅうがっこう）':'test',
        '母親の旧姓は？':'test',
        '父親の出身地は？（例：とうきょうとしながわく）':'test',
        '兄弟・姉妹の名前は？':'test',
        '学生時代に所属したクラブ・サークルは？（例：すいそうがくぶ）':'test',
        '初めて飼ったペットの名前は？':'test',
        '所有している車は？':'test',
        '初めて訪れた海外の国は？（例：おーすとらりあ）':'test',
        '初めて買った曲のタイトルは？':'test',
        '最も好きな映画は？':'test'
    }
    Rakuten_bank_balance_check(username, passwd, branch_number, account_number, secret_word_list)
    