import sqlite3
import pandas as pd
con = sqlite3.connect(r"C:\Users\VARUN\Desktop\flipkart\mydata.db")

import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Data sheet')

sheet1.write( 0,1, 'Title')
sheet1.write( 0,2, 'Product Rating')
sheet1.write( 0,3, 'Seller Name')
sheet1.write( 0,4, 'Seller Rating')
sheet1.write( 0,5, 'Contact Number')


#con = sqlite3.connect(r"C:\Users\VARUN\Desktop\flask\Web Scraper\Webscrape\Webscrape\mydata.db")
cur = con.cursor()
cur.execute("SELECT * FROM data_tb")
data = cur.fetchall()
#print(data)


z=1 
for i in data:
        sheet1.write(z, 1, data[z-1][0])
        sheet1.write(z, 2, data[z-1][1])
        sheet1.write(z, 3, data[z-1][2])
        sheet1.write(z, 4, data[z-1][3])
        sheet1.write(z, 5, data[z-1][4])
        z=z+1
        wb.save('Data.xls')
#sql_query = pd.read_sql_query ('''
#                               SELECT
#                               *
#                               FROM data_tb
#                              ''', con)

#df = pd.DataFrame(sql_query, columns = ['Title', 'Author', 'Paragraph'])
#print (df)
