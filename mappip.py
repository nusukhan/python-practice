#appling function-apply,map & pipe
#pandas ke andr jab hum datframe bante hai to us ke uper matric operation ke lye kuch function available hote hai jaise ke apply,map ,pipe function  ye wo apply and map function hai jiske zarye se hum apne column ko manuplate kar ke new column create kae sakte hai 
# pipe se hum  dataset ke uper ak series of operation perform kar sakte hai pipe function se hum apna dataset ke uper ak series of operation performn kr sakte hai 
#load dataset

import pandas as pd #pandas library ko import krna prta hai data manipulation ke lye pandas liberry ko import krna prta hai 

# Load CSV file and convert order_date into datetime
df = pd.read_csv("ecommerse_sales_analytics_5000.csv",parse_dates=["order_date"]) #ddf =dataframe read csv function se csv file ko read krta hai csv file ko read krne ke lye read_csv function ka use krta hai csv comma separed  values ko read krta hai ab comma separed hota kya hai jab csv file me data ko comma se separate krna hota hai to usko comma separed values kehte hai 
#"ecommerse_sales_analytics_5000.csv" file ko read krna hai se_dates parameter se order_date column ko date format me convert krna hai parse_dates ye ak parameter hai order_dates ye ak actaul column name hai (mtlb csv file ke andr order_dates column hai usko dates format me convert krna hai )
#["order_date"]) ye  ak list hai jisme order_date column name hai usko date format me convert krna hai 
#df = pd.read_csv("ecommerse_sales_analytics_5000.csv",parse_dates=["order_date"]) ab is pori line me humne csv file ko read krna hai aur order_dates column ko date format me convert krna hai

# Verify dataframe
df.info() #df.info() function se data ke summary ko print krta hai (mtlb csv file ke summary ko print krta hai )

# Map payment methods into categories
df["payment_type"] = df["payment_method"].map({ #df kya krta hai  [(dataframe me se payment_method column ko acess krta hai aur uske uper map function ka use krta hai map function se hum apne column ke values ko manuplate kar sakte hai ab manuplate (ka mtlb column ke values ko change krna ) karne ke lye hum map function ka use krte hai ) or payment type column se new column create krna hai jisme payment method ke categories ko store krna hai (mtlb hum payment method wala column se new column create kr rhe hai  payment type ke name se jisme payment method ke catories ko store krna hai )
    "card": "digital", #card payment method ko digit category me map krna hai (mtlb csv file ke andr card payment methhod hai usko digital category me map krna hai)
    "wallet": "digital", #wallet payment method ko digital category me map krna hai (mtlb csv file ke andr wallet payment method hai usko digital category me map krna hai )
    "COD": "cash" #COD payment method ko cash category me map krna hai (mtlb csv file ke andr COD payment method hai usko cash category me map krna hai )
}) # hum kehte hai payment method ko dekha jai or payment type ka ak new attribute  introduce kya jai hamre dataset ke andr  kya jai hamre dataset ke andr  or uske hum ak mapping define krte hai map ke function ke zarye se jis main hum batte hai ke jab bhe payment method card ho to usko   payment type degital assume hu jab payment method wallet ho to uske payment type digital assume hu jab payment method cod ho to usko payment type cash assume ho 

# df["payment_type"] = df["payment_method"].map({ ak line main iska tlb hai ke df datadrame me se payment_method column ko access krna hai aur uske uper map function la use krna hai map function se hum apna column ke values ko manuplate kar sakte hai  or payment type coumn se new column create krna hai jisme payment method ke categories ko store krna hai (mtlb hum payment method wala column se new column create krna hai payment type ke name se jisme payment method ke categorues ko store krna hai )
#lehza hum  ak new column bana rhe hai payment type ka  jis ke andr 2 type ke payment hai digital or cash 
# verify
df["payment_type"].unique() #df[["payment_type"].unique() function se payent_type column ke unique value ko print krta hai (mtlb payment_type column ke uniqua values ko print krta hai )]]
df[["payment_method","payment_type"]].head() #function se payment_method aur payment_type column ke fisrt 5 rows ko print krta hai (mtlb payment_method aur payment_type column ke first 5 rows ko print krta hai)
df.groupby("payment_type").size() #group function se payment_type column ke uper group by krna hai or size function se har group ke size ko print krna hai(mtlb payment_type column ke uper group by krna hai or size fnction se har group ke size ko print krna hai)

# apply() -create revenue category  map ka function surf ak column pr apply hu sakta hai or apply la fumction multiple column pr apply hu sakta hai  or dono main speed ka frq surf ye hai ke map ka function bht  speed se execute hu jata hai kyu ke wo single series pr apply hota hai  ( apply ka function column ke uper apply hu sakta hai ya row ke uper apply hu sakta hai )
# jab hamre pass complex logic hota hai jisme multiple column involved hota hai to ham apply function ka use karte hai (mtlb jab hamre pass complex logic hota hai jisme multiple column involved hota hai to ham apply function ka use karte hai ) or jab hamre pass simple logic hota hai jisme single column involved hota hai to ham map function ka use karte hai (mtlb jab hamre pass simple logic hota hai jisme single column involved hota hai to ham map function ka use karte hai)
def revenue_category(row): #revenue_category function ko define krna hai jisme row parameter pass krna hai row parameter se hum apne dataframe ke rows ko access kr sakte hai (mtlb hum apne dataframe ke row ko access krne ke lye row parameter ka use kr sakte hai)
    if row["revenue"] > 500: #agar row ke revenue column ki value 500 se zyada hai to usko high category  ke tranction hai me map krna hai (mtlb agar csv file ke andr revenue column ki value 500 se zyada hai to usko high category me map krna hai  high category ka mtlb hai ke usko high category me map krna hai high category main map krne ka mtlb hai ke usko high category me map krna hai )
        return "High"
    elif row["revenue"] >= 200: # 200 or 500 ke beech me hai to hum usko medium category ke tranction hai 
        return "Medium"
    else:
        return "low"
df["revenue_category"] =df.apply(revenue_category,axis=1) # jab hum ye criteria banne ge to usse hamre pass revenue_category ka ak new column create ho jayega jisme hamre pass high,mediumn,low category ke tranction hai (mtlb jab hum ye criteria banne ge to usse hamre pass revenue_category ka ak new column create ho jayega jisme hamre pass high,mediumn,low category ke traction hai )or apply function se hum apne criteria ko dataframe ke uper apply karengeor axis=1 ka mtlb hai ke hum apne criteria ko row ke upper apply karege(mtlb hum apne criteria ko row ke upper apply karege ) or jab hum axis=0 karege to hum apne criteria ko column ke uper apply karege (mtlb hum apne column ke upper apply karege ) or jab hum axis=1 karege to hum apne criteria ko row ke upper apply karege )
# why apply decision depend on multiple columns
#verify
df["revenue_category"].value_count() #df["revenue_category"].value_count() function se revenue_category column ke unique value ke count ko print krta hai(mtlb_revenue_category column ke unique value ke count ko print krta hai )or revenue_category column ke uper value count krna hai 
df[["revenue","revenue_category"]].simple(10) #df[["revenue","revenue_category"]].simple(10)function se revenue aur revenue_category column ke firrst 10 rows ko print krta hai (mltb revenue aur revenue_category column ke first 10 rows ko print krta hai )
  #revenue > 5000 high 
  # between 200 and 5000 mediumn
  # < 200 low 
#pipe() method chaining
#pipe method se hum apne dataset ke uper ak series of operation perform kar sakte hai (mtlb pipe method se hum apne dataset ke uper ak series of operation perform kar sakte hai ) 

def add_profit(data): #def add_profit function ko define krna hai jisme data parameter pass krna hai data parameter se hum apne dataframe ko access kar sakte hai ( mtlb hum apne dataframe ko acess karne ke lye data parameter ka use kar sakte hai ) or add_profit function se hum apne dataset me profit column ko add karna hai (mtlb add_profit function se hum apne dataset me profit column ko add karna hai ) or profit column ki value revenue column ki value ka 20% hoga (mtlb profit column ki value revnue column ki value ke 20% hoga )
    data["profit"] = data ["revenue"] *0.20 # data["profit"] = data ["revenue"] *0.20 ka mtlb hai ke profit column ki value revenue column ki value ke 20% hoga 
    return data 
def add_net_revenue(data):# dosra humne ak or column banya hai net revnue ka def add_net_revenue(data):function ko define krna hai jisme data parameter pass krna hai data parameter se hum apne dataframe ko access kar sakte hai 
    data["net_revenue"] =data["revenue"] - data["profit"] # data["net_revenue"] se data dataframe me net_revnue column ko acces krna hai or data["revenue"]
    #jis me hum revenue column ki value ko profit column ki value se minus krna hau
    return data # return data ka mtlb hai ke hum apne dataset ko return karna hai (mtlb hum apne dataset ko return karna hai )
df = ( #df = ( se hum apne dataset ko pipe method ke zarye se manuplate karenge (mtlb hum apne dataset ko pipe method ke zarye se manuplate karenge ) 
    df #df se hum apne dataset ko access karenge (mtlb hum apne dataset ko access karenge ) )
    .pipe(add_profit) #.pipe(add_profit) se hum apne dataset ke uper add_profit function ko apply karenge (mtlb hum apne dataset ke uper add_profit function ko apply karenge ) or pipe method se hum apne dataset ke uper ak series of opertion perform karenge 
    .pipe(add_net_revenue) # .pipe(add_net_revenue) se hum apne dataset ke uper add_net_revenue function ko apply karenge (mtlb hum apne dataset ke uper add_net_revenue function ko apply karenge ) or pipe method se hum apne dataset ke ueper ak series of operation perform karenge  
)
 #verify
df[["revenue","profit","net_revenue"]].head() #df[["revenue","profit","net_revenue"]].head() function se revenue profit aur net_revenue column ke first 5 rows ko print krta hai 
