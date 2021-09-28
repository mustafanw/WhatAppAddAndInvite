import requests
url = "https://www.fast2sms.com/dev/bulk"
msg = '''
Big Billion Day Deals Whatsapp 
Join Now - https://chat.whatsapp.com/G2BXApDo9FU3UrLaFmru5K
'''
import psycopg2

conn = psycopg2.connect(host="ec2-23-20-208-173.compute-1.amazonaws.com",
                            port="5432",
                            user="wtgfwfsrmdtsxf",
                            password="7023c8b48035cf5f07a3a56b72e806e52cdbeb00228849038a4b4430cbfeb9b9",
                            database="d3d94oi1klcln2",
                            )


cursor = conn.cursor()
sql_read = "select phone_number from whatsapp_users where sms_sent='false' order by id ASC limit 20;" # 
cursor.execute(sql_read)
rows = cursor.fetchall()
cursor.close()
conn.close()

print ('Database Connected')


headers = {
'authorization': "fW2V6nQZuKastClkz3MbhSoRY98dqyHLNGI54EFUmwxTB0Jjv1afXReUsQZhLF6cVidGTwgxvDmBHlo4",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}

phones=list()
for row in rows:
    phones.append(row[0])

for index, number in enumerate(phones):

    

    try:
        conn = psycopg2.connect(host="ec2-23-20-208-173.compute-1.amazonaws.com",
                            port="5432",
                            user="wtgfwfsrmdtsxf",
                            password="7023c8b48035cf5f07a3a56b72e806e52cdbeb00228849038a4b4430cbfeb9b9",
                            database="d3d94oi1klcln2",
                            )
        cursor = conn.cursor()
        update_sql = "UPDATE whatsapp_users SET sms_sent = 'temp' WHERE phone_number = '{0}'".format(str(number))
        cursor.execute(update_sql)
        conn.commit()    
        payload = f"sender_id=FSTSMS&message="+msg+"&language=english&route=p&numbers={number}"
        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        print (f'Sent to {index}  : {number}')
        update_sql = "UPDATE whatsapp_users SET sms_sent = 'true' WHERE phone_number = '{0}'".format(str(number))
        cursor.execute(update_sql)
        conn.commit()            
    except Exception as ex:
        print("not yet")
        print(str(ex))
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(exc_type, exc_tb.tb_lineno)
        print (f'Unable to Sent to {index}  : {number}')

        conn = psycopg2.connect(host="ec2-23-20-208-173.compute-1.amazonaws.com",
                            port="5432",
                            user="wtgfwfsrmdtsxf",
                            password="7023c8b48035cf5f07a3a56b72e806e52cdbeb00228849038a4b4430cbfeb9b9",
                            database="d3d94oi1klcln2",
                            )
        cursor = conn.cursor()
        update_sql = "UPDATE whatsapp_users SET sms_sent = 'error' WHERE phone_number = '{0}'".format(str(number))
        cursor.execute(update_sql)
        conn.commit()
    finally:
        conn.close()
        cursor.close()
        
    
    
print ("Done")