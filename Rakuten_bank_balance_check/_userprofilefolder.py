
###############################
# Remarks
###############################
# Module for creating and deleting folders for user profiles

###############################
# Import
###############################
import sys
import os
import logging
from Rakuten_bank_balance_check import _setup_logger
import shutil
import time

# Use common log settings
logger = logging.getLogger(__name__)

###############################
# Parameters
###############################
MAX_RETRIES = 3

###############################
# User profile creation
###############################
def userprofilefolder_create(userprofile_path):
    try:
        os.mkdir(userprofile_path)
        logger.info("User profile created.")
    except Exception:
        logger.info("Failed to create user profile.")

###############################
# User profile deletion
###############################
def userprofilefolder_remove(userprofile_path):
    for attempt in range (1,MAX_RETRIES +1):
        try:
            if os.path.exists(userprofile_path):
                shutil.rmtree(userprofile_path)
            logger.info('The user profile has been deleted.')
            break
        except Exception as e:
            logger.error ('The user profile could not be deleted.')
            logger.error (f'{attempt}th failed deletion attempt : {e}')
            if attempt < MAX_RETRIES:
                time.sleep (5)
            else:
                break

###############################
# Test
###############################
if __name__=="__main__":
    current_dir_path = os.path.dirname(sys.argv[0])
    userprofile_path = current_dir_path + r'\userdata'
    print(current_dir_path)
    #userprofilefolder_create(userprofile_path)
    #userprofilefolder_remove(userprofile_path)
