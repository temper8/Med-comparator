import pandas as pd

miac_df = pd.read_excel('files/МИАЦ введено.xlsx', index_col=0)
my_list1 = miac_df.columns.values.tolist()
print(my_list1)
#sv_med_df =pd.read_excel('files/СВ МЕД МЭС 6 лет.xlsx', index_col=0)
sv_med_df =pd.read_excel('files/СВ МЕД Список 6 лет общий.xlsx', index_col=0)
print(sv_med_df)
my_list2 = sv_med_df.columns.values.tolist()
print(my_list2)

res_table = []
for i, row in sv_med_df.iterrows():
    #print(f"Index: {i}")
    fio = f"{row['Фамилия']} {row['Имя']} {row['Отчетство']}"
    #print(f"{row}\n")
    #print(fio)
    res= miac_df.loc[miac_df['ФИО ребенка'] == fio]
    if res.empty:
        res_table.append(row)
        #print(fio)
        #print(row)
    #print('----------------')

res_df = pd.DataFrame(res_table)
print(res_df)
res_df.to_excel("output.xlsx")