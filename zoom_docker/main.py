import pyautogui
import time
import os
import logging
import random
import time
import requests
from dotenv import load_dotenv

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
DISPLAY_NAME = random.choice(NAME_LIST)

BASE_PATH = './'
CSV_PATH = os.path.join(BASE_PATH, "meetings.csv")
IMG_PATH = os.path.join(BASE_PATH, "img")
# Load environment variables from .env file
load_dotenv()
##############################################################
meeting_alive = True
MEETING_DURATION = os.getenv('MEETING_DURATION')
MEETING_ID = os.getenv('MEETING_ID')
MEETING_PASSWORD = os.getenv('MEETING_PASSWORD')


def upload_to_gofile(file_path):
    url = 'https://api.gofile.io/servers'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        first_server_name = data['data']['servers'][0]['name']
        url = f'https://{first_server_name}.gofile.io/contents/uploadfile'
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files,)
        data = response.json()
        return data['data']['downloadPage']
    else:
        print("Error:", response.status_code)
        return None


def sign_in(meet_id, password):
    logging.info("Join a meeting by ID..")
    found_join_meeting = False
    try:
        result = pyautogui.locateCenterOnScreen(os.path.join(
            IMG_PATH, 'join_meeting.png'), minSearchTime=2, confidence=0.9)
        if result is not None:
            x, y = result
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
    result = pyautogui.locateCenterOnScreen(os.path.join(
        IMG_PATH, 'join_with_computer_audio.png'), minSearchTime=2, confidence=0.9)
    if result is not None:
        x, y = result
        pyautogui.click(x, y)


sign_in(MEETING_ID, MEETING_PASSWORD,)
logging.info("Signed in..")
logging.info("Started Timer")

while meeting_alive:
    logging.info('Still Recording..')
