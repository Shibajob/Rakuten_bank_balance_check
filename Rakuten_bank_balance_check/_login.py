
###############################
# Remarks
###############################
# Module for AU Jibun Bank login

###############################
# Import
###############################
import logging
import time
from Rakuten_bank_balance_check import _setup_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Use common log settings
logger = logging.getLogger(__name__)

###############################
# Rakuten_bank_login
###############################
def Rakuten_bank_login(driver, wait, username, password, branch_number, account_number, secret_word_list):
    try:
        logger.info('Enter your login information.')
        driver.find_element(By.NAME, 'LOGIN:USER_ID').clear()
        driver.find_element(By.NAME, 'LOGIN:LOGIN_PASSWORD').clear()
        driver.find_element(By.NAME, 'LOGIN:USER_ID').send_keys(username)
        driver.find_element(By.NAME, 'LOGIN:LOGIN_PASSWORD').send_keys(password)
        driver.find_element(By.CLASS_NAME, "btn-login01").click()
        logger.info('Clicked on the login button.')
        # Processing branching by additional password
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, 'INPUT_FORM:INPUT_BRANCH_CODE')))
        except Exception:
            logger.info('No additional password was asked.')
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "amount")))
            logger.info('Login completed.')
            return True
    except Exception as e:
        logger.error ('login failed.')
        logger.error ('=== Error Content ===')
        logger.error ('type:' + str(type(e)))
        logger.error ('args:' + str(e.args))
        logger.error ('e:' + str(e))
        raise

    # additional password
    try:
        # Branch number
        driver.find_element(By.NAME, 'INPUT_FORM:INPUT_BRANCH_CODE').clear()
        driver.find_element(By.NAME, 'INPUT_FORM:INPUT_BRANCH_CODE').send_keys(int(branch_number))
        # Account Number
        driver.find_element(By.NAME, 'INPUT_FORM:INPUT_ACCOUNT_NUMBER').clear()
        driver.find_element(By.NAME, 'INPUT_FORM:INPUT_ACCOUNT_NUMBER').send_keys(int(account_number))
        # watchword
        secret_word_driver = driver.find_element(By.CSS_SELECTOR, 'p.c00.margintop20.large.marginleft20pc')
        logger.info(secret_word_driver.text)

        driver.find_element(By.NAME, 'INPUT_FORM:SECRET_WORD').clear()
        driver.find_element(By.NAME, 'INPUT_FORM:SECRET_WORD').send_keys(secret_word_list[secret_word_driver])

        time.sleep(5)
        driver.find_element(By.ID, "INPUT_FORM:j_id_28").click()
        logger.info('認証ボタンクリックしました。')
        logger.info('楽天銀行ログイン完了しました。')

    except Exception as e:
        logger.error ('認証に失敗しました。')
        logger.error ('=== エラー内容 ===')
        logger.error ('type:' + str(type(e)))
        logger.error ('args:' + str(e.args))
        logger.error ('e自身:' + str(e))

if __name__ == '__main__':
    print(list[0])
