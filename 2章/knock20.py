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
