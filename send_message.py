from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys, os
# from urllib import quote      #Uncomment line below to use python 2
from urllib.parse import quote  #Uncomment line below to use python 3 

from time import sleep
import pymysql
from selenium.webdriver.chrome.options import Options
import pathlib

import psycopg2
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager



conn = psycopg2.connect(host="ec2-23-20-208-173.compute-1.amazonaws.com",
                            port="5432",
                            user="wtgfwfsrmdtsxf",
                            password="7023c8b48035cf5f07a3a56b72e806e52cdbeb00228849038a4b4430cbfeb9b9",
                            database="d3d94oi1klcln2",
                            )
print ('Whatsapp Sending message started')


cursor = conn.cursor()
sql_read = "select phone_number from whatsapp_users where message_sent='false' order by id ASC limit 20;" # 
cursor.execute(sql_read)
rows = cursor.fetchall()
cursor.close()
conn.close()

print ('Database Connected')

phones=list()
for row in rows:
    phones.append(row[0])

css_selector = "#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text"

# message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys
msg = '''
*Musaira Deals India*
*Big Billion Day - Flipkart & Amazon Loots & Offers*

*Weekly 500 Rs. Give Away Amazon Gift Cards.*

Keep sharing & Support ❤️😊

*Join Now* Whatsapp Group Link: https://chat.whatsapp.com/EENPV5xeCofL6nzznu6vzr

*Save this number as Musaira Deals to enable above whatsapp group link*
'''   
BASE_DIR = pathlib.Path(__file__).parent.absolute()
user_data = os.path.join(BASE_DIR, "User_Data")  

mode='server'
if mode=='local':
    options = Options()
    options = webdriver.ChromeOptions()
    execute_path=r"D:\Projects\whatsapp\chromedriver.exe"
else:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    execute_path=os.environ.get("CHROMEDRIVER_PATH")
options.add_argument('--user-data-dir='+user_data)#D:\\Projects\\whatsapp\\whatsapp_automation\\User_Data')

options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
driver = webdriver.Chrome(executable_path=execute_path,options=options)
# driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
wait = WebDriverWait(driver, 600)

msg = quote(msg)  # url-encode the message, use other functios for handling dictionaries, not recommended

failed_list = []
for index, number in enumerate(phones):
    try:
        conn = psycopg2.connect(host="ec2-23-20-208-173.compute-1.amazonaws.com",
                            port="5432",
                            user="wtgfwfsrmdtsxf",
                            password="7023c8b48035cf5f07a3a56b72e806e52cdbeb00228849038a4b4430cbfeb9b9",
                            database="d3d94oi1klcln2",
                            )
        cursor = conn.cursor()
        update_sql = "UPDATE whatsapp_users SET message_sent = 'temp' WHERE phone_number = '{0}'".format(str(number))
        cursor.execute(update_sql)
        conn.commit()    
        print (f'Opening whatsapp phone url {index} and {number}')
        url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + msg
        driver.get(url)
        driver.implicitly_wait(5)
    # try:
        
        # button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='main']/footer/div/div[2]/div/div[2]/button/span")))
        button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='main']/footer/div/div/div/div[2]/div[2]/button/span")))
        driver.implicitly_wait(10)
        sleep(10)
        button.click()        
        driver.execute_script("window.onbeforeunload = function() {};")
        print (f'Sent to {index}  : {number}')
        update_sql = "UPDATE whatsapp_users SET message_sent = 'true' WHERE phone_number = '{0}'".format(str(number))
        cursor.execute(update_sql)
        conn.commit()            
    except Exception as ex:
        print("not yet")
        print(str(ex))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(exc_type, exc_tb.tb_lineno)
        print (f'Unable to Sent to {index}  : {number}')
        sleep(1)
        failed_list.append(number)

        conn = psycopg2.connect(host="ec2-23-20-208-173.compute-1.amazonaws.com",
                            port="5432",
                            user="wtgfwfsrmdtsxf",
                            password="7023c8b48035cf5f07a3a56b72e806e52cdbeb00228849038a4b4430cbfeb9b9",
                            database="d3d94oi1klcln2",
                            )
        cursor = conn.cursor()
        update_sql = "UPDATE whatsapp_users SET message_sent = 'error' WHERE phone_number = '{0}'".format(str(number))
        cursor.execute(update_sql)
        conn.commit()
    finally:
        conn.close()
        cursor.close()
        
    
    
print ("Done")

if (len(failed_list)==0):
    print (f'Message successfully sent to all {len(phones)} numbers.')
else:
    print (f'Message sent to all numbers EXCEPT:')
    for number in failed_list:
        print (number)
    
driver.quit()                                                 #uncomment to close chrome window as scoon as program ends
