
import pandas as pd

df = pd.read_csv ('FETCH REWARDS SUMMARY.csv')
index = [list(df.columns)]


df['TRANSACTION_DATE'] = pd.to_datetime(df['TRANSACTION_DATE']) # format to correct datetime
for rewards in df.index:
    if df.loc[rewards, 'FETCH_REWARDS_EARNED'] == 0: #remove rows where fetch rewards earned =0
        df.drop(rewards, inplace = True) #replace with new data 
print(df)    #read and print the csv file

#calculations
total_number_of_items = df['NUMBER_OF_ITEMS'].sum()
TOTAL_AMOUNT_SPENT = df['TOTAL_AMOUNT_SPENT($)'].sum()
maximum_amt_spent = df['TOTAL_AMOUNT_SPENT($)'].max()
minimum_amt_spent = df['TOTAL_AMOUNT_SPENT($)'].min()
average_amt_spent = df['TOTAL_AMOUNT_SPENT($)'].mean()
number_of_trans = df['TRANSACTION_NUMBER'].count()


#calculations by specific store name

#total_spent_by_store_name = df.groupby(['STORE_NAME']).sum() # sum by each store

print(f'The indexes for this summary are : {index}')
print(f'Total number of items : {total_number_of_items}')
print(f'Total amount spent : $ {TOTAL_AMOUNT_SPENT}')
print(f'Maximum amount spent : ${maximum_amt_spent}')
print(f'Minimum amount spent : ${minimum_amt_spent}')
print(f'Average amount spent : ${average_amt_spent}')
print(f'total number of transaction : {number_of_trans}')

#print(f'Total spent by storename : ${total_spent_by_store_name}')
print(df.info())