import pandas as pd
df=pd.read_csv('C:\\Users\\pczarnecki2\\Desktop\\Kaggle Dataset\\archive\\features.csv')
#if file format is xlsx use pd.read_excel
print(df.head(10))