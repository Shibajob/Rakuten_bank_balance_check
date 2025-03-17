
###############################
# Remarks
###############################
# Module for balance check

###############################
# Import
###############################
import logging
from Rakuten_bank_balance_check import _setup_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# Use common log settings
logger = logging.getLogger(__name__)

###############################
# Rakuten_bank_balance_check
###############################
def balance_check(driver,wait, username,password):
    try:
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "amount")))
        balance = driver.find_element(By.CLASS_NAME, "amount")
        logger.info('残高：' + balance.text)#1,889,243円
        return balance.text
    except Exception as e:
        logger.error  ("Balance check failed")
        logger.error ('=== Error Content ===')
        logger.error ('type:' + str(type(e)))
        logger.error ('args:' + str(e.args))
        logger.error ('e:' + str(e))
        raise

