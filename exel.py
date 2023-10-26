import pandas as pd
from pathlib import Path

input_dir = Path('files')
archive_dir = Path('archive')
result_dir = Path('result')
file_name = None

def prepare(df):
    df = fix_date(df)
    df['База'] = '+'
    col_list = df.columns.values.tolist()
    df["ФИО ребенка"] = df["Фамилия"] + ' ' + df["Имя"] + ' ' + df["Отчетство"]
    df["ФИО ребенка"] = df["ФИО ребенка"].str.replace('Ё', 'Е')
    return df.drop(columns=['Фамилия', 'Имя', 'Отчетство'])

def fix_date(df):
    if 'Дата Рождения' in df.columns:
        print(f"rename col 'Дата Рождения'")
        df = df.rename(columns={"Дата Рождения": "Дата рождения"})
    time_col = 'Дата рождения'
    if time_col in df.columns:
        #print('fix date')
        df[time_col] = df[time_col].astype(str)
    else:
        print(f'нет {time_col}')
    return df

def read(fn):
    global file_name
    print(f"reading: {fn}")
    file_name = fn
    with pd.ExcelFile(file_name) as xls:  
        miac = pd.read_excel(xls, sheet_name='МИАЦ')
        miac["ФИО ребенка"] = miac["ФИО ребенка"].str.replace('Ё', 'Е')
        miac['База'] = '+'
        svmed = prepare(pd.read_excel(xls, sheet_name='СВ-МЕД'))
        mes_svmed = prepare(pd.read_excel(xls, sheet_name='СВ-МЕД МЭС'))
        return miac, svmed, mes_svmed

def get_result_file_name():
    new_name = file_name.with_stem(f"{file_name.stem}_res").name
    return result_dir.joinpath(new_name)

def write_results(res):
    fn = get_result_file_name()
    print(f"write result to: {fn} ")
    with pd.ExcelWriter(fn) as writer:  
        for key, df in res.items():
            df.to_excel(writer, sheet_name=key)

def get_file_list():
    return list(input_dir.glob('*.xlsx'))

if __name__ == '__main__':
    miac, svmed, mes_svmed = read('04_2023_10_25.xlsx')
    #print(miac)
    print('----------------------------')
    print(svmed)
    #print(df.columns.values.tolist())