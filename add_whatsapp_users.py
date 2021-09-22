import ast
import pymysql

import psycopg2

conn = psycopg2.connect(host="ec2-23-20-208-173.compute-1.amazonaws.com",
                            port="5432",
                            user="wtgfwfsrmdtsxf",
                            password="7023c8b48035cf5f07a3a56b72e806e52cdbeb00228849038a4b4430cbfeb9b9",
                            database="d3d94oi1klcln2",
                            )
sql='create table if NOT EXISTS whatsapp_users( id serial, phone_number character varying primary key, message_sent character varying);'
cur = conn.cursor()
# cur.execute(sql)
# conn.commit()
# cur.close()
a='<span title="+919822207304, +1 (346) 401-3462, +1 (347) 325-2646, +1 (416) 807-5253, +1 (437) 972-5152, +1 (479) 544-5374, +1 (503) 432-9108, +1 (639) 539-0786, +1 (647) 287-8295, +1 (732) 543-3052, +1 (857) 233-6913, +1 (857) 869-4172, +256 701 215253, +44 7557 919053, +91 70304 44136, +91 72760 53452, +91 73870 00252, +91 73874 86776, +91 74062 95253, +91 75074 78663, +91 75668 85799, +91 77091 78653, +91 77570 25994, +91 78759 60717, +91 80552 03720, +91 80556 56257, +91 80874 24348, +91 80877 78653, +91 81034 54200, +91 81096 76321, +91 83059 66372, +91 83906 55153, +91 84549 36026, +91 84601 34321, +91 84694 61348, +91 85548 78700, +91 86000 35756, +91 86025 18172, +91 87664 77260, +91 87697 12776, +91 88062 82257, +91 88662 64474, +91 88667 18140, +91 88677 99921, +91 88909 86196, +91 89567 05201, +91 89567 94652, +91 89897 02972, +91 90166 06898, +91 90283 21822, +91 90284 30969, +91 90287 41152, +91 90296 09323, +91 90334 43261, +91 90879 40452, +91 90960 34468, +91 90966 90847, +91 91589 09053, +91 91679 98097, +91 92736 08072, +91 92841 25796, +91 93293 88334, +91 93297 16552, +91 93729 12342, +91 94089 73369, +91 94287 81996, +91 94624 74170, +91 95032 69552, +91 95034 16254, +91 96375 75651, +91 96499 30981, +91 96533 98790, +91 96658 40267, +91 97240 84088, +91 97247 41384, +91 97635 86951, +91 97655 92160, +91 97660 22545, +91 97661 88032, +91 97682 20105, +91 98199 19602, +91 98209 33057, +91 98215 53752, +91 98226 08169, +91 98235 92128, +91 98240 25752, +91 98269 32974, +91 98336 40028, +91 98337 71627, +91 98341 85250, +91 98819 02256, +91 98908 15248, +91 98921 45472, +91 98926 60421, +91 99041 64851, +91 99133 70052, +91 99208 95352, +91 99701 74852, +91 99704 99252, +91 99749 20449, +91 99980 15291, +965 9409 0552, +971 54 432 2753"</span>'
a=a.replace('<span title="',"")
a=a.replace('"</span>','')
a=a.replace(' ','')
a=a.replace(',You','')
a=a.replace(',','","')
a=a.replace('+91','')
a=a.replace('class="_3Id9P_1VzZY">',',"')
a='["'+a+'"]'
a=ast.literal_eval(a)
print(a)
users=list()
for user in a:
    if "+" in user:
        pass
    else:
        users.append((user,"false"))

sql='INSERT INTO whatsapp_users(phone_number,message_sent) VALUES(%s,%s) ON CONFLICT DO NOTHING'
cur.executemany(sql, users)
conn.commit()
cur.close()
# print(users)
# db = pymysql.connect("remotemysql.com","oCtHbs37t9","Ifvu2JOuDf","oCtHbs37t9",charset='utf8' )
# cursor = db.cursor()
# cursor.executemany("""INSERT IGNORE INTO whatsapp_users(phone_number,message_sent) VALUES(%s,%s)""", users)
# db.commit()
#create table if NOT EXISTS whatsapp_users( id int AUTO_INCREMENT NOT null, phone_number VARCHAR(100) UNIQUE NOT NULL, message_sent VARCHAR(50),primary key (id));
