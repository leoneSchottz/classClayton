#%%
import pandas as pd
import plotly.express as px

#%%
df = pd.read_csv('LEC_SpringSeason_2024.csv')

# %%
df_jg = df.loc[df['Role'] == 'JUNGLE']
df_jg = df_jg.corr(numeric_only=True)
# df_jg = df_jg.where((df_jg >=0.75) | (df_jg <=0.75 ))
px.imshow(df_jg.where((df_jg >=0.75) | (df_jg <=-0.75 )),title='Jungle').show()
# cor_jg = df_jg['CSD@15'].corr(df_jg['CS'])

df_top = df.loc[df['Role'] == 'TOP']
df_top = df_top.corr(numeric_only=True)
# df_top = df_top.where((df_top >=0.75) | (df_top <=0.75 ))
px.imshow(df_top.where((df_top >=0.75) | (df_top <=-0.75 )),title='Top').show()
# cor_top = df_top['CSD@15'].corr(df_top['CS'])

df_sup = df.loc[df['Role'] == 'SUPPORT']
df_sup = df_sup.corr(numeric_only=True)
# df_sup = df_sup.where((df_sup >=0.75) | (df_sup <=0.75 ))
px.imshow(df_sup.where((df_sup >=0.75) | (df_sup <=-0.75 )),title='Support').show()
# cor_sup = df_sup['CSD@15'].corr(df_sup['CS'])

df_car = df.loc[df['Role'] == 'ADCARRY']
df_car = df_car.corr(numeric_only=True)
# df_car = df_car.where((df_car >=0.75) | (df_car <=0.75 ))
px.imshow(df_car.where((df_car >=0.75) | (df_car <=-0.75 )),title='Adcarry').show()
# cor_car = df_car['CSD@15'].corr(df_car['CS'])

df_mid = df.loc[df['Role'] == 'MID']
df_mid = df_mid.corr(numeric_only=True)
# df_mid = df_mid.where((df_mid >=0.75) | (df_mid <=0.75 ))
px.imshow(df_mid.where((df_mid >=0.75) | (df_mid <=-0.75 )),title='Mid').show()
# cor_mid = df_mid['CSD@15'].corr(df_mid['CS'])

# print(f'cor_mid: {cor_mid}')
# print(f'cor_top: {cor_top}')
# print(f'cor_sup: {cor_sup}')
# print(f'cor_car: {cor_car}')
# print(f'cor_jg: {cor_jg}')
#%%
df.columns


#%%

# px.imshow(df_good_heat).show()
# %%
# df['Role'].value_counts()

# %%
# sns.pairplot(df)

# %%
