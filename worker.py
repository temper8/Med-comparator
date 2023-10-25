import pandas as pd
import exel

def executor(fn):
    miac_df, svmed_df, mes_df = exel.read(fn)
 
    print(mes_df.columns.values.tolist())

    lost_table = []
    svmed_mes = []
    for i, row in svmed_df.iterrows():
        fio = row['ФИО ребенка']
        res= mes_df.loc[mes_df['ФИО ребенка'] == fio]
        if res.empty:
            lost_table.append(row)
            svmed_mes.append(row)
        else:
            row['База'] = 'мэс'
            svmed_mes.append(row)
            #print(row)

    svmed_mes_df = pd.DataFrame(svmed_mes)
    print('-----------------')
    #print(pd.DataFrame(lost_table))
    print('-----------------')

    df = miac_df.join(svmed_mes_df.set_index('ФИО ребенка'), lsuffix='_миац', rsuffix='_св-мед', on='ФИО ребенка', how='outer', validate='m:1')
    col_list = df.columns.values.tolist()
    print(col_list)
    first_list = ['ФИО ребенка', 'База_миац', 'База_св-мед', 'Врач', 'ФИО врача', 'Возрастная группа']
    print(first_list)
    tail =  [item for item in col_list if item not in set(first_list)]

    print(tail)

    out_df = df[first_list+tail]
    #print(out_df)

    res = {
        'Сводка'     : out_df,
        'МИАЦ'       : miac_df,
        'СВ-МЕД'     : svmed_df,
        'СВ-МЕД МЭС' : mes_df
    }

    exel.write_results(res)


if __name__ == '__main__':
    fl = exel.get_file_list()
    for f in fl:
        executor(f)
        print('----------------------------')