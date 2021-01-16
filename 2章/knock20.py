# %%
# ノック11
import pandas as pd 
uriage_data = pd.read_csv('/Users/itouyuuta/Desktop/Python/pythonStudies/python_100_knocks/2章/uriage.csv')
uriage_data.head()
kokyaku_data = pd.read_excel('/Users/itouyuuta/Desktop/Python/pythonStudies/python_100_knocks/2章/kokyaku_daicho.xlsx')
kokyaku_data.head()
# %%
# ノック13
uriage_data['purchase_date'] = pd.to_datetime(uriage_data['purchase_date'])
uriage_data['purchase_month'] = uriage_data['purchase_date'].dt.strftime('%Y%m')
res = uriage_data.pivot_table(index='purchase_month', columns='item_name', values='item_price', aggfunc='sum', fill_value=0)
res
# %%
# ノック14
uriage_data['item_name'] = uriage_data['item_name'].str.upper()
uriage_data['item_name'] = uriage_data['item_name'].str.replace(" ", "")
uriage_data['item_name'] = uriage_data['item_name'].str.replace("　", "")
uriage_data.sort_values(by='item_name')
pd.unique(uriage_data['item_name'].sort_values())
# %%
# ノック15
flg_is_null = uriage_data['item_price'].isnull()
for trg in list(uriage_data.loc[flg_is_null, 'item_name'].unique()):
    price = uriage_data.loc[(~flg_is_null)&(uriage_data['item_name'] == trg), 'item_price'].max()
    uriage_data.loc[((flg_is_null) & (uriage_data['item_name'] == trg)), 'item_price'] = price
uriage_data.head()
# %%
uriage_data.isnull().any()
# %%
# ノック16
kokyaku_data['顧客名'].head()
# %%
uriage_data['customer_name'].head()
# %%
# 顧客名から余分なスペースを除く
kokyaku_data['顧客名'] = kokyaku_data['顧客名'].str.replace(" ", "")
kokyaku_data['顧客名'] = kokyaku_data['顧客名'].str.replace("　", "")
# %%
# ノック17
flg_is_digit = kokyaku_data['登録日'].astype('str').str.isdigit()
flg_is_digit
# %%
flg_is_serial = pd.to_timedelta(kokyaku_data.loc[flg_is_digit, '登録日'], unit='D')
from_serial = flg_is_serial + pd.to_datetime('1900/01/01')
from_serial
# %%
from_string = pd.to_datetime(kokyaku_data.loc[(~flg_is_digit), '登録日'])
from_string
# %%
kokyaku_data['登録日'] = pd.concat([from_serial, from_string])
kokyaku_data
#%%
kokyaku_data['登録年月'] = kokyaku_data['登録日'].dt.strftime('%y%m')
result = kokyaku_data.groupby('登録日')
print(result)
# %%
