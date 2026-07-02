# working with datetime & time series data
# datetime data ke sath kaam krna or time series data ke sath kaam krna data anaysis main ek important aspect hai kyun ke datetime data ke sath kaam krne se hum apne data ke time based patterns ko samjh sakte hai or time series data ke sath kaam krne se hum apne data ke time based trend ko samjh sakte hai or future ke lye prediction kr sakte hai
# timeseries
#time series data is to much important data (aksar real world senieor main hume jo data milta hai  wo time series based data hota hai )
#to yaha hum jo time series based data ko read kre g us main hum time or date ke column ko specail read kre g or specail treatment kre g 
# load dataset
import pandas as pd # pandas ki library ko import kre g 

df = pd.read_csv("ecommerce_sales_analytics 5000.csv", parse_dates=["order_date"]) # df dataframe ke andr csv file ko acess krna hai 

# setting datetime index
df = df.set_index("order_date") # yaha hum order date ko index bana le g  ska matlab hai:

#df ek dataframe hai.
#order_date" us dataframe ka column hai.
#set_index() function us column ko dataframe ka index bana deta hai.

df.index # df dataframe hai .index dataframe ke row ko acess karne ke liye use hota hai 
#df.index ka matlab hai:
#“Muje dataframe ke indexes dikhao.”
#Easy yaad rakhne ka tareeqa:
#df.columns → columns dikhao
#df.index → rows ke labels/index dikhao
#df.values → actual data dikha

# montly revenue analysis (yaha hum apne data ko month wise le kr jai g  pori revenue stream ka monthly analysis kre g  )
#monthly_revenue = ...“Jo bhi result aaye usko monthly_revenue naam ke variable main save kar do.” ye ak varaible hai yni jo reslt aa ga usko is varaible main store kar rhe hai 
#df["revenue"] dataframe df se "revenue" wala column nikalo df["revenue"]sirf revenue column dega.
#.resample("ME")
#Ye bohat important part hai.
#resample time/date data ko group karta hai.
#"ME" ka matlab:

#Month End (har month ka data ek group bana do)

#Yani January ka alag total,
#February ka alag total,
#etc.
#.sum()
#Ab jo monthly groups bane hain un sab ka total nikal raha hai.
#Ab jo monthly groups bane hain un sab ka total nikal raha hai.

#Yani:

#Jan Revenue	100 + 200 = 300
#Feb Revenue	500 + 400 = 900
monthly_revenue = df["revenue"].resample("ME").sum() #ka matlab:
#“Revenue column lo, usko month-wise group karo, har month ka total revenue nikalo, aur result monthly_revenue variable main save kar do.”
monthly_revenue #monthly_revenue ek naam hai jisme humne monthly revenue ka result rakh diya hai taa ke baad main use kar saken.

# trend interpretation
monthly_revenue.pct_change() # ye wo montly_revenue hai jo hamne pehle banya tha 
#pct_change ka matlab hota hai:

#Percentage Change (kitna percent change hua pichle month se) ke jo hamra montly revenue hai us main change kitna hai or us change ko hum absulote ke bjhe percentage main change kr de g  

monthly_revenue.index.is_monotonic_increasing #verify 
#1. monthly_revenue

#Ye tumhara variable hai jisme monthly revenue wala result save hai
#2. .index

#Ye us data ke indexes ko access kar raha hai.
#3. .is_monotonic_increasing

#Ye check karta hai:

#“Kya indexes ascending order main hain?”
#yani chhote se bade order main.



 # 3. .is_monotonic_increasing

#Ye check karta hai:

#“Kya indexes ascending order main hain?”
#yani chhote se bade order main.


print(monthly_revenue.sum(),df["revenue"].sum()) #hum dekhe hai jo humne month wise grouping ke hai or resamply kya hai  us main hum sanitary check laga sakte hai ke jo month end ka revenue hai wo total revenue se zada to nhi hu gya 
monthly_revenue.sum()<=df["revenue"].sum()