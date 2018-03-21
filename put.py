import sqlite3
connection = sqlite3.connect("myTable.db")
# cursor 
crsr = connection.cursor()
 
# SQL command to create a table in the database


# sql_command="drop table HOSPITAL_RECORD"
# crsr.execute(sql_command)


line_list=[]
with open('ip.txt','r')as file_handle:
	for line in file_handle:

		line=line.strip()
		line_list.append(line)
sql_command=""" CREATE TABLE HOSPITAL_RECORD (
year integer,
hosp int
);"""
# sql_command=""" CREATE TABLE HOSPITAL_RECORD (
# year integer,
# hosp int,
# net_rev int,
# nat_real_gdp int,
# wa_real_gdp int,
# wa_unemployment float,
# wa_median_income float,
# WAHealthcareExpPerCap int,
# us_defense_budget int,
# hosp_name varchar(30),
# critical_access int
# );"""
crsr.execute(sql_command)
for item in line_list:
    # print("%r"), % (tuple(line_list),))
    item_list=item.split('\t')
    var_string = ', '.join(item_list)
    # query_string = 'INSERT INTO HOSPITAL_RECORD VALUES (%s);' % var_string
    # print(query_string)
    # year=item_list[0]
    # hosp=item_list[1]
    # net_rev=item_list[2]
    # nat_real_gdp=item_list[3]
    # wa_unemployment=item_list[4]
    # wa_median_income=item_list[5]
    # WAHealthcareExpPerCap=item_list[6]
    # us_defense_budget=item_list[7]
    # hosp_name=item_list[8]
    # critical_access=item_list[9]

    year=item_list[0]
    hosp=item_list[1]
    insertstmt=("insert into HOSPITAL_RECORD (year, hosp) values ('%s', '%s')" % (year, hosp))


    crsr.execute(insertstmt)



 

 
# To save the changes in the files. Never skip this. 
# If we skip this, nothing will be saved in the database.
connection.commit()

# close the connection
connection.close()
