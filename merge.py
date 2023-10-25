import miac
import svmed
import pandas as pd

age = '5 лет'
files_list ={
        '4 года' :
        {
            'МИАЦ'       : '4 ГОДА МИАЦ.xlsx',
            'СВ-МЕД'     : '4 ОБЩИЙ СВ-МЕД.xlsx',
            'СВ-МЕД МЭС' : '4 ГОДА МЭС СВМЕД.xlsx'
        },
        '5 лет' :
        {
            'МИАЦ'   : '5 ЛЕТ МИАЦ.xlsx',
            'СВ-МЕД' : '5 МЭС СВМЕД.xlsx',
            'СВ-МЕД МЭС' : '5 ОБЩИЙ СВ-МЕД.xlsx'
        },
        '6 лет' :
            {
                'МИАЦ'   : 'МИАЦ_Реднева.xlsx',
                'СВ-МЕД' : '06_СВ_МЕД_общий.xlsx',
                'СВ-МЕД МЭС' : '06_СВ_МЕД_МЭС.xlsx'
            }

}


files = files_list[age]
miac_df = miac.read_exec(files['МИАЦ'], age)

svmed_df = svmed.read_exel(files['СВ-МЕД'])
print(svmed_df.columns.values.tolist())

mes_df = svmed.read_exel(files['СВ-МЕД МЭС'])
 
print(mes_df.columns.values.tolist())

lost_table = []
svmed_mes = []
for i, row in svmed_df.iterrows():
    #print(f"Index: {i}")
    #fio = f"{row['Фамилия']} {row['Имя']} {row['Отчетство']}"
    #print(row)
    fio = row['ФИО ребенка']
    #print(f"{row}\n")
    #print(fio)
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
first_list = ['ФИО ребенка', 'База_миац', 'База_св-мед', 'Врач', 'ФИО врача', 'Возрастная группа']
tail =  [item for item in col_list if item not in set(first_list)]

print(first_list+tail)
out_df = df[first_list+tail]
print(out_df)

with pd.ExcelWriter(f"{age}_out.xlsx") as writer:  
    out_df.to_excel(writer, sheet_name='Сводка')
    miac_df.to_excel(writer, sheet_name='МИАЦ')
    svmed_df.to_excel(writer, sheet_name='СВ-МЕД')
    mes_df.to_excel(writer, sheet_name='СВ-МЕД МЭС')
#out_df.to_excel(f"{age}_out.xlsx", sheet_name='Сводка')
#miac_df.to_excel(f"{age}_out.xlsx", sheet_name='МИАЦ')