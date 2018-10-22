import urllib
import json
import os
import dialogflow
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from flask import Flask
from flask import request
from flask import make_response
from sqlalchemy import *
import json
import requests


#local file untitled-3.ipynb

x1 = pd.read_excel('/Users/sai/Desktop/Zehrs.xlsx')
x2 = pd.read_excel('/Users/sai/Desktop/Zehrs.xlsx',sheet_name='Planograms in Store')
#tables are all name with table_

table_dept=x2[['Department','POG Category']] #20 Depts..456..Categories

des=x1['Article Descripton']
des1=des.str.split().str.get(0)#converted description to list and taking first element
table_brand=des1
table_brand=table_brand.drop_duplicates()
table_article_numbers=x1[['Article #','Article Descripton']]
table_article_numbers['Article Descripton'][0]='$10 BREADED SWISS CHKN BREAST'
table_planograms=x1['Planogram Name'].drop_duplicates()
table_Category=x1['POG Category'].drop_duplicates()
table_departments=x2['Department'].drop_duplicates()

#some processing to have categories department wise

new=x2[x2['Department']=='Meat']
new1=x2[x2['Department']=='Grocery']
new3=x2[x2['Department']=='HBC']
new4=x2[x2['Department']=='Home']
new5=x2[x2['Department']=='Natural Foods']
new6=x2[x2['Department']=='Produce']
new7=x2[x2['Department']=='Bakery']
new8=x2[x2['Department']=='Apparel']
new9=x2[x2['Department']=='Bulk']
new10=x2[x2['Department']=='Dairy']
new11=x2[x2['Department']=='Frozen']
new12=x2[x2['Department']=='Seafood']
new13=x2[x2['Department']=='Pharmacy']
new14=x2[x2['Department']=='HMR']
new15=x2[x2['Department']=='Front End']
new16=x2[x2['Department']=='Deli']
new17=x2[x2['Department']=='Tobacconists']
new18=x2[x2['Department']=='Cosmetics']



table_dept_meat=new[['POG Category','Department']]
table_dept_grocery=x2[x2['Department']=='Grocery']
table_dept_grocery=table_dept_grocery[['POG Category','Department']]
table_dept_hbc=new3[['POG Category','Department']]
table_dept_Home=new4[['POG Category','Department']]
table_dept_Natural_Foods=new5[['POG Category','Department']]
table_dept_Produce=new6[['POG Category','Department']]
table_dept_Bakery=new7[['POG Category','Department']]
table_dept_Apparel=new8[['POG Category','Department']]
table_dept_Bulk=new9[['POG Category','Department']]
table_dept_Dairy=new10[['POG Category','Department']]
table_dept_Frozen=new11[['POG Category','Department']]
table_dept_Seafood=new12[['POG Category','Department']]
table_dept_Pharmacy=new13[['POG Category','Department']]
table_dept_HMR=new14[['POG Category','Department']]
table_dept_Front_End=new15[['POG Category','Department']]
table_dept_Deli=new16[['POG Category','Department']]
table_dept_Tobacconists=new17[['POG Category','Department']]
table_dept_Cosmetics=new18[['POG Category','Department']]

#tables look good. each and every department has its own tables
#tables look good
