import pandas as pd 
  
# reading csv file  
pdf=pd.read_csv(r"femeli-D1.csv") 
pdf1=pd.read_csv(r"femeli-M15.csv") 

#print(pdf.loc[pdf['<DTYYYYMMDD>'] == 20200825])
#result = pd.DataFrame( columns = ['date', 'OPEN','HIGH','LOW','CLOSE']) 

def test(row):
   return row['<DTYYYYMMDD>']
    
    
result=pd.concat([pd.DataFrame([test(row)], columns=['date']) for index, row in pdf.iterrows()],
          ignore_index=True)

print(result)