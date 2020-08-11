#import cac thu vien can thiet
import pandas as pd 
import datetime as dt
import wbdata
import xlsxwriter


# thiet lap thoi gian can thiet
start_time = dt.datetime(2000,1,1)
end_time = dt.datetime(2018,12,30)



# thu hien lay du lieu voi modul wbdata de lay so lieu cua inflation va GDP
data_dates = (start_time,end_time)
#lấy dưu liệu của của inflation
data_inflation = wbdata.get_dataframe({'FP.CPI.TOTL.ZG':'INF'}, 
                            country=('vn'), 
                            data_date=data_dates, 
                            convert_date=False, keep_levels=True)
#lấy dữ liệu của GDP
data_gdp = wbdata.get_dataframe({'NY.GDP.MKTP.CD':'GDP'}, 
                            country=('vn'), 
                            data_date=data_dates, 
                            convert_date=False, keep_levels=True)
#lấy dữ liệu của GDP
data_gni = wbdata.get_dataframe({'NY.GNP.PCAP.CD':'GNI'},
						country=('vn'), 
                        data_date=data_dates, 
                        convert_date=False, keep_levels=True)        

                                            


df1 = pd.DataFrame(data_gdp)      
df2 = pd.DataFrame(data_inflation)  
df3 = pd.DataFrame(data_gni)

# write to excel

data = pd.concat([df1, df2, df3], axis=1)

writer = pd.ExcelWriter('worldbank.xlsx', engine='xlsxwriter')
data.to_excel(writer, sheet_name= 'sheet1')
writer.save()




    




    