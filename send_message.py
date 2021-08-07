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

print ('Whatsapp Sending message started')

db = pymysql.connect("remotemysql.com","oCtHbs37t9","Ifvu2JOuDf","oCtHbs37t9",charset='utf8' )
cursor = db.cursor()
sql_read = "select phone_number from whatsapp_users where message_sent='false' order by id DESC limit 20;"
cursor.execute(sql_read)
rows = cursor.fetchall()

print ('Database Connected')

phones=list()
for row in rows:
    phones.append(row[0])

# %%from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()

#update css selector if you have any issues
css_selector = "#main > footer > div._3ee1T._1LkpH.copyable-area > div._3uMse > div > div._3FRCZ.copyable-text.selectable-text"

# message to be sent to everyone, you can also read it as a dict from a file with ph nos as keys
msg = '''
*Musaira Deals*
Join this group for everyday deals, sale and loots across multiple Online Shopping Websites.
So no need to check multiple websites. Just join this group and you are good to go to grab all the latest deals.

*Weekly 500 Rs. Give Away Amazon Gift Cards.*

Keep sharing & Support ❤️😊
Whatsapp: https://chat.whatsapp.com/G2BXApDo9FU3UrLaFmru5K

*Save this number as Musaira Deals to enable above whatsapp group link*
'''   
BASE_DIR = pathlib.Path(__file__).parent.absolute()
user_data = os.path.join(BASE_DIR, "User_Data")  
# execute_path=r"D:\Projects\whatsapp\chromedriver.exe"

# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument('--user-data-dir=D:\\Projects\\whatsapp\\add_User_Data')#D:\\Projects\\whatsapp\\whatsapp_automation\\User_Data')
# options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
# driver = webdriver.Chrome(executable_path=execute_path,options=options)
# wait = WebDriverWait(driver, 10)
mode='server'
if mode=='local':
    options = Options()
    options = webdriver.ChromeOptions()
    # options.headless = True
    # execute_path=r"D:\Projects\whpip install chromedriver-binary-autoatsapp\whatsapp_automation\chromedriver.exe"
    execute_path=r"D:\Projects\chromedriver.exe"
else:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    execute_path=os.environ.get("CHROMEDRIVER_PATH")
options.add_argument('--user-data-dir='+user_data)#D:\\Projects\\whatsapp\\whatsapp_automation\\User_Data')
# options.add_argument('window-size=1200x600')    
options.add_argument("user-agent=User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")
driver = webdriver.Chrome(executable_path=execute_path,options=options)
wait = WebDriverWait(driver, 600)

msg = quote(msg)  # url-encode the message, use other functios for handling dictionaries, not recommended
# driver.get("https://web.whatsapp.com")  # first call without delay in order to scan qr code
# sleep(2)
failed_list = []
for index, number in enumerate(phones):
    print (f'Opening whatsapp phone url {index} and {number}')
    url = "https://web.whatsapp.com/send?phone=91" + number + "&text=" + msg
    driver.get(url)
    driver.implicitly_wait(5)
    sleep(3)  # any delay is okay, even 0, but 3-5 seems appropriate
    # for i in range(TRIES):
    try:
        button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='main']/footer/div/div[2]/div/div[2]/button/span")))
        driver.implicitly_wait(10)
        sleep(10)
        button.click()        
        # driver.find_element_by_xpath("//div[@id='main']/footer/div/div[3]/button/span").click()
        # driver.find_element_by_css_selector(css_selector).send_keys(Keys.RETURN)
        driver.execute_script("window.onbeforeunload = function() {};")
        print (f'Sent to {index}  : {number}')
        update_sql = "UPDATE whatsapp_users SET message_sent = 'true' WHERE phone_number = {0}".format(number)
        cursor.execute(update_sql)
        db.commit()
        
        
    except Exception as ex:
        print("not yet")
        print(str(ex))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(exc_type, exc_tb.tb_lineno)
        print (f'Unable to Sent to {index}  : {number}')
        sleep(1)
        failed_list.append(number)
        
    # else:
    #     failed_list.append(number)
    
print ("Done")

if (len(failed_list)==0):
    print (f'Message successfully sent to all {len(phones)} numbers.')
else:
    print (f'Message sent to all numbers EXCEPT:')
    for number in failed_list:
        print (number)
    
driver.quit()                                                 #uncomment to close chrome window as scoon as program ends
