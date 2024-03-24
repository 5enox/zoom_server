import subprocess
import pyautogui
import time
from datetime import datetime
import os
import logging
import random
from time import perf_counter
import time
import requests

NAME_LIST = [
    'iPhone',
    'iPad',
    'Macbook',
    'Desktop',
    'Huawei',
    'Mobile',
    'PC',
    'Windows',
    'Home',
    'MyPC',
    'Computer',
    'Android'
]

BASE_PATH = './'
CSV_PATH = os.path.join(BASE_PATH, "meetings.csv")
IMG_PATH = os.path.join(BASE_PATH, "img")
REC_PATH = os.path.join(BASE_PATH, "recordings")
AUDIO_PATH = os.path.join(BASE_PATH, "audio")
DEBUG_PATH = os.path.join(REC_PATH, "screenshots")
DISPLAY_NAME = random.choice(NAME_LIST)
################ merly a place holder replace this with working code
os.loadenv()
##############################################################
meeting_alive = True
MEETING_DURATION = os.getenv('MEETING_DURATION')
MEETING_ID = os.getenv('MEETING_ID')
MEETING_PASSWORD = os.getenv('MEETING_PASSWORD')

class BackgroundThread:

    def __init__(self, interval=):
        # Sleep interval between
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread
        thread.start()  # Start the execution

    def run(self):
        start = perf_counter()
        while meeting_alive:
            end = perf_counter()
            time = end-start
            if time > duration:
                print(f'The Zoom Recording is Done is done in {time}')
                meeting_alive = False

            


def sign_in(meet_id, password):
    logging.info("Join a meeting by ID..")
    found_join_meeting = False
    try:
        x, y = pyautogui.locateCenterOnScreen(os.path.join(
            IMG_PATH, 'join_meeting.png'), minSearchTime=2, confidence=0.9)
        pyautogui.click(x, y)
        found_join_meeting = True
    except TypeError:
        pass

    if not found_join_meeting:
        logging.error("Could not find 'Join Meeting' on screen!")
        return False

    time.sleep(2)

    # Insert meeting id
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(meet_id, interval=0.1)

    # Insert name
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(DISPLAY_NAME, interval=0.1)

    # Configure
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(10)
    pyautogui.write(password, interval=0.1)
    pyautogui.press('enter')
    time.sleep(5)
    x, y = pyautogui.locateCenterOnScreen(os.path.join(
        IMG_PATH, 'join_with_computer_audio.png'), minSearchTime=2, confidence=0.9)
    pyautogui.click(x, y)
    
def record_and_upload():
    """
    This Function Records Both The audio and the video and uploads them directly to gofile,
    retrieves the links and stores them in some live json site
    
    """
    

sign_in(MEETING_ID, MEETING_PASSWORD,)
record_and_upload()
logging.info("Signed in..")
BackgroundThread()
logging.info("Started Timer")

while meeting_alive:
    logging.info('Still Recording..')
