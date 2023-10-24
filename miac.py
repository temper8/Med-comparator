import pandas as pd

def read_exec(fname, ages_group= None):
    df = pd.read_excel(f'files/{fname}')
    df.rename(columns={"ФИО врача": "Врач"})
    col_list = df.columns.values.tolist()
    #print(col_list)
    if ages_group is None:
        ages_groups =sorted(df['Возрастная группа'].unique().tolist())
        for i, ag in enumerate(ages_groups):
            print(f"[{i}] - {ag}")
        print("Введите номер возрастной группы:")
        iag = int(input())
        ages_group = ages_groups[iag]
        print(f"{iag} - {ages_group}")
    group = df[df['Возрастная группа'] == ages_group]
    group['База'] = '+'
    return group

if __name__ == '__main__':
    df = read_exec('МИАЦ_Реднева.xlsx')
    print(df[['ФИО ребенка', 'Дата рождения', 'Возрастная группа', 'ФИО врача']])