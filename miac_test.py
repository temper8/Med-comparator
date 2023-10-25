import pandas as pd

miac_df = pd.read_excel('files/МИАЦ_Реднева.xlsx')

col_list = miac_df.columns.values.tolist()
print(col_list)
ages_groups =sorted(miac_df['Возрастная группа'].unique().tolist())
for i, ag in enumerate(ages_groups):
    print(f"[{i}] - {ag}")
print("Введите номер возрастной группы:")
iag = int(input())
ag = ages_groups[iag]
print(f"{iag} - {ag}")
group_06 = miac_df[miac_df['Возрастная группа'] == ag]
print(group_06[['ФИО ребенка', 'Дата рождения', 'Возрастная группа', 'ФИО врача']])