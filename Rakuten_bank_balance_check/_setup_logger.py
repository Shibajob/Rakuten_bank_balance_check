
###############################
# Remarks
###############################
# Logger setup module

###############################
# Import
###############################
import logging
import os

###############################
# Parameters
###############################
CURRENT_DIR_PATH = os.path.dirname(__file__)

###############################
# Setup logger
###############################
def setup_logger():
    # ロガーの設定
    logfilename = CURRENT_DIR_PATH + r'/log.log'
    log_level = logging.INFO

    # フォーマッターの設定
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    # ファイルハンドラーの設定
    log_file_handler = logging.FileHandler(logfilename , mode = 'w')
    log_file_handler.setLevel(logging.DEBUG)
    log_file_handler.setFormatter(log_format)

    # コンソールハンドラーの設定
    log_console_handler = logging.StreamHandler()
    log_console_handler.setLevel(logging.INFO)
    log_console_handler.setFormatter(log_format)

    logging.basicConfig(filename=logfilename, level=log_level, format=log_format)

setup_logger()
