import pandas as pd


import matplotlib 
from matplotlib import pyplot as plt
monthly_budget = 900

df = pd.read_csv (r'FETCH REWARDS SUMMARY.csv') #read.csv file stored in capstone project folder
index = [list(df.columns)]    #prints all the header of column
df['TRANSACTION_DATE'] = pd.to_datetime(df['TRANSACTION_DATE']) # format to correct datetime

#removing rows where fetch rewards=0 and replacing it with new dataframe
for rewards in df.index:
    if df.loc[rewards, 'FETCH_REWARDS_EARNED'] == 0: #remove rows where fetch rewards earned =0
        df.drop(rewards, inplace = True) #replace with new data 

# calculating 
total_number_of_items = df['NUMBER_OF_ITEMS'].sum()
TOTAL_AMOUNT_SPENT = df['TOTAL_AMOUNT_SPENT($)'].sum()
maximum_amt_spent = df['TOTAL_AMOUNT_SPENT($)'].max()
minimum_amt_spent = df['TOTAL_AMOUNT_SPENT($)'].min()
average_amt_spent = round(df['TOTAL_AMOUNT_SPENT($)'].mean(), 1)
number_of_trans = df['TRANSACTION_NUMBER'].count()
average_cost_of_each_item = round(TOTAL_AMOUNT_SPENT / total_number_of_items, 1)

#summing by transaction date and putting it in a month format
monthly_expense = df.groupby(df.TRANSACTION_DATE.dt.month)[['TOTAL_AMOUNT_SPENT($)', 'NUMBER_OF_ITEMS', 'FETCH_REWARDS_EARNED']].sum()
'''if monthly_expense <= monthly_budget:
    print('Great job! You stayed on budget')
    else:
    print('!!!You went over budget!!!!')'''

#total_spent_by_store_name = df.groupby(['STORE_NAME']).sum() # sum by each store

#getting storename, amount spent n no of items
total_spent_by_store_amount_items = df.loc[:,['STORE_NAME', 'TOTAL_AMOUNT_SPENT($)', 'NUMBER_OF_ITEMS']] 

#info for specific store only like costco
total_spent_by_specific_store = total_spent_by_store_amount_items.loc[total_spent_by_store_amount_items ['STORE_NAME'] == 'REMKE MARKETS']



print(index)
print(f'Total number of items : {total_number_of_items}')
print(f'Total amount spent : $ {TOTAL_AMOUNT_SPENT}')
print(f'Maximum amount spent : ${maximum_amt_spent}')
print(f'Minimum amount spent : ${minimum_amt_spent}')
print(f'Average amount spent : ${average_amt_spent}')
print(f'Total number of transaction : {number_of_trans}')
print(f'Average cost of each item : ${average_cost_of_each_item}')
print(monthly_expense)
#print(total_spent_by_store_amount_items)
print(total_spent_by_specific_store)
#plt.plot(monthly_expense_by_month)
plt.plot(monthly_expense)
plt.xlabel('TRANSACTION MONTH')
plt.ylabel('TOTAL AMOUNT SPENT')
plt.title('MONTHLY EXPENSE REPORT')
plt.legend(['TOTAL_AMOUNT_SPENT($)', 'NUMBER_OF_ITEMS', 'FETCH_REWARDS_EARNED'])
#print(df)
#print(df.tail(10))
