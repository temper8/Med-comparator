import pandas as pd

miac_df = pd.read_excel('files/МИАЦ введено.xlsx', index_col=0)
print(miac_df)
my_list1 = miac_df.columns.values.tolist()
print(my_list1)