#exploditory data analysis (EDA) data ko analysis krne ka ak bht he acha tarika hai jase he apko client se data milta hai to apko us data ko samjhna hota hai or us data me kya kya cheeze hai or us data me kya kya missing values hai or us data me kya kya outliers hai or us date me kya kya correlation hai or us data me kya kya distribution hai or us data me kya kya relationship hai or us data me kya kya pattern hai or us data me kya kya trend hai or us data me kya kya seasonality hai or us data me kya kya anomaly hai or us data me kya kya insight hai or us data me kya kya story hai or us data me kya kya business problem solve ho sakte hai or us data me kya kya opportunity hai or us data me kya kya risk hai or us data me kya kya challenge hai or us data me kya kya strength hai or us data me kya kya weakness hai 
#what is EDA 
#exploratory data analysis (EDA) is the process of understaning data before modeling
#key goals of EDA 
#1.identify patterns ,trend,&anomalies in data 
#2.check data quality
#3.understand feature type jis me kuch feature numerical hai kuch feature categorical hai or kuch feature datetime hai
 #EDA mindset & checklist (EDA report banate time apko kya kya cheeze check krni hai or kya kya cheeze apko apne EDA report me include krni hai )
#1. be curious  ask why & how ( EDA report banate time apko curious hona chahiye or apko pata hona chahiye ke apko apne EDA report me kya kya cheeze incule krni hai )
#2. look for relationships between features (apne feature ke beech relationship ko develop krna hai or wo relationship apne apne client ko dekhne hai  or usse wet  krwane hai ke kya ye co relation thk hai ya nhi )
#3.) document assumptions & findings (uske bad  data ke mutalk assumption kre g  or jo bhe finding hu g usko EDA report me lekh kr client se share krni hai )


#FUNCTION FOR EDA REPORT 
# data dimention check krna hai (.shape)
#column type (.dtypes) dtypes se hum tamam column type check kr sakte hai  data sahi trha se read howa ya nhi howa hai 
#agr ak numerical column or wo read hu raha hai as an object to apko us column ko numerical me convert krna hai or agr ak categorical column read hu raha hai as an object to apko us column ko category me convert krna hai 
#missing value check krna hai (.isnull().sum()) isnull().sum() se hum apne dataset me missing value check kr sakte hai or uske bad missing value ko handle krna hai 
#summary statistics mil sakte hai (.describe()) describe() se hum apne dataset ke numerical column ke summary statistics check kr sakte hai 

#example dataset 
#customer transaction  how many missing values are present in each column
# what is the distribution of product category
#which product are purchased most frequently
# are there any outliers in the transaction amounts?
#how do purchased amount vary by customer region ?
#example 5 EDA question
#is there any missing value data quantity has x missing values 
#what is the target varaible? _>revenue
#what is the numerical feature ? _>revenue,quantity
# what is the range of product? 4 type
#summary statistics (.describe()) se hum apne dataset ke numerical column ke summary statistics check kr sakte hai or uske bad missing values ko handle krna hai 

#key takeaways
#always define goals before starting EDA (EDA report banate time apko apne goals ko define krna chahiye or apko pata hona chahiye ke apko apne eda report me kya kya cheeze include krni hai)
#use EDA questions to guide analysis ( to hum phle he set of question bana le or apne eda report main usko include kre 
#document data quality issues & assumptions ( data ke quality issue or  hamri assumption jo hai unko hamre eda report ke andr document krna bht zarori hai  take client bta de hamri ko assumption galt to nahi  )
