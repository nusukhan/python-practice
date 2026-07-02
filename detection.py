# outlier detection using statistical rules 
#outlier detection ka basic purpose ye hota hai ke hum apne data main se un data points ko identify kr ke remove kr de jo normal data point ke range main nahi ate
#dataset main asi value dhondna jo baki data se bht zayda different hu or usko remove krna taki hamra data analysis accurate ho jaye 
#suppose ek class ke marks hai
#marks 78,80,82.79.81,400
#yaha 400 outlier hai kyunki wo baaki marks se bht zayda different hai  baki sab 80 ke around hai 
#ye ho sakta hai ke 400 kisi data entry error ki waja se aa gya ho ya kisi student ne cheating kr ke 400 marks le liye ho 
#data entry  mistake ya cheating ke waja se outlier aa sakta hai 
#sensor error ya kisi machine ka malfunction bhe outlier ka waja ban sakta hai 
#fraudulent activity bhe outlier ka waja ban sakta hai 
#unusual event ya natural disaster ke waja se bhi outlier aa sakta hai 
#is lye outlier detection important hai taki hum apne data ko clean kr ke accurate analysis kr saken

#outlier detection kyu important hai
#average ya mean ko outlier bht zayda affect krta hai
#median outlier se zayda affect nhi hota hai
#machine learning ko confuse karte hai
#grafh ko distort karke data vistualization ko galat bana dete hai 
#predictions ko wrong bana dete hai
#
#example normal salary data 50k,55k,60k,58k,52k
#average salary 55k hai
#lekin agar ek outlier salary 500k aa jaye to average salary 143k ho jaye gi jo ke galat hai 


# jab hum koi dataset load kr lete hai to uske nadr hume ak kaam krte hai outlier remover
# outlier ase data point hote hai jo normal data point ke range main nhi ate jo normally one of extreate value hote hai  jo hamre data ke andr mean,median ko disturb krte hai
# or data analysis ko bhe disturb krte hai jo mostly data main error ke waja se aa jate hai unko hum outlier keh dete hai or unko hum remove kr dete hai
# outlier are data points that fall outside the normal range, representing extreme values that can distort the mean & median of dataset

# methods of outlier identification & removal
# (outlier ko identify kr ke remove krne ke method )
# 1.IQR method (jis main hum interquartile range ko follow krte hai outlier ko remove krne ke lye )
# IQR = interquartile range
# IQR = Q3 - Q1
# WHERE
# Q1 = 25TH PERCENTILE
# Q3 = 75TH PERCENTILE
# suppose hamre data set main 1,2,3,4,5,6,100 value hai
# Q1 = 2
# 2.Z_score method ()
# 3.domain_driven threholds (hum kisii dpmain expert ko bethe  or usse poche ke is data ke andr kon kon se outlier hai or wo hume domain expert bta de   )
#outlier kya hota hai (asi value jo baqi data se bht zayda different hu )
10,12,15,18,20,22,500
#yaha 500 unusual hai outlier 
#normally ecommerce dataset me revenue 1000_5000 hu sakta hai 
#lekin agr order ka revenue 500000 aa jai to wo suspicious ho sakta hai is lye outlier detect krte hai 


# load dataset
import pandas as pd #pandas ko import krna pandas library ko import kr rhe hai take data handle kar sake 

df = pd.read_csv("ecommerce_sales_analytics_5000.csv", parse_dates=["order_date"]) #csv file ko dataframe main load kar rahe hai or oder_date ko date format me convert kr rhe hai 
#read_csv()csv file ko dataframe me convert krta hai 
#df dataframe varaible hai 
#dataframe excel table jaisa structure 
#order_date     revenue   category
#2025-01-01      5000     electronics

#parse_dates = ["order_date"] ( ye column ko normal text ke bajhe date format me convert karta hai )
#without parse_dates "2025-01-01" surf string hoti hai 
#with parse_dates: python usko actual date samjhega 



#step 3 - Q1 niklana 
# IQR method
Q1 = df["revenue"].quantile(0.25) # revnue column ka 25% quartile Q1 nikl rahe hai  #df["revenue"] revenue column access kar raha hai  #quantile(0.25) 25% position wali value fisrt quantile (Q1) 
 #mtlb 25% data is value se neche hai 75% data is value se upar hai 
 #step 4 Q3 niklana mtlb 75% data is se neeche 25% data is se uper 
Q3 = df["revenue"].quantile(0.75)#revenue column ka 75% quartile nikla rahe hai #mtlb 75% data is se neeche 25% data is se uper
#iqr = q3-q1 middle 50% data ka range calculate kr rhe hai 
lower_bound = Q1 - 1.5 * IQR #outlier detect karne ke lye minimum accceptable limit bana rhe hai 
upper_bound = Q3 + 1.5 * IQR #outlier detect karne ke lye maximum acceptable limit bana rhe hai
outlier_iqr = df[(df["revenue"]< lower_bound) | (df["revenue"] > upper_bound)] #wo sari rows nikal rahe hai jinka revnue bounds se behar hai yani outiler hain 
#iqr (interquartile range):measure the middle 50% of data.robust for skewed distributions (like revenue)
outlier_iqr.shape #verification outlier rows or column ki total count print kr rhe hau 
outlier_iqr[["revenue","product_category"]].head() #inspect first 5 outlier rows ka revenue or category dekh rahe hai 
df = df[(df["revenue"]>=lower_bound)&(df["revenue"] <= upper_bound)] #dataset se outlier remove karke sirf normal data save kar rahe hai 


#z-score method (statistics ka ak concept hai jo batata hai ke koi value mean se kitne standard deviation dur hai)
#z_score="ye value normal data point se kitne standard deviation dur hai"
#positive z_score ka mtlb value mean se upar hai 
#negative z_score ka mtlb value mean se neeche hai 
#suppose class ke marks 
#marks:60,70,80,90,100
#mean =80
#agr kisi student ke marks 100 hai or standard deviation 10 hai to uska z_score 2 hoga (100-80)/10=2
from scipy.stats import zscore #zscore function ko import kr rhe hai scipy library se 
df =pd.read_csv("ecommerce_sales_analytics_5000.csv",parse_dates=["order_date"]) #csv file ko dataframe main load kar rahe hai or order_date ko date format me convert kr rahe hai
df["revenue_z"] = zscore(df["revenue"]) #df["revenue_z"] revenue column ka z-score calculate kr ke naya column bana rahe hai jisme z_score value store hogi z_score kya hota hai: how many standand deviations a value is from the mean 
 
outliers_z =df [ df ["revenue_z"].abs() <= 3] #outliers_z main wo sari rows nikal rahe hai jinka z_score 3 se kam hai yani normal data point hain 
#z_score shows:how many standard deviations a value is from the mean 
#rule:[z] > 3 outlie.shape #outlier rows or column ki total count print kr rhe hai
outliers_z.shape #inspect first 5 outlier rows ka revenue or category dekh rahe hai
df = df[df["revenue_z"].abs() <= 3] #dataset se outlier remove karke sirf normal data save kar raha hai