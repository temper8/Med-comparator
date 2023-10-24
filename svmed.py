import pandas as pd

def read_exel(fname):
    df =pd.read_excel(f'files/{fname}')
    df['База'] = '+'
    #print(sv_med_df)
    col_list = df.columns.values.tolist()
    print(col_list)
    df["ФИО ребенка"] = df["Фамилия"] + ' ' + df["Имя"] + ' ' + df["Отчетство"]
    return df.drop(columns=['Фамилия', 'Имя', 'Отчетство'])

if __name__ == '__main__':
    #sv_med_df =pd.read_excel('files/СВ МЕД МЭС 6 лет.xlsx', index_col=0)
    df = read_exel('06_СВ_МЕД_общий.xlsx')
    print(df[['ФИО ребенка',  'Дата рождения', 'Врач']])
    print(df.columns.values.tolist())