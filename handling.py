#handlingmissing data 
# kis trha large data set me missing data ko handle kr sakte hain
 #calient se jo data lete hain usme kuch data missing hota hai  to usko handle krna prta hai 
#uske andr bht sari missing value hoti hain to usko handle krna prta hai
import pandas as pd #pands libery ko import krna prta hai ( csv files handle karta hai ,excel data ,tables,data cleaning,analysis)
import numpy as np #importnumpy as np #numberical data ko handle krta hau ( arrays ,fast calculation ,mathematical functions)
df =pd.read_csv(   #df =dataframe read_csv function se csv file ko read krta hai  csv file ko read krne ke lye read_csv function ka use krta hai  CSV commaseparated vakues ko read krta hai csv file ko read krne ke lye
    "retail_sales.csv", #reatail_sales.csv file ko read krna hai 
    parse_dates=["date"], #parse_dates parameter se date column ko date format me convert krna hai  arse_dates ye ak parameter hai  date ye ak actual columnname hai  ( mtlb csv file me date column hai usko date format me convert krna hai )
    dtype={ #dtype parameter se data type specific karna hai dtype te ak parameter hai data type specific karne ke lye data type specific karne ke lye dictionary ka use krta hai dictionary me key column name hai aur values data type hai
        "category":"category", #category column name hai usk DATA type category hai  (mtlb csv file me category column hai usko category data type me convert krna hai )
        "region":"category", #region column name hai uska data type category hai ( mtlb csv file me region column hai usko catory data type me convert krna hai )
    }
)
df.head() #df.head() function se data ke first 5 rows ko print krta hai ( mtlb csv file ke first 5 rows ko print krta hai )
df.info() #df.indo() function se data ke summary ko print krta hai (mtlb csv file ke summary ko print krta hai )
 
 #detect missing values in data 
print(df.isna().sum())    #df.isna() function se data ke missing values ko detect krta hai sum() function se missing values ke column wise count ko print krta hai (mtllb csv file ke missing values ke column wise count ko print krta hai )
# fill missing age with median ( ab hum in null values ko fill krne ke khish karege iske lye hum kuch statistics ko use kar sakte statistics ke 3 bare function  hain jaise ke mean,medium,mode etec))
df['quantity'] = pd.to_numeric(df['quantity'])
# ab in null values ko thk krne ke 2 tareke hai 
# 1st tareeka hai filing missing values with median (median se missing values ko fill krna hai )
# 2nd tareeka hai dropping missing values (mising values ko drop krna hai ) drpping missing values se data me se missing values ko remove krna hai (missing values ko data se remove krna hai)


#ab hum in null values ko fill krne ke khish karege iske lye hum kuch statistics ko use kar sakte statistics ke 
# 3 bare function  hain jaise ke mean,medium,mode etec))
# jaha pr humre pass numberical data hai waha pr hum means ya medium ka use kr sakte hai 
# jaha pr hamre pass categorical data hai waha pr hum mode ka use kr sakte hai 
# sab pr sab se phle hum jis null values ko fill kre g wo (quantity ) hum numerical data ke median ko 
