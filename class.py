#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import plotly.express as px

#%%
df = pd.read_csv('LEC_SpringSeason_2024.csv')

# df = df[['Role', 'Damage_self_mitigated', 'Physical_Damage', 'GOLD%', 'CS_in_Teams_Jungle']]

df['Role'] = df['Role'].replace({'TOP': 1, 'MID' : 2, 'JUNGLE' : 3, 'SUPPORT': 4, 'ADCARRY' : 5})

#%%
df = df.select_dtypes('number')

X = df.drop(['Role'], axis=1)

y = df['Role']

#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier()

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

#%%

df_check = pd.DataFrame( { 'test' : y_test , 'pred' : y_pred})
# %%
print(accuracy)
# df_check = df_check.where(df_check['test'] != df_check['pred']).dropna()

# print(df.iloc[df_check.index])
# %%

importances = clf.feature_importances_
feature_names = X.columns
importance_dict = dict(zip(feature_names, importances))

print("Importância das características:")
for feature, importance in importance_dict.items():
    print(f'{feature}: {importance * 100:.2f}%')

