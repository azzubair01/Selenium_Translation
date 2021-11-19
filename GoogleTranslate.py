import os
import time
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Give Language code in which you want to translate the text:=>
source_lang = 'en'
dest_lang = 'ms'

# Read Doc files
input_path = '.\\docs'
dir_list = os.listdir(input_path)

# Define Output folder
output_path = '.\\output'
if not os.path.exists(output_path):
    os.mkdir(output_path)

# Iterate translation over Docs files
translated_inputs = []
for i in tqdm(range(len(dir_list))):
    # launch browser with selenium:=>
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation', 'disable-popup-blocking'])
    browser = webdriver.Chrome(options=options)
    # browser = webdriver.Chrome('path of chromedriver.exe file') if the chromedriver.exe is in different folder

    with open(input_path + '\\' + dir_list[i], 'r') as file:
        text = file.read()

    # copy google Translator link here:=>
    browser.get("https://translate.google.com.my/?sl="+source_lang+"&tl="+dest_lang+"&text="+text+"&op=translate")

    # just wait for some time for translating input text:=>
    # time.sleep(0.5)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]'))).text

    # Given below x path contains the translated output that we are storing in output variable:=>
    output1 = browser.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]').text

    with open(output_path + '\\' + dir_list[i], 'w') as file:
        file.write(output1)

    # Display the output:=>
    # print("Translated Paragraph:=> " + output1)

    # Quit the browser
    browser.quit()
