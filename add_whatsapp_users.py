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
a='<span title="+1 (209) 286-6705, +1 (331) 444-0164, +1 (423) 414-2278, +1 (504) 229-0564, +1 (507) 320-4672, +1 (509) 651-1103, +1 (562) 473-6604, +1 (587) 418-3452, +1 (762) 338-4025, +1 (838) 444-0158, +1 (972) 750-3003, +20 111 364 1313, +212 613-911470, +225 05 37 99 27, +229 98 20 60 30, +234 704 638 3094, +234 805 472 0108, +234 810 034 7660, +234 811 352 5942, +234 812 989 0004, +234 904 604 4679, +234 912 379 0856, +237 6 51 47 07 25, +263 78 552 3489, +380 99 263 2918, +880 1709-601719, +880 1793-449811, +91 6201 515 035, +91 6201 891 830, +91 6202 199 035, +91 6239 438 244, +91 6260 204 147, +91 6261 142 436, +91 6261 724 008, +91 6307 525 975, +91 6350 085 461, +91 6350 464 783, +91 6350 590 412, +91 6352 589 192, +91 6353 121 692, +91 6353 252 460, +91 6354 278 181, +91 6362 605 873, +91 6367 196 893, +91 6370 748 296, +91 6375 056 931, +91 6375 351 332, +91 6376 126 186, +91 6377 236 145, +91 6397 445 109, +91 6397 999 540, +91 70064 41232, +91 70240 62837, +91 70248 04576, +91 70452 97998, +91 70465 59898, +91 70585 04826, +91 70653 26478, +91 70677 54071, +91 70897 43630, +91 70926 38169, +91 72043 91921, +91 72068 52706, +91 72182 57453, +91 72328 85181, +91 73105 20220, +91 73106 58971, +91 73199 75202, +91 73397 11007, +91 73553 46687, +91 74250 28403, +91 74628 90055, +91 74658 08349, +91 74799 44137, +91 74800 79310, +91 74881 41600, +91 74886 45660, +91 74960 23536, +91 74978 52875, +91 74980 70103, +91 75203 94805, +91 75440 83132, +91 75687 23024, +91 75868 98213, +91 75994 95304, +91 76071 87799, +91 76075 91152, +91 76312 48917, +91 76790 90801, +91 76973 85817, +91 76984 03893, +91 77387 64455, +91 77430 72455, +91 77510 14808, +91 77749 76771, +91 77809 52725, +91 78048 27852, +91 78286 08269, +91 78289 00143, +91 78802 19845, +91 78882 45513, +91 79085 05830, +91 79847 80449, +91 79889 46953, +91 80533 36557, +91 80566 87707, +91 80827 96640, +91 81021 44142, +91 81163 32885, +91 81265 54367, +91 81296 26301, +91 81305 60165, +91 81418 58769, +91 81419 93171, +91 81716 46010, +91 81977 06985, +91 82188 56131, +91 82207 25920, +91 82309 17334, +91 82659 74981, +91 83054 62819, +91 83094 21155, +91 83208 05993, +91 83208 87813, +91 83471 17544, +91 83608 57814, +91 84348 70896, +91 84455 91767, +91 85113 49224, +91 85286 34198, +91 85286 51019, +91 85293 21025, +91 85719 61277, +91 85859 96049, +91 85878 32218, +91 85955 80200, +91 87418 45327, +91 87974 67589, +91 88084 16243, +91 88096 76269, +91 88227 35844, +91 88372 27632, +91 88825 36352, +91 88829 47521, +91 88879 55691, +91 88953 10542, +91 89020 54687, +91 89049 19458, +91 89378 03505, +91 89482 00569, +91 89532 61856, +91 89553 17606, +91 89796 90989, +91 90014 40678, +91 90243 47072, +91 90414 55494, +91 90609 69569, +91 90840 52460, +91 91427 88089, +91 91428 13423, +91 91651 22308, +91 91792 04435, +91 91987 96721, +91 92642 71694, +91 93116 01546, +91 93255 80916, +91 93594 92346, +91 94006 16122, +91 94112 47901, +91 94490 04157, +91 95104 19030, +91 95116 18087, +91 95409 17249, +91 95488 25403, +91 95540 28861, +91 95829 18308, +91 96308 16837, +91 96750 20407, +91 96927 02013, +91 97175 21795, +91 97232 13614, +91 97323 72144, +91 97832 34957, +91 97995 20909, +91 98123 36262, +91 98252 15704, +91 98773 15523, +91 98895 45468, +91 98902 91899, +91 99328 88884, +91 99539 13461, +91 99834 94919, +92 301 9333821, +92 303 0389574, +92 307 9906729, +92 316 9815293, +92 318 2368060, +92 318 5559187, +92 321 5687846, +92 322 4899630, +92 333 5701492, +92 340 3613067, +92 342 9681100, +92 347 1419630, +92 348 3417978, +93 70 464 4695, +93 76 740 9328, +966 50 378 2955, +967 712 781 653, +967 717 322 333, +967 737 989 120, +967 775 926 949, +967 776 190 694, +971 54 718 0347, +994 40 068 38 89, +994 40 202 35 38, +994 40 258 74 63, +994 40 269 48 57, +994 40 381 12 38, +994 40 840 02 35"</span>'
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
