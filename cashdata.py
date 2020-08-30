import pandas as pd 
  
# reading csv file  
pdf=pd.read_csv(r"folad-D1.csv") 
pdf1=pd.read_csv(r"folad-M15.csv") 

#print(pdf.loc[pdf['<DTYYYYMMDD>'] == 20200825])
#result = pd.DataFrame( columns = ['date', 'OPEN','HIGH','LOW','CLOSE']) 

def test(row):
    low=row['<LOW>']
    high=row['<HIGH>']
    findedRows=pdf1.loc[pdf1['<DTYYYYMMDD>'] == row['<DTYYYYMMDD>']]
    
    for index,findedRow in findedRows.iterrows():
        if(findedRow['<HIGH>']==high):
            d1=pd.DataFrame({'date':[row['<DTYYYYMMDD>']],'open':[high],'high':[high],'low':[high],'close':[high]}, columns=['date','open','high','low','close'])
            d2=pd.DataFrame({'date':[row['<DTYYYYMMDD>']],'open':[low],'high':[low],'low':[low],'close':[low]}, columns=['date','open','high','low','close'])
            d3=[d1,d2]
            d3= pd.concat(d3)
            return d3
        elif(findedRow['<LOW>']==low):
            d1=pd.DataFrame({'date':[row['<DTYYYYMMDD>']],'open':[low],'high':[low],'low':[low],'close':[low]}, columns=['date','open','high','low','close'])
            d2=pd.DataFrame({'date':[row['<DTYYYYMMDD>']],'open':[high],'high':[high],'low':[high],'close':[high]}, columns=['date','open','high','low','close'])
            d3=[d1,d2]
            d3= pd.concat(d3)
            return d3
           
     
    
    
result=pd.concat([pd.DataFrame(test(row)) for index, row in pdf.iterrows()],
          ignore_index=True)

result.to_csv (r'C:\Users\masood\Downloads\Video\test.csv', index = False, header=True)