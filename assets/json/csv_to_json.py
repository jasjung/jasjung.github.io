import pandas as pd 

# df = pd.read_csv('books.csv')
# df.to_json('books2.json',orient='records')

df = pd.read_excel('books.xlsx')
df.to_json('books.json',orient='records')
print(df)

