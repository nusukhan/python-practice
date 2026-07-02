#descriptive stats & data distribution hum pandas ke data set main kaam kr rhe hai  or uske lye hum panadas ke dataframe ko use kr rhe hai 
# ab hum kuch  statistic anaysis ke bay kre g jis ke zarye se hum apn data ke sense banne ke khish kre g or ye verify kre g ke hamra data set sahi hai uske lye hum python ke kuch function ke use kre g  
#key function for descriptive statistics ye hume kuch basic statistic ke bare main batata hai 
#df.describe() or descriptive statistics ye hume kuch basic statistic ke bare main batata hai 
#df['col'].value_counts() #value count ye hume data ke unique value ko count kr ke deta hai 
#df.quantile(q) #quantile hamre dataset  ko equal set of probability main divide kr deta hai usally hum 4 quantile use krte hai jisme se 25%,50%,75%ke value ko calculate krte hai or har portion main 25% data hota hai 
#  skewness operator ke zarye se hum apne data ke skewness ko calculate kr sakte hai ke hamra dataset right or left side skewed hai ya nahi skewness ke value 0 ke barabar hone par data perfectly symmetric hota hai agar skewness ki value positive hoti hai to data right skewed hota hai aur agar negative hoti hai to data left skewed hota hai
#kurtosis nikl kr kurtosis anaysis bhe kr sakte hai 
#loaddataset() 
import pandas as pd # panadas library ko import kr rhe hai 

df =pd.read_csv( #csv file ko read kr rhe hai  (mtlb df dataframe main csv file ko load kr rhe hai )
    "ecommerce_sales_analysis_5000.csv",#csv file ka name hai jisko hum load kr rhe hai 
    parse_dates=["order_dates"] # is main jo order_dates hai usko date format main convert kr dega parse_dates ke zarye se
)

df.shape  #verify dataset before anaysis #df.shape mtlb df dataframe ke shape ko batata hai yani ke kitni rows or column  hai  

#core descriptive statistics 
df.describe() #ye hume data ke bsic statistic ke bare main batata hai 

df[["unit-price","revenue"]].describe() #for revevue values df dataframe main se unit_price or revenue ke basic statistic ke bare main batata hai 

#quantiles 
df["revenue"].quantile([0.25,0.5,0.75]) # hum revenue ke phle 3 quantiles ko calculate kr rhe hai quantile ka function use kr k ye built_in function hai pandas ka 

#skewness
df["revenue"].mean(),df["revenue"].median() #yaha hum apne data ke mean or median ko calculate kr rhe hai skewness ke lye 

df["revenue"].skew() #skewness ke function se hum data ke dkewness nikle sakte hai  #positive value right skewed data ko indicate krta hai .skewness ke zarye se hum apne data ke skewness ko calculate kr sakte hai ke hamra dataset right or left side skewed hai ya nahi skewness ke value 0 ke barabar hone par data perfecttly symmetric hota hai agar skewness ki value positive hoti hai to data right skewed hoti hai aur agar negative hoti hai to data left skewed hota hai 

#category-level descriptive statistics
df.groupby("product_category")["revenue"].describe() #groupby ke xzarye se hum apne data ke product_category ke hisab se revenue ke basic statistic ke bare main batata hai 
 
df.groupby("product_category")["revenue"].mean()  #group wise mean nikal kr category ke hisab se revenue ke average ko calculate kr rhe hai 

#using IQR to undertand spread of data or outliers
Q1 =df["revenue"].quantile(0.25) #first quantile ko calcolate kr rhe hai 
Q3 =df["revenue"].quantile(0.75) #third quantile ko calculate kr rhe hai
IQR =Q3-Q1 #interquartile range ko calculate kr rhe hai interquartile range ka mtlb hota hai ke data ke 75% or 25% ke beech ka difference hota hai
Q1,Q3,IQR #ye hume Q1,Q3 or IQR ke value ko print kr dega


#helps understand normal range of data or outliers ko identify krne main madad krta hai 
# prepares us for outlier detection or data transformation
(Q3 > Q1) and (IQR >0) # ye condition check krta hai ke q3 q1 se bada hai or iqr 0 se bada hai agar ye condition true hoti hai to iska matlb hai ke data ke spread normal hai or outliers ke chances kam hai 

 