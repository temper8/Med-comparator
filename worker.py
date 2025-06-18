from pathlib import Path
import pandas as pd
import exel

def executor(fn):
    miac_df, svmed_df, mes_df = exel.read(fn)
    print(f'convert: {fn.name}')
    lost_table = []
    svmed_mes = []
    for i, row in svmed_df.iterrows():
        fio = row['ФИО ребенка']
        res= mes_df.loc[mes_df['ФИО ребенка'] == fio]
        if res.empty:
            lost_table.append(row)
            svmed_mes.append(row)
        else:
            row['св-мед'] = 'мэс'
            svmed_mes.append(row)
            #print(row)

    m_df = mes_df[['ФИО ребенка', 'мэс']]
    #svmed_mes_df = pd.DataFrame(svmed_mes)
    svmed_mes_join_df = svmed_df.join(m_df.set_index('ФИО ребенка'),  on='ФИО ребенка', how='outer', validate='m:m')

    #print(pd.DataFrame(lost_table))
    #print('-----------------')

    df = miac_df.join(svmed_mes_join_df.set_index('ФИО ребенка'), lsuffix='_миац', rsuffix='_св-мед', on='ФИО ребенка', how='outer', validate='m:m')
    col_list = df.columns.values.tolist()
    #print(col_list)
    first_list = ['ФИО ребенка', 'миац', 'св-мед', 'мэс', 'Врач', 'ФИО врача', 'Возрастная группа']
    #print(first_list)
    tail =  [item for item in col_list if item not in set(first_list)]

    #print(tail)

    out_df = df[first_list+tail]
    #print(out_df)

    res = {
        'Сводка'     : out_df.sort_values(by=['ФИО ребенка']),
        'СВ-МЕД+МЭС' : svmed_mes_join_df.sort_values(by=['ФИО ребенка']),
        'МИАЦ'       : miac_df.sort_values(by=['ФИО ребенка']),
        'СВ-МЕД'     : svmed_df.sort_values(by=['ФИО ребенка']),
        'МЭС' : mes_df.sort_values(by=['ФИО ребенка'])
    }

    exel.write_results(res)


if __name__ == '__main__':
    fl = exel.get_file_list()
    for f in fl:
        try:
            executor(f)
        except Exception as e :
            print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: \n{e}")
        print('----------------------------')