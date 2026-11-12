# --- cell ---
# import pandas as pd
import pandas as pd
# import numpy as np
import numpy as np
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# import seaborn as sns
import seaborn as sns
# import warnings
import warnings
# from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OrdinalEncoder
# from sklearn.impute import SimpleImputer
from sklearn.impute import SimpleImputer
# from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import KBinsDiscretizer
# warnings.filterwarnings('ignore')
warnings.filterwarnings('ignore')
# --- cell ---
# train = pd.read_csv("train_Insurance.csv", sep=";")
train = pd.read_csv("train_Insurance.csv", sep=";")
# train.head()
train.head()
# --- cell ---
# test=pd.read_csv("test_Insurance.csv", sep=";")
test=pd.read_csv("test_Insurance.csv", sep=";")
# test.head()
test.head()
# --- cell ---
# train.describe(include='all')
train.describe(include='all')
# --- cell ---
# test.describe(include="all")
test.describe(include="all")
# --- cell ---
# train.info()
train.info()
# --- cell ---
# test.info()
test.info()
# --- cell ---
# train.isnull().sum()
train.isnull().sum()
# --- cell ---
# test.isnull().sum()
test.isnull().sum()
# --- cell ---
# train.isnull().sum().sum()
train.isnull().sum().sum()
# --- cell ---
# test.isnull().sum().sum()
test.isnull().sum().sum()
# --- cell ---
# def impute_mode(df, col):
def impute_mode(df, col):
#     imputer = SimpleImputer(strategy='most_frequent')
    imputer = SimpleImputer(strategy='most_frequent')
#     df[[col]] = imputer.fit_transform(df[[col]])
    df[[col]] = imputer.fit_transform(df[[col]])
#     return df
    return df
# def impute_median(df, col):
def impute_median(df, col):
#     imputer = SimpleImputer(strategy='median')
    imputer = SimpleImputer(strategy='median')
#     df[[col]] = imputer.fit_transform(df[[col]])
    df[[col]] = imputer.fit_transform(df[[col]])
#     return df
    return df
# def drop_nan(df, col):
def drop_nan(df, col):
#     return df.dropna(subset=[col])
    return df.dropna(subset=[col])
# --- cell ---
# train["window_count"].replace("without",0, inplace=True)
train["window_count"].replace("without",0, inplace=True)
# --- cell ---
# test["window_count"].replace("without",0, inplace=True)
test["window_count"].replace("without",0, inplace=True)
# --- cell ---
# test['window_count'] = test['window_count'].replace('>=10', 10)
test['window_count'] = test['window_count'].replace('>=10', 10)
# --- cell ---
# train['window_count'] = train['window_count'].replace('>=10', 10)
train['window_count'] = train['window_count'].replace('>=10', 10)
# --- cell ---
# mode_cols = ['year', 'coverage_period', 'is_residential', 
mode_cols = ['year', 'coverage_period', 'is_residential', 
#              'is_finished_and_fenced', 'has_garden', 'locality', 
             'is_finished_and_fenced', 'has_garden', 'locality', 
#              'structure_type', 'Geo_Code']
             'structure_type', 'Geo_Code']
# ligne vide

# for col in mode_cols:
for col in mode_cols:
#     train = impute_mode(train, col)
    train = impute_mode(train, col)
# ligne vide

# median_cols = ['area_m2', 'window_count']
median_cols = ['area_m2', 'window_count']
# for col in median_cols:
for col in median_cols:
#     train = impute_median(train, col)
    train = impute_median(train, col)
# train = drop_nan(train, 'claim')
train = drop_nan(train, 'claim')
# --- cell ---
# train.isnull().sum()
train.isnull().sum()
# --- cell ---
# train.drop(columns=['risk_score'], inplace=True)
train.drop(columns=['risk_score'], inplace=True)
# --- cell ---
# test.drop(columns=['risk_score'], inplace=True)
test.drop(columns=['risk_score'], inplace=True)
# --- cell ---
# mode_cols_test = [ 'has_garden','Geo_Code']
mode_cols_test = [ 'has_garden','Geo_Code']
# ligne vide

# for col in mode_cols_test:
for col in mode_cols_test:
#     test = impute_mode(test, col)
    test = impute_mode(test, col)
# ligne vide

# median_cols_test = ['area_m2']
median_cols_test = ['area_m2']
# for col in median_cols_test:
for col in median_cols_test:
#     test = impute_median(test, col)
    test = impute_median(test, col)
# --- cell ---
# test.isnull().sum()
test.isnull().sum()
# --- cell ---
# train['Geo_Code'] = pd.to_numeric(train['Geo_Code'], errors='coerce')
train['Geo_Code'] = pd.to_numeric(train['Geo_Code'], errors='coerce')
# train.dropna(subset=["Geo_Code"],axis=0, inplace=True)
train.dropna(subset=["Geo_Code"],axis=0, inplace=True)
# train['Geo_Code'].astype("int64")
train['Geo_Code'].astype("int64")
# enc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='quantile', subsample=len(train))                                      
enc = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='quantile', subsample=len(train))                                      
# ligne vide

# train['Geo_Code'] = enc.fit_transform(train[['Geo_Code']])
train['Geo_Code'] = enc.fit_transform(train[['Geo_Code']])
# train
train
# --- cell ---
# test['Geo_Code'] = pd.to_numeric(test['Geo_Code'], errors='coerce')
test['Geo_Code'] = pd.to_numeric(test['Geo_Code'], errors='coerce')
# test.dropna(subset=["Geo_Code"],axis=0, inplace=True)
test.dropna(subset=["Geo_Code"],axis=0, inplace=True)
# test['Geo_Code'].astype("int64")
test['Geo_Code'].astype("int64")
# enc = KBinsDiscretizer(n_bins=10, encode='ordinal',strategy='quantile', subsample=len(test))
enc = KBinsDiscretizer(n_bins=10, encode='ordinal',strategy='quantile', subsample=len(test))
# test['Geo_Code'] = enc.fit_transform(test[['Geo_Code']])
test['Geo_Code'] = enc.fit_transform(test[['Geo_Code']])
# test
test
# --- cell ---
# l_num=list(train.select_dtypes(include="number"))
l_num=list(train.select_dtypes(include="number"))
# print(l_num)
print(l_num)
# --- cell ---
# sns.boxplot(data=train[l_num])
sns.boxplot(data=train[l_num])
# plt.show()
plt.show()
# --- cell ---
# sns.boxplot(data=test[l_num])
sns.boxplot(data=test[l_num])
# plt.show()
plt.show()
# --- cell ---
# train.describe(include='all')
train.describe(include='all')
# --- cell ---
# def boxplot_treatment(df):
def boxplot_treatment(df):
#   Q1,Q3=np.percentile(df["area_m2"],[25,75])
  Q1,Q3=np.percentile(df["area_m2"],[25,75])
#   IQR=Q3-Q1
  IQR=Q3-Q1
#   lower_limit=max(Q1 - 1.5 * IQR, df["area_m2"].min()+100) 
  lower_limit=max(Q1 - 1.5 * IQR, df["area_m2"].min()+100) 
#   upper_limit=Q3+1.5*IQR
  upper_limit=Q3+1.5*IQR
#   df['area_m2']=np.where(df['area_m2']>=upper_limit,
  df['area_m2']=np.where(df['area_m2']>=upper_limit,
#   upper_limit,df['area_m2'])
  upper_limit,df['area_m2'])
#   return df
  return df
# train=boxplot_treatment(train)
train=boxplot_treatment(train)
# test=boxplot_treatment(test)
test=boxplot_treatment(test)
# --- cell ---
# train.describe(include='all')
train.describe(include='all')
# --- cell ---
# sns.boxplot(data=train[['area_m2']])
sns.boxplot(data=train[['area_m2']])
# plt.show()
plt.show()
# --- cell ---
# sns.boxplot(data=test[['area_m2']])
sns.boxplot(data=test[['area_m2']])
# plt.show()
plt.show()
# --- cell ---
# train[['is_finished', 'is_fenced']] = train['is_finished_and_fenced'].str.split('/', expand=True)
train[['is_finished', 'is_fenced']] = train['is_finished_and_fenced'].str.split('/', expand=True)
# train =train.drop('is_finished_and_fenced', axis=1)
train =train.drop('is_finished_and_fenced', axis=1)
# train['is_finished'] = train['is_finished'].map({'N':0, 'V':1})
train['is_finished'] = train['is_finished'].map({'N':0, 'V':1})
# train['is_fenced']   = train['is_fenced'].map({'N':0, 'V':1})
train['is_fenced']   = train['is_fenced'].map({'N':0, 'V':1})
# train.head()
train.head()
# --- cell ---
# test[['is_finished', 'is_fenced']] = test['is_finished_and_fenced'].str.split('/', expand=True)
test[['is_finished', 'is_fenced']] = test['is_finished_and_fenced'].str.split('/', expand=True)
# test = test.drop('is_finished_and_fenced', axis=1)
test = test.drop('is_finished_and_fenced', axis=1)
# test['is_finished'] = test['is_finished'].map({'N':0, 'V':1})
test['is_finished'] = test['is_finished'].map({'N':0, 'V':1})
# test['is_fenced']   = test['is_fenced'].map({'N':0, 'V':1})
test['is_fenced']   = test['is_fenced'].map({'N':0, 'V':1})
# test.head()
test.head()
# --- cell ---
# enc = OrdinalEncoder()
enc = OrdinalEncoder()
# train[["is_residential"]]=enc.fit_transform(
train[["is_residential"]]=enc.fit_transform(
# train.loc[:,["is_residential"]])
train.loc[:,["is_residential"]])
# ligne vide

# ligne vide

# enc = OrdinalEncoder()
enc = OrdinalEncoder()
# train[["claim"]]=enc.fit_transform(
train[["claim"]]=enc.fit_transform(
# train.loc[:,["claim"]])
train.loc[:,["claim"]])
# ligne vide

# enc = OrdinalEncoder()
enc = OrdinalEncoder()
# train[["locality"]]=enc.fit_transform(
train[["locality"]]=enc.fit_transform(
# train.loc[:,["locality"]])
train.loc[:,["locality"]])
# ligne vide

# enc = OrdinalEncoder()
enc = OrdinalEncoder()
# train[["has_garden"]]=enc.fit_transform(
train[["has_garden"]]=enc.fit_transform(
# train.loc[:,["has_garden"]])
train.loc[:,["has_garden"]])
# ligne vide

# train = pd.get_dummies(train, columns=['structure_type'], dtype='int32', prefix='', prefix_sep='')
train = pd.get_dummies(train, columns=['structure_type'], dtype='int32', prefix='', prefix_sep='')
# claim_column = train.pop('claim')
claim_column = train.pop('claim')
# train = pd.concat([train, claim_column], axis=1)
train = pd.concat([train, claim_column], axis=1)
# ligne vide

# train =train.drop('policy_id', axis=1)
train =train.drop('policy_id', axis=1)
# train
train
# --- cell ---
# enc = OrdinalEncoder()
enc = OrdinalEncoder()
# test[["is_residential"]] = enc.fit_transform(
test[["is_residential"]] = enc.fit_transform(
#     test.loc[:, ["is_residential"]]
    test.loc[:, ["is_residential"]]
# )
)
# ligne vide

# enc = OrdinalEncoder()
enc = OrdinalEncoder()
# test[["claim"]] = enc.fit_transform(
test[["claim"]] = enc.fit_transform(
#     test.loc[:, ["claim"]]
    test.loc[:, ["claim"]]
# )
)
# ligne vide

# enc = OrdinalEncoder()
enc = OrdinalEncoder()
# test[["locality"]] = enc.fit_transform(
test[["locality"]] = enc.fit_transform(
#     test.loc[:, ["locality"]]
    test.loc[:, ["locality"]]
# )
)
# ligne vide

# enc = OrdinalEncoder()
enc = OrdinalEncoder()
# test[["has_garden"]]=enc.fit_transform(
test[["has_garden"]]=enc.fit_transform(
# test.loc[:,["has_garden"]])
test.loc[:,["has_garden"]])
# ligne vide

# ligne vide

# test = pd.get_dummies(test, columns=['structure_type'], dtype='int32', prefix='', prefix_sep='')
test = pd.get_dummies(test, columns=['structure_type'], dtype='int32', prefix='', prefix_sep='')
# ligne vide

# claim_column = test.pop('claim')
claim_column = test.pop('claim')
# test = pd.concat([test, claim_column], axis=1)
test = pd.concat([test, claim_column], axis=1)
# ligne vide

# test = test.drop('policy_id', axis=1)
test = test.drop('policy_id', axis=1)
# test
test
# --- cell ---
# df_train = train.corr(numeric_only=True)
df_train = train.corr(numeric_only=True)
# plt.figure(figsize=(12, 10))
plt.figure(figsize=(12, 10))
# sns.heatmap(df_train, annot=True, vmin=-1, vmax=1, cmap="coolwarm")
sns.heatmap(df_train, annot=True, vmin=-1, vmax=1, cmap="coolwarm")
# plt.title('Matrice de Corrélation')
plt.title('Matrice de Corrélation')
# plt.show()
plt.show()
# --- cell ---
# df_test = test.corr(numeric_only=True)
df_test = test.corr(numeric_only=True)
# plt.figure(figsize=(12, 10))
plt.figure(figsize=(12, 10))
# sns.heatmap(df_test, annot=True, vmin=-1, vmax=1, cmap="coolwarm")
sns.heatmap(df_test, annot=True, vmin=-1, vmax=1, cmap="coolwarm")
# plt.title('Matrice de Corrélation')
plt.title('Matrice de Corrélation')
# plt.show()
plt.show()
# --- cell ---
# train =train.drop('year', axis=1)                                                             
train =train.drop('year', axis=1)                                                             
# ligne vide

# train =train.drop('is_finished', axis=1)
train =train.drop('is_finished', axis=1)
# train =train.drop('is_fenced', axis=1)
train =train.drop('is_fenced', axis=1)
# train =train.drop('has_garden', axis=1)
train =train.drop('has_garden', axis=1)
# train =train.drop('locality', axis=1)
train =train.drop('locality', axis=1)
# train
train
# --- cell ---
# test = test.drop('year', axis=1)          
test = test.drop('year', axis=1)          
# ligne vide

# test = test.drop('is_finished', axis=1)
test = test.drop('is_finished', axis=1)
# test = test.drop('is_fenced', axis=1)
test = test.drop('is_fenced', axis=1)
# test = test.drop('has_garden', axis=1)
test = test.drop('has_garden', axis=1)
# test = test.drop('locality', axis=1)
test = test.drop('locality', axis=1)
# test
test
# --- cell ---
# train1=train[train.duplicated()]
train1=train[train.duplicated()]
# train1
train1
# --- cell ---
# train.drop_duplicates(inplace=True, ignore_index=True)
train.drop_duplicates(inplace=True, ignore_index=True)
# train
train
# --- cell ---
# train1=train[train.duplicated()]
train1=train[train.duplicated()]
# train1
train1
# --- cell ---
# test1=test[test.duplicated()]
test1=test[test.duplicated()]
# test1
test1
# --- cell ---
# test.drop_duplicates(inplace=True, ignore_index=True)
test.drop_duplicates(inplace=True, ignore_index=True)
# test
test
# --- cell ---
# test1=test[test.duplicated()]
test1=test[test.duplicated()]
# test1
test1
# --- cell ---
# sns.kdeplot(train['area_m2'],bw_method='scott',bw_adjust=1)
sns.kdeplot(train['area_m2'],bw_method='scott',bw_adjust=1)
# plt.show()
plt.show()
# --- cell ---
# sns.kdeplot(test['area_m2'],bw_method='scott',bw_adjust=1)
sns.kdeplot(test['area_m2'],bw_method='scott',bw_adjust=1)
# plt.show()
plt.show()
# --- cell ---
# --- cell ---
# plt.figure(figsize=(8, 6))
plt.figure(figsize=(8, 6))
# train['claim'].value_counts().plot(kind='bar')
train['claim'].value_counts().plot(kind='bar')
# plt.title('Distribution of Insurance Claims')
plt.title('Distribution of Insurance Claims')
# plt.xlabel('Claim')
plt.xlabel('Claim')
# plt.ylabel('Count')
plt.ylabel('Count')
# plt.show()
plt.show()
# --- cell ---
# train['coverage_period'] = train['coverage_period'].astype(str).str.replace(',', '.').astype('float64')
train['coverage_period'] = train['coverage_period'].astype(str).str.replace(',', '.').astype('float64')
# test['coverage_period'] = test['coverage_period'].astype(str).str.replace(',', '.').astype('float64')
test['coverage_period'] = test['coverage_period'].astype(str).str.replace(',', '.').astype('float64')
# --- cell ---
# from imblearn.combine import SMOTETomek
from imblearn.combine import SMOTETomek
# from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
# import pandas as pd
import pandas as pd
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# ligne vide

# X = train.drop('claim', axis=1)
X = train.drop('claim', axis=1)
# y = train['claim']
y = train['claim']
# ligne vide

# smote_tomek = SMOTETomek(random_state=42)
smote_tomek = SMOTETomek(random_state=42)
# X_resampled, y_resampled = smote_tomek.fit_resample(X, y)
X_resampled, y_resampled = smote_tomek.fit_resample(X, y)
# ligne vide

# print("Après rééquilibrage :", pd.Series(y_resampled).value_counts())
print("Après rééquilibrage :", pd.Series(y_resampled).value_counts())
# ligne vide

# plt.figure(figsize=(8, 6))
plt.figure(figsize=(8, 6))
# pd.Series(y_resampled).value_counts().plot(kind='bar')
pd.Series(y_resampled).value_counts().plot(kind='bar')
# plt.title('Distribution of Insurance Claims (After SMOTETomek)')
plt.title('Distribution of Insurance Claims (After SMOTETomek)')
# plt.xlabel('Claim')
plt.xlabel('Claim')
# plt.ylabel('Count')
plt.ylabel('Count')
# plt.show()
plt.show()
# ligne vide

# scaler = StandardScaler()
scaler = StandardScaler()
# X_rescaled = scaler.fit_transform(X_resampled)
X_rescaled = scaler.fit_transform(X_resampled)
# ligne vide

# X_train, X_val, Y_train, Y_val = train_test_split(
X_train, X_val, Y_train, Y_val = train_test_split(
#     X_rescaled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
    X_rescaled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
# )
)
# ligne vide

# print("X_train shape:", X_train.shape)
print("X_train shape:", X_train.shape)
# print("X_val shape:", X_val.shape)
print("X_val shape:", X_val.shape)
# print("Distribution Y_train:n", pd.Series(Y_train).value_counts())
print("Distribution Y_train:n", pd.Series(Y_train).value_counts())
# print("Distribution Y_val:n", pd.Series(Y_val).value_counts())
print("Distribution Y_val:n", pd.Series(Y_val).value_counts())
# --- cell ---
# train['window_count'] = pd.to_numeric(train['window_count']).astype('float64')
train['window_count'] = pd.to_numeric(train['window_count']).astype('float64')
# test['window_count']  = pd.to_numeric(test['window_count']).astype('float64')
test['window_count']  = pd.to_numeric(test['window_count']).astype('float64')
# ligne vide

# ligne vide

# ligne vide

# X_train = train.iloc[:, :-1].values
X_train = train.iloc[:, :-1].values
# Y_train = train.iloc[:, -1].values
Y_train = train.iloc[:, -1].values
# ligne vide

# X_test  = test.iloc[:, :-1].values
X_test  = test.iloc[:, :-1].values
# Y_test  = test.iloc[:, -1].values
Y_test  = test.iloc[:, -1].values
# --- cell ---
# import pandas as pd
import pandas as pd
# import numpy as np
import numpy as np
# from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
# from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score
# import seaborn as sns
import seaborn as sns
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# ligne vide

# ligne vide

# cls = DecisionTreeClassifier(max_depth=3)
cls = DecisionTreeClassifier(max_depth=3)
# cls.fit(X_train, Y_train)
cls.fit(X_train, Y_train)
# ligne vide

# fig = plt.figure(figsize=(15, 10))
fig = plt.figure(figsize=(15, 10))
# plot_tree(cls, feature_names=list(train)[:-1], class_names=[str(cls_class) for cls_class in cls.classes_], filled=True)
plot_tree(cls, feature_names=list(train)[:-1], class_names=[str(cls_class) for cls_class in cls.classes_], filled=True)
# plt.show()
plt.show()
# ligne vide

# print(export_text(cls, feature_names=list(train)[:-1]))
print(export_text(cls, feature_names=list(train)[:-1]))
# ligne vide

# Y_p_train = cls.predict(X_train)
Y_p_train = cls.predict(X_train)
# c_m_train = confusion_matrix(Y_train, Y_p_train)
c_m_train = confusion_matrix(Y_train, Y_p_train)
# ligne vide

# accuracy_train = accuracy_score(Y_train, Y_p_train)
accuracy_train = accuracy_score(Y_train, Y_p_train)
# ligne vide

# sns.heatmap(c_m_train, annot=True, cbar=False, xticklabels=[str(cls_class) for cls_class in cls.classes_], yticklabels=[str(cls_class) for cls_class in cls.classes_], fmt='d')
sns.heatmap(c_m_train, annot=True, cbar=False, xticklabels=[str(cls_class) for cls_class in cls.classes_], yticklabels=[str(cls_class) for cls_class in cls.classes_], fmt='d')
# plt.title('Confusion Matrix (Training Set)')
plt.title('Confusion Matrix (Training Set)')
# plt.show()
plt.show()
# ligne vide

# print(f"Accuracy on the training set: {accuracy_train:.2%}")
print(f"Accuracy on the training set: {accuracy_train:.2%}")
# ligne vide

# Y_p_test = cls.predict(X_test)
Y_p_test = cls.predict(X_test)
# c_m_test = confusion_matrix(Y_test, Y_p_test)
c_m_test = confusion_matrix(Y_test, Y_p_test)
# ligne vide

# accuracy_test = accuracy_score(Y_test, Y_p_test)
accuracy_test = accuracy_score(Y_test, Y_p_test)
# ligne vide

# sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=[str(cls_class) for cls_class in cls.classes_], yticklabels=[str(cls_class) for cls_class in cls.classes_], fmt='d')
sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=[str(cls_class) for cls_class in cls.classes_], yticklabels=[str(cls_class) for cls_class in cls.classes_], fmt='d')
# plt.title('Confusion Matrix (Test Set)')
plt.title('Confusion Matrix (Test Set)')
# plt.show()
plt.show()
# ligne vide

# print(f"Accuracy on the test set: {accuracy_test:.2%}")
print(f"Accuracy on the test set: {accuracy_test:.2%}")
# print("Training and testing completed.")
print("Training and testing completed.")
# --- cell ---
# from sklearn.metrics import precision_recall_fscore_support, roc_curve, roc_auc_score
from sklearn.metrics import precision_recall_fscore_support, roc_curve, roc_auc_score
# precision,recall,f1,occ= precision_recall_fscore_support(Y_train,
precision,recall,f1,occ= precision_recall_fscore_support(Y_train,
# Y_p_train, average=None)
Y_p_train, average=None)
# print(precision, recall, f1, occ)
print(precision, recall, f1, occ)
# y_train_prob=cls.predict_proba(X_train)[:,1]
y_train_prob=cls.predict_proba(X_train)[:,1]
# fpr,tpr,thresholds = roc_curve(Y_train,y_train_prob,pos_label=1)
fpr,tpr,thresholds = roc_curve(Y_train,y_train_prob,pos_label=1)
# auc = roc_auc_score(Y_train, y_train_prob)
auc = roc_auc_score(Y_train, y_train_prob)
# plt.plot(fpr, tpr)
plt.plot(fpr, tpr)
# plt.xlabel('False Positive Rate')
plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
plt.ylabel('True Positive Rate')
# plt.text(0.6, 0.2, f'AUC = {auc:.2f}',
plt.text(0.6, 0.2, f'AUC = {auc:.2f}',
#  color='blue',fontsize=12)
 color='blue',fontsize=12)
# plt.show()
plt.show()
# precision,recall,f1,occ= precision_recall_fscore_support(Y_test,
precision,recall,f1,occ= precision_recall_fscore_support(Y_test,
# Y_p_test, average=None)
Y_p_test, average=None)
# print(precision, recall, f1, occ)
print(precision, recall, f1, occ)
# y_test_prob=cls.predict_proba(X_test)[:,1]
y_test_prob=cls.predict_proba(X_test)[:,1]
# fpr,tpr,thresholds = roc_curve(Y_test,y_test_prob,pos_label=1)
fpr,tpr,thresholds = roc_curve(Y_test,y_test_prob,pos_label=1)
# auc = roc_auc_score(Y_test, y_test_prob)
auc = roc_auc_score(Y_test, y_test_prob)
# plt.plot(fpr, tpr)
plt.plot(fpr, tpr)
# plt.xlabel('False Positive Rate')
plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
plt.ylabel('True Positive Rate')
# plt.text(0.6, 0.2, f'AUC = {auc:.2f}',
plt.text(0.6, 0.2, f'AUC = {auc:.2f}',
#  color='blue',fontsize=12)
 color='blue',fontsize=12)
# plt.show()
plt.show()
# --- cell ---
# complement_recall = 1 - recall
complement_recall = 1 - recall
# print("Class-wise complement of recall:")
print("Class-wise complement of recall:")
# for i, class_label in enumerate(cls.classes_):
for i, class_label in enumerate(cls.classes_):
#     print(f"Class {class_label}: {complement_recall[i]:.2%}")
    print(f"Class {class_label}: {complement_recall[i]:.2%}")
# complement_precision = 1 - precision
complement_precision = 1 - precision
# print("Class-wise complement of precision:")
print("Class-wise complement of precision:")
# for i, class_label in enumerate(cls.classes_):
for i, class_label in enumerate(cls.classes_):
#     print(f"Class {class_label}: {complement_precision[i]:.2%}")
    print(f"Class {class_label}: {complement_precision[i]:.2%}")
# --- cell ---
# import pandas as pd
import pandas as pd
# import numpy as np
import numpy as np
# from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score
# import seaborn as sns
import seaborn as sns
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# ligne vide

# ligne vide

# cls = RandomForestClassifier(
cls = RandomForestClassifier(
#     n_estimators=100,                                 
    n_estimators=100,                                 
#     criterion='gini',                                       
    criterion='gini',                                       
# ligne vide

#     max_depth=None,                                                         
    max_depth=None,                                                         
#     min_samples_split=2,                                                      
    min_samples_split=2,                                                      
#     min_samples_leaf=1,                                                  
    min_samples_leaf=1,                                                  
#     max_features='sqrt',                                                                                      
    max_features='sqrt',                                                                                      
#     max_leaf_nodes=None,                                                     
    max_leaf_nodes=None,                                                     
#     bootstrap=True,                                                          
    bootstrap=True,                                                          
#     oob_score=True,                              
    oob_score=True,                              
#     max_samples=0.53                                                                
    max_samples=0.53                                                                
# )
)
# cls.fit(X_train, Y_train)
cls.fit(X_train, Y_train)
# ligne vide

# Y_p_train = cls.predict(X_train)
Y_p_train = cls.predict(X_train)
# c_m_train = confusion_matrix(Y_train, Y_p_train)
c_m_train = confusion_matrix(Y_train, Y_p_train)
# ligne vide

# accuracy_train = accuracy_score(Y_train, Y_p_train)
accuracy_train = accuracy_score(Y_train, Y_p_train)
# ligne vide

# sns.heatmap(c_m_train, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_train, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Training Set)')
plt.title('Confusion Matrix (Training Set)')
# plt.show()
plt.show()
# ligne vide

# print(f"Accuracy on the training set: {accuracy_train:.2%}")
print(f"Accuracy on the training set: {accuracy_train:.2%}")
# ligne vide

# Y_p_test = cls.predict(X_test)
Y_p_test = cls.predict(X_test)
# c_m_test = confusion_matrix(Y_test, Y_p_test)
c_m_test = confusion_matrix(Y_test, Y_p_test)
# ligne vide

# accuracy_test = accuracy_score(Y_test, Y_p_test)
accuracy_test = accuracy_score(Y_test, Y_p_test)
# ligne vide

# sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Test Set)')
plt.title('Confusion Matrix (Test Set)')
# plt.show()
plt.show()
# ligne vide

# print(f"Accuracy on the test set: {accuracy_test:.2%}")
print(f"Accuracy on the test set: {accuracy_test:.2%}")
# print("Training and testing completed.")
print("Training and testing completed.")
# --- cell ---
# from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
# ligne vide

# cls= RandomForestClassifier(n_estimators=100,                            
cls= RandomForestClassifier(n_estimators=100,                            
#     criterion='gini',                                 
    criterion='gini',                                 
#     class_weight='balanced',                                                                  
    class_weight='balanced',                                                                  
#     max_depth=None,                               
    max_depth=None,                               
#     min_samples_split=2,                                               
    min_samples_split=2,                                               
#  min_samples_leaf=1,                                          
 min_samples_leaf=1,                                          
#  max_features='sqrt',                                                   
 max_features='sqrt',                                                   
#  max_leaf_nodes=None,                                           
 max_leaf_nodes=None,                                           
# bootstrap=True,                            
bootstrap=True,                            
# oob_score=True,                              
oob_score=True,                              
# max_samples=0.53 )                                                   
max_samples=0.53 )                                                   
# cls.fit(X_train, Y_train)
cls.fit(X_train, Y_train)
# --- cell ---
# import pandas as pd
import pandas as pd
# import numpy as np
import numpy as np
# from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score
# import seaborn as sns
import seaborn as sns
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# ligne vide

# ligne vide

# ligne vide

# Y_p_train = cls.predict(X_train)
Y_p_train = cls.predict(X_train)
# c_m_train = confusion_matrix(Y_train, Y_p_train)
c_m_train = confusion_matrix(Y_train, Y_p_train)
# ligne vide

# accuracy_train = accuracy_score(Y_train, Y_p_train)
accuracy_train = accuracy_score(Y_train, Y_p_train)
# print(c_m_train)
print(c_m_train)
# sns.heatmap(c_m_train, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_train, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Training Set)')
plt.title('Confusion Matrix (Training Set)')
# plt.show()
plt.show()
# ligne vide

# print(f"Accuracy on the test set: {accuracy_test:.2%}")
print(f"Accuracy on the test set: {accuracy_test:.2%}")
# ligne vide

# Y_p_test = cls.predict(X_test)
Y_p_test = cls.predict(X_test)
# c_m_test = confusion_matrix(Y_test, Y_p_test)
c_m_test = confusion_matrix(Y_test, Y_p_test)
# ligne vide

# accuracy_test = accuracy_score(Y_test, Y_p_test)
accuracy_test = accuracy_score(Y_test, Y_p_test)
# print(c_m_test)
print(c_m_test)
# sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Test Set)')
plt.title('Confusion Matrix (Test Set)')
# plt.show()
plt.show()
# ligne vide

# print(f"Accuracy on the test set: {accuracy_test:.2%}")
print(f"Accuracy on the test set: {accuracy_test:.2%}")
# print("Training and testing completed.")
print("Training and testing completed.")
# --- cell ---
# import pandas as pd
import pandas as pd
# import numpy as np
import numpy as np
# from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score
# from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import RandomOverSampler
# import seaborn as sns
import seaborn as sns
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# ligne vide

# ligne vide

# cls = RandomForestClassifier(
cls = RandomForestClassifier(
#     n_estimators=100,              
    n_estimators=100,              
#     criterion='gini',                
    criterion='gini',                
#     max_depth=None,                               
    max_depth=None,                               
#     min_samples_split=2,                                       
    min_samples_split=2,                                       
#     min_samples_leaf=1,                                     
    min_samples_leaf=1,                                     
#     max_features='sqrt',                                       
    max_features='sqrt',                                       
#     max_leaf_nodes=None,                             
    max_leaf_nodes=None,                             
#     bootstrap=True,                    
    bootstrap=True,                    
#     oob_score=True,                           
    oob_score=True,                           
#     max_samples=0.53                                  
    max_samples=0.53                                  
# )
)
# cls.fit(X_train, Y_train)
cls.fit(X_train, Y_train)
# ligne vide

# Y_p_test = cls.predict(X_test)
Y_p_test = cls.predict(X_test)
# c_m_test = confusion_matrix(Y_test, Y_p_test)
c_m_test = confusion_matrix(Y_test, Y_p_test)
# ligne vide

# sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Test Set) - Original Model')
plt.title('Confusion Matrix (Test Set) - Original Model')
# plt.show()
plt.show()
# ligne vide

# accuracy_test = accuracy_score(Y_test, Y_p_test)
accuracy_test = accuracy_score(Y_test, Y_p_test)
# print(f"Accuracy on the test set: {accuracy_test:.2%}")
print(f"Accuracy on the test set: {accuracy_test:.2%}")
# ligne vide

# ros = RandomOverSampler(sampling_strategy={1.0: 6000})
ros = RandomOverSampler(sampling_strategy={1.0: 6000})
# X_train_resampled, Y_train_resampled = ros.fit_resample(X_train, Y_train)
X_train_resampled, Y_train_resampled = ros.fit_resample(X_train, Y_train)
# ligne vide

# cls.fit(X_train_resampled, Y_train_resampled)
cls.fit(X_train_resampled, Y_train_resampled)
# Y_p_test = cls.predict(X_test)
Y_p_test = cls.predict(X_test)
# c_m_test = confusion_matrix(Y_test, Y_p_test)
c_m_test = confusion_matrix(Y_test, Y_p_test)
# ligne vide

# sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Test Set) - Over-sampling "no" class')
plt.title('Confusion Matrix (Test Set) - Over-sampling "no" class')
# plt.show()
plt.show()
# ligne vide

# accuracy_test = accuracy_score(Y_test, Y_p_test)
accuracy_test = accuracy_score(Y_test, Y_p_test)
# print(f"Accuracy on the test set (with over-sampling): {accuracy_test:.2%}")
print(f"Accuracy on the test set (with over-sampling): {accuracy_test:.2%}")
# --- cell ---
# import pandas as pd
import pandas as pd
# import numpy as np
import numpy as np
# from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score
# from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import RandomUnderSampler
# import seaborn as sns
import seaborn as sns
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# ligne vide

# ligne vide

# cls = RandomForestClassifier(
cls = RandomForestClassifier(
#     n_estimators=100,              
    n_estimators=100,              
#     criterion='gini',                
    criterion='gini',                
#     max_depth=None,                               
    max_depth=None,                               
#     min_samples_split=2,                                       
    min_samples_split=2,                                       
#     min_samples_leaf=1,                                     
    min_samples_leaf=1,                                     
#     max_features='sqrt',                                       
    max_features='sqrt',                                       
#     max_leaf_nodes=None,                             
    max_leaf_nodes=None,                             
#     bootstrap=True,                    
    bootstrap=True,                    
#     oob_score=True,                    
    oob_score=True,                    
#     max_samples=0.53                                  
    max_samples=0.53                                  
# )
)
# cls.fit(X_train, Y_train)
cls.fit(X_train, Y_train)
# ligne vide

# Y_p_test = cls.predict(X_test)
Y_p_test = cls.predict(X_test)
# c_m_test = confusion_matrix(Y_test, Y_p_test)
c_m_test = confusion_matrix(Y_test, Y_p_test)
# ligne vide

# sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Test Set) - Original Model')
plt.title('Confusion Matrix (Test Set) - Original Model')
# plt.show()
plt.show()
# ligne vide

# accuracy_test = accuracy_score(Y_test, Y_p_test)
accuracy_test = accuracy_score(Y_test, Y_p_test)
# print(f"Accuracy on the test set: {accuracy_test:.2%}")
print(f"Accuracy on the test set: {accuracy_test:.2%}")
# ligne vide

# rus = RandomUnderSampler(sampling_strategy={0.0: 1000})
rus = RandomUnderSampler(sampling_strategy={0.0: 1000})
# X_train_resampled, Y_train_resampled = rus.fit_resample(X_train, Y_train)
X_train_resampled, Y_train_resampled = rus.fit_resample(X_train, Y_train)
# ligne vide

# cls.fit(X_train_resampled, Y_train_resampled)
cls.fit(X_train_resampled, Y_train_resampled)
# Y_p_test = cls.predict(X_test)
Y_p_test = cls.predict(X_test)
# c_m_test = confusion_matrix(Y_test, Y_p_test)
c_m_test = confusion_matrix(Y_test, Y_p_test)
# ligne vide

# sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Test Set) - Under-sampling "yes" class')
plt.title('Confusion Matrix (Test Set) - Under-sampling "yes" class')
# plt.show()
plt.show()
# ligne vide

# accuracy_test = accuracy_score(Y_test, Y_p_test)
accuracy_test = accuracy_score(Y_test, Y_p_test)
# print(f"Accuracy on the test set (with under-sampling): {accuracy_test:.2%}")
print(f"Accuracy on the test set (with under-sampling): {accuracy_test:.2%}")
# --- cell ---
# import pandas as pd
import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
# import seaborn as sns
import seaborn as sns
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# ligne vide

# ligne vide

# cls = DecisionTreeClassifier(criterion='entropy', random_state=42)
cls = DecisionTreeClassifier(criterion='entropy', random_state=42)
# cls.fit(X_train, Y_train)
cls.fit(X_train, Y_train)
# ligne vide

# Y_p_train = cls.predict(X_train)
Y_p_train = cls.predict(X_train)
# c_m_train = confusion_matrix(Y_train, Y_p_train)
c_m_train = confusion_matrix(Y_train, Y_p_train)
# ligne vide

# sns.heatmap(c_m_train, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_train, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Train Set) - Decision Tree without Oversampling')
plt.title('Confusion Matrix (Train Set) - Decision Tree without Oversampling')
# plt.show()
plt.show()
# ligne vide

# print("Classification Report:")
print("Classification Report:")
# print(classification_report(Y_train, Y_p_train))
print(classification_report(Y_train, Y_p_train))
# ligne vide

# accuracy_test = accuracy_score(Y_train, Y_p_train)
accuracy_test = accuracy_score(Y_train, Y_p_train)
# print(f"Accuracy on the test set: {accuracy_test:.2%}")
print(f"Accuracy on the test set: {accuracy_test:.2%}")
# ligne vide

# threshold = 0.0005                                                      
threshold = 0.0005                                                      
# Y_p_train_adjusted = (cls.predict_proba(X_train)[:, 1] > threshold).astype(int)
Y_p_train_adjusted = (cls.predict_proba(X_train)[:, 1] > threshold).astype(int)
# ligne vide

# print("nClassification Report (Adjusted Threshold):")
print("nClassification Report (Adjusted Threshold):")
# print(classification_report(Y_train, Y_p_train_adjusted))
print(classification_report(Y_train, Y_p_train_adjusted))
# ligne vide

# accuracy_train_adjusted = accuracy_score(Y_train, Y_p_train_adjusted)
accuracy_train_adjusted = accuracy_score(Y_train, Y_p_train_adjusted)
# print(f"Accuracy on the training set (Adjusted Threshold): {accuracy_train_adjusted:.2%}")
print(f"Accuracy on the training set (Adjusted Threshold): {accuracy_train_adjusted:.2%}")
# ligne vide

# Y_p_test = cls.predict(X_test)
Y_p_test = cls.predict(X_test)
# c_m_test = confusion_matrix(Y_test, Y_p_test)
c_m_test = confusion_matrix(Y_test, Y_p_test)
# ligne vide

# sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
sns.heatmap(c_m_test, annot=True, cbar=False, xticklabels=cls.classes_, yticklabels=cls.classes_, fmt='d')
# plt.title('Confusion Matrix (Test Set) - Decision Tree without Oversampling')
plt.title('Confusion Matrix (Test Set) - Decision Tree without Oversampling')
# plt.show()
plt.show()
# ligne vide

# print("Classification Report:")
print("Classification Report:")
# print(classification_report(Y_test, Y_p_test))
print(classification_report(Y_test, Y_p_test))
# ligne vide

# accuracy_test = accuracy_score(Y_test, Y_p_test)
accuracy_test = accuracy_score(Y_test, Y_p_test)
# print(f"Accuracy on the test set: {accuracy_test:.2%}")
print(f"Accuracy on the test set: {accuracy_test:.2%}")
# ligne vide

# threshold = 0.0005                
threshold = 0.0005                
# Y_p_test_adjusted = (cls.predict_proba(X_test)[:, 1] > threshold).astype(int)
Y_p_test_adjusted = (cls.predict_proba(X_test)[:, 1] > threshold).astype(int)
# ligne vide

# print("nClassification Report (Adjusted Threshold):")
print("nClassification Report (Adjusted Threshold):")
# print(classification_report(Y_test, Y_p_test_adjusted))
print(classification_report(Y_test, Y_p_test_adjusted))
# ligne vide

# accuracy_test_adjusted = accuracy_score(Y_test, Y_p_test_adjusted)
accuracy_test_adjusted = accuracy_score(Y_test, Y_p_test_adjusted)
# print(f"Accuracy on the test set (Adjusted Threshold): {accuracy_test_adjusted:.2%}")
print(f"Accuracy on the test set (Adjusted Threshold): {accuracy_test_adjusted:.2%}")
# --- cell ---
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
# from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC
from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report, roc_auc_score, roc_curve
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# import seaborn as sns
import seaborn as sns
# ligne vide

# models = {
models = {
#     "Random Forest": RandomForestClassifier(),                                              
    "Random Forest": RandomForestClassifier(),                                              
#     "Gradient Boosting": GradientBoostingClassifier(),                                                
    "Gradient Boosting": GradientBoostingClassifier(),                                                
#     "Logistic Regression": LogisticRegression(max_iter=1000),                                                  
    "Logistic Regression": LogisticRegression(max_iter=1000),                                                  
#     "SVM": SVC(probability=True),                                                       
    "SVM": SVC(probability=True),                                                       
#     "KNN": KNeighborsClassifier()                                                  
    "KNN": KNeighborsClassifier()                                                  
# }
}
# ligne vide

# for name, model in models.items():
for name, model in models.items():
#     print(f"=== {name} ===")
    print(f"=== {name} ===")
#     model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
# ligne vide

#     y_train_pred = model.predict(X_train)
    y_train_pred = model.predict(X_train)
#     y_test_pred = model.predict(X_test)
    y_test_pred = model.predict(X_test)
# ligne vide

#     y_train_prob = model.predict_proba(X_train)[:, 1] if hasattr(model, "predict_proba") else None
    y_train_prob = model.predict_proba(X_train)[:, 1] if hasattr(model, "predict_proba") else None
#     y_test_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None
    y_test_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None
# ligne vide

#     print(f"--- Évaluation sur le jeu d'entraînement ---")
    print(f"--- Évaluation sur le jeu d'entraînement ---")
#     print(f"Accuracy (train) : {accuracy_score(Y_train, y_train_pred):.2f}")
    print(f"Accuracy (train) : {accuracy_score(Y_train, y_train_pred):.2f}")
#     print(f"F1-score (train) : {f1_score(Y_train, y_train_pred):.2f}")
    print(f"F1-score (train) : {f1_score(Y_train, y_train_pred):.2f}")
# ligne vide

#     print(f"--- Évaluation sur le jeu de test ---")
    print(f"--- Évaluation sur le jeu de test ---")
#     print(f"Accuracy (test) : {accuracy_score(Y_test, y_test_pred):.2f}")
    print(f"Accuracy (test) : {accuracy_score(Y_test, y_test_pred):.2f}")
#     print(f"F1-score (test) : {f1_score(Y_test, y_test_pred):.2f}")
    print(f"F1-score (test) : {f1_score(Y_test, y_test_pred):.2f}")
#     print("Classification Report (test) :n", classification_report(Y_test, y_test_pred))
    print("Classification Report (test) :n", classification_report(Y_test, y_test_pred))
# ligne vide

#     cm = confusion_matrix(Y_test, y_test_pred)
    cm = confusion_matrix(Y_test, y_test_pred)
#     plt.figure(figsize=(6, 4))
    plt.figure(figsize=(6, 4))
#     sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
#     plt.title(f"Matrice de confusion - {name}")
    plt.title(f"Matrice de confusion - {name}")
#     plt.xlabel("Prédit")
    plt.xlabel("Prédit")
#     plt.ylabel("Réel")
    plt.ylabel("Réel")
#     plt.show()
    plt.show()
# ligne vide

#     if y_test_prob is not None:
    if y_test_prob is not None:
#         fpr_test, tpr_test, _ = roc_curve(Y_test, y_test_prob)
        fpr_test, tpr_test, _ = roc_curve(Y_test, y_test_prob)
#         auc_test = roc_auc_score(Y_test, y_test_prob)
        auc_test = roc_auc_score(Y_test, y_test_prob)
#         plt.figure(figsize=(6, 4))
        plt.figure(figsize=(6, 4))
#         plt.plot(fpr_test, tpr_test, label=f"ROC Curve (Test - AUC = {auc_test:.2f})")
        plt.plot(fpr_test, tpr_test, label=f"ROC Curve (Test - AUC = {auc_test:.2f})")
#         plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
        plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
#         plt.xlabel("Taux de Faux Positifs (FPR)")
        plt.xlabel("Taux de Faux Positifs (FPR)")
#         plt.ylabel("Taux de Vrais Positifs (TPR)")
        plt.ylabel("Taux de Vrais Positifs (TPR)")
#         plt.title(f"Courbe ROC (Test) - {name}")
        plt.title(f"Courbe ROC (Test) - {name}")
#         plt.legend(loc="lower right")
        plt.legend(loc="lower right")
#         plt.show()
        plt.show()
# ligne vide

#         fpr_train, tpr_train, _ = roc_curve(Y_train, y_train_prob)
        fpr_train, tpr_train, _ = roc_curve(Y_train, y_train_prob)
#         auc_train = roc_auc_score(Y_train, y_train_prob)
        auc_train = roc_auc_score(Y_train, y_train_prob)
#         plt.figure(figsize=(6, 4))
        plt.figure(figsize=(6, 4))
#         plt.plot(fpr_train, tpr_train, label=f"ROC Curve (Train - AUC = {auc_train:.2f})")
        plt.plot(fpr_train, tpr_train, label=f"ROC Curve (Train - AUC = {auc_train:.2f})")
#         plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
        plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
#         plt.xlabel("Taux de Faux Positifs (FPR)")
        plt.xlabel("Taux de Faux Positifs (FPR)")
#         plt.ylabel("Taux de Vrais Positifs (TPR)")
        plt.ylabel("Taux de Vrais Positifs (TPR)")
#         plt.title(f"Courbe ROC (Train) - {name}")
        plt.title(f"Courbe ROC (Train) - {name}")
#         plt.legend(loc="lower right")
        plt.legend(loc="lower right")
#         plt.show()
        plt.show()
# --- cell ---
# import numpy as np
import numpy as np
# import pandas as pd
import pandas as pd
# from sklearn.svm import SVC
from sklearn.svm import SVC
# from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPClassifier
# from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import RandomizedSearchCV
# from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
# import seaborn as sns
import seaborn as sns
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# ligne vide

# ligne vide

# svc_params = {
svc_params = {
#     'C': [0.1, 1, 10, 100],                                        
    'C': [0.1, 1, 10, 100],                                        
#     'kernel': ['rbf', 'poly'],                                                       
    'kernel': ['rbf', 'poly'],                                                       
#     'gamma': ['scale', 0.1]                        
    'gamma': ['scale', 0.1]                        
# }
}
# mlp_params = {
mlp_params = {
#     'hidden_layer_sizes': [(50,), (100,)],                                               
    'hidden_layer_sizes': [(50,), (100,)],                                               
#     'activation': ['relu'],                                
    'activation': ['relu'],                                
#     'alpha': [0.0001, 0.001],                                  
    'alpha': [0.0001, 0.001],                                  
#     'learning_rate': ['adaptive']                                  
    'learning_rate': ['adaptive']                                  
# }
}
# gb_params = {
gb_params = {
#     'n_estimators': [100, 200],                                 
    'n_estimators': [100, 200],                                 
#     'learning_rate': [0.05, 0.1],                        
    'learning_rate': [0.05, 0.1],                        
#     'max_depth': [3, 4],                                  
    'max_depth': [3, 4],                                  
#     'min_samples_split': [2, 5]                                                      
    'min_samples_split': [2, 5]                                                      
# }
}
# ligne vide

# svc = RandomizedSearchCV(SVC(random_state=42), svc_params, n_iter=5, cv=5, n_jobs=-1, random_state=42)
svc = RandomizedSearchCV(SVC(random_state=42), svc_params, n_iter=5, cv=5, n_jobs=-1, random_state=42)
# svc.fit(X_train, Y_train)
svc.fit(X_train, Y_train)
# ligne vide

# mlp = RandomizedSearchCV(MLPClassifier(random_state=42, max_iter=300), mlp_params, n_iter=5, cv=5, n_jobs=-1, random_state=42)
mlp = RandomizedSearchCV(MLPClassifier(random_state=42, max_iter=300), mlp_params, n_iter=5, cv=5, n_jobs=-1, random_state=42)
# mlp.fit(X_train, Y_train)
mlp.fit(X_train, Y_train)
# ligne vide

# gb = RandomizedSearchCV(GradientBoostingClassifier(random_state=42), gb_params, n_iter=5, cv=5, n_jobs=-1, random_state=42)
gb = RandomizedSearchCV(GradientBoostingClassifier(random_state=42), gb_params, n_iter=5, cv=5, n_jobs=-1, random_state=42)
# gb.fit(X_train, Y_train)
gb.fit(X_train, Y_train)
# ligne vide

# def evaluate_model(model, X_test, Y_test, model_name):
def evaluate_model(model, X_test, Y_test, model_name):
#     Y_pred = model.predict(X_test)
    Y_pred = model.predict(X_test)
#     cm = confusion_matrix(Y_test, Y_pred)
    cm = confusion_matrix(Y_test, Y_pred)
# ligne vide

#     plt.figure(figsize=(8, 6))
    plt.figure(figsize=(8, 6))
#     sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
#     plt.title(f'Confusion Matrix - {model_name}')
    plt.title(f'Confusion Matrix - {model_name}')
#     plt.ylabel('True Label')
    plt.ylabel('True Label')
#     plt.xlabel('Predicted Label')
    plt.xlabel('Predicted Label')
#     plt.show()
    plt.show()
# ligne vide

#     print(f"Classification Report - {model_name}")
    print(f"Classification Report - {model_name}")
#     print(classification_report(Y_test, Y_pred))
    print(classification_report(Y_test, Y_pred))
#     print(f"Accuracy: {accuracy_score(Y_test, Y_pred):.4f}")
    print(f"Accuracy: {accuracy_score(Y_test, Y_pred):.4f}")
# ligne vide

# evaluate_model(svc.best_estimator_, X_test, Y_test, "SVC")
evaluate_model(svc.best_estimator_, X_test, Y_test, "SVC")
# evaluate_model(mlp.best_estimator_, X_test, Y_test, "MLP Classifier")
evaluate_model(mlp.best_estimator_, X_test, Y_test, "MLP Classifier")
# evaluate_model(gb.best_estimator_, X_test, Y_test, "Gradient Boosting")
evaluate_model(gb.best_estimator_, X_test, Y_test, "Gradient Boosting")
# ligne vide

# print("Best parameters for SVC:", svc.best_params_)
print("Best parameters for SVC:", svc.best_params_)
# print("Best parameters for MLP:", mlp.best_params_)
print("Best parameters for MLP:", mlp.best_params_)
# print("Best parameters for Gradient Boosting:", gb.best_params_)
print("Best parameters for Gradient Boosting:", gb.best_params_)
# --- cell ---
# import numpy as np
import numpy as np
# import pandas as pd
import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# ligne vide

# models = [
models = [
#     ("Decision Tree", DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)),
    ("Decision Tree", DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)),
#     ("Random Forest", RandomForestClassifier(n_estimators=100, class_weight='balanced', max_samples=0.53, random_state=42)),
    ("Random Forest", RandomForestClassifier(n_estimators=100, class_weight='balanced', max_samples=0.53, random_state=42)),
#     ("SVC", svc.best_estimator_),
    ("SVC", svc.best_estimator_),
#     ("MLP", mlp.best_estimator_),
    ("MLP", mlp.best_estimator_),
#     ("Gradient Boosting", gb.best_estimator_)
    ("Gradient Boosting", gb.best_estimator_)
# ]
]
# ligne vide

# results = []
results = []
# for name, model in models:
for name, model in models:
#     model.fit(X_train, Y_train)
    model.fit(X_train, Y_train)
#     y_pred = model.predict(X_test)
    y_pred = model.predict(X_test)
#     accuracy = accuracy_score(Y_test, y_pred)
    accuracy = accuracy_score(Y_test, y_pred)
#     precision, recall, f1, _ = precision_recall_fscore_support(Y_test, y_pred, average='weighted')
    precision, recall, f1, _ = precision_recall_fscore_support(Y_test, y_pred, average='weighted')
#     results.append((name, accuracy, precision, recall, f1))
    results.append((name, accuracy, precision, recall, f1))
# ligne vide

# df_results = pd.DataFrame(results, columns=['Model', 'Accuracy', 'Precision', 'Recall', 'F1 Score'])
df_results = pd.DataFrame(results, columns=['Model', 'Accuracy', 'Precision', 'Recall', 'F1 Score'])
# ligne vide

# print("n" + "=" * 90)
print("n" + "=" * 90)
# print("📊 COMPARAISON FINALE DE TOUS LES MODÈLES DE MACHINE LEARNING")
print("📊 COMPARAISON FINALE DE TOUS LES MODÈLES DE MACHINE LEARNING")
# print("=" * 90)
print("=" * 90)
# print("n✅ ÉTAPE 1 : RÉSUMÉ DE L'EXPÉRIENCE")
print("n✅ ÉTAPE 1 : RÉSUMÉ DE L'EXPÉRIENCE")
# print("-" * 90)
print("-" * 90)
# print("✓ 5 modèles différents ont été créés et entraînés")
print("✓ 5 modèles différents ont été créés et entraînés")
# print("✓ Tous les modèles ont été testés sur LES MÊMES données (ensemble de test)")
print("✓ Tous les modèles ont été testés sur LES MÊMES données (ensemble de test)")
# print("✓ 4 métriques importantes ont été calculées pour chaque modèle")
print("✓ 4 métriques importantes ont été calculées pour chaque modèle")
# print("✓ Cela nous permet de comparer objectivement lequel fonctionne le mieuxn")
print("✓ Cela nous permet de comparer objectivement lequel fonctionne le mieuxn")
# ligne vide

# print("✅ ÉTAPE 2 : VISUALISATION GRAPHIQUE DES RÉSULTATS")
print("✅ ÉTAPE 2 : VISUALISATION GRAPHIQUE DES RÉSULTATS")
# print("-" * 90)
print("-" * 90)
# print("Voici un graphique qui montre visuellement les performances de chaque modèle:n")
print("Voici un graphique qui montre visuellement les performances de chaque modèle:n")
# ligne vide

# plt.figure(figsize=(12, 6))
plt.figure(figsize=(12, 6))
# df_results.set_index('Model').plot(kind='bar', ylim=[0, 1])
df_results.set_index('Model').plot(kind='bar', ylim=[0, 1])
# plt.title('📈 Comparaison des Performances des Modèles', fontsize=14, fontweight='bold')
plt.title('📈 Comparaison des Performances des Modèles', fontsize=14, fontweight='bold')
# plt.ylabel('Score (0 à 1 = 0% à 100%)', fontsize=11)
plt.ylabel('Score (0 à 1 = 0% à 100%)', fontsize=11)
# plt.xlabel('Modèles', fontsize=11)
plt.xlabel('Modèles', fontsize=11)
# plt.xticks(rotation=45)
plt.xticks(rotation=45)
# plt.legend(loc='lower right', fontsize=10)
plt.legend(loc='lower right', fontsize=10)
# plt.tight_layout()
plt.tight_layout()
# plt.show()
plt.show()
# ligne vide

# print("n✅ ÉTAPE 3 : TABLEAU DES RÉSULTATS DÉTAILLÉS")
print("n✅ ÉTAPE 3 : TABLEAU DES RÉSULTATS DÉTAILLÉS")
# print("=" * 90)
print("=" * 90)
# print("n📋 Voici le tableau complet avec tous les scores de chaque modèle:n")
print("n📋 Voici le tableau complet avec tous les scores de chaque modèle:n")
# print(df_results.to_string(index=False))
print(df_results.to_string(index=False))
# ligne vide

# print("nn✅ ÉTAPE 4 : EXPLICATION DES MÉTRIQUES")
print("nn✅ ÉTAPE 4 : EXPLICATION DES MÉTRIQUES")
# print("=" * 90)
print("=" * 90)
print("""
# 🔹 ACCURACY (Exactitude) :
🔹 ACCURACY (Exactitude) :
#    → Pourcentage de prédictions correctes
   → Pourcentage de prédictions correctes
#    → Plus la valeur est proche de 100%, mieux c'est
   → Plus la valeur est proche de 100%, mieux c'est
#    → C'est la métrique la plus importante pour notre problème
   → C'est la métrique la plus importante pour notre problème
# ligne vide

# 🔹 PRECISION (Précision) :
🔹 PRECISION (Précision) :
#    → Sur les personnes prédites comme "réclamant", quel % a vraiment réclamé ?
   → Sur les personnes prédites comme "réclamant", quel % a vraiment réclamé ?
#    → Évite les faux positifs (dire "oui" quand c'est "non")
   → Évite les faux positifs (dire "oui" quand c'est "non")
# ligne vide

# 🔹 RECALL (Sensibilité) :
🔹 RECALL (Sensibilité) :
#    → Sur les personnes qui ont VRAIMENT réclamé, quel % a été détecté ?
   → Sur les personnes qui ont VRAIMENT réclamé, quel % a été détecté ?
#    → Évite les faux négatifs (dire "non" quand c'est "oui")
   → Évite les faux négatifs (dire "non" quand c'est "oui")
# ligne vide

# 🔹 F1-SCORE :
🔹 F1-SCORE :
#    → C'est un équilibre entre Precision et Recall
   → C'est un équilibre entre Precision et Recall
#    → Utile quand on veut un bon équilibre entre les deux
   → Utile quand on veut un bon équilibre entre les deux
""")
# ligne vide

# print("n✅ ÉTAPE 5 : CLASSEMENT DES MEILLEURS MODÈLES")
print("n✅ ÉTAPE 5 : CLASSEMENT DES MEILLEURS MODÈLES")
# print("=" * 90)
print("=" * 90)
# ligne vide

# df_sorted = df_results.sort_values('Accuracy', ascending=False).reset_index(drop=True)
df_sorted = df_results.sort_values('Accuracy', ascending=False).reset_index(drop=True)
# ligne vide

# print("nVoici l'ordre des modèles du MEILLEUR au MOINS BON (basé sur l'Accuracy):n")
print("nVoici l'ordre des modèles du MEILLEUR au MOINS BON (basé sur l'Accuracy):n")
# ligne vide

# for idx, row in df_sorted.iterrows():
for idx, row in df_sorted.iterrows():
#     rank = idx + 1
    rank = idx + 1
#     medal = "🥇 OR" if rank == 1 else "🥈 ARGENT" if rank == 2 else "🥉 BRONZE" if rank == 3 else f"#{rank}"
    medal = "🥇 OR" if rank == 1 else "🥈 ARGENT" if rank == 2 else "🥉 BRONZE" if rank == 3 else f"#{rank}"
#     accuracy_percent = row['Accuracy']*100
    accuracy_percent = row['Accuracy']*100
#     bar_length = int(accuracy_percent / 5)
    bar_length = int(accuracy_percent / 5)
#     progress_bar = "█" * bar_length + "░" * (20 - bar_length)
    progress_bar = "█" * bar_length + "░" * (20 - bar_length)
#     print(f"┌─ {medal} - POSITION {rank}")
    print(f"┌─ {medal} - POSITION {rank}")
#     print(f"│")
    print(f"│")
#     print(f"│ Modèle : {row['Model']}")
    print(f"│ Modèle : {row['Model']}")
#     print(f"│ Exactitude     : [{progress_bar}] {accuracy_percent:.2f}%")
    print(f"│ Exactitude     : [{progress_bar}] {accuracy_percent:.2f}%")
#     print(f"│ Précision      : {row['Precision']*100:.2f}%")
    print(f"│ Précision      : {row['Precision']*100:.2f}%")
#     print(f"│ Sensibilité    : {row['Recall']*100:.2f}%")
    print(f"│ Sensibilité    : {row['Recall']*100:.2f}%")
#     print(f"│ F1-Score       : {row['F1 Score']*100:.2f}%")
    print(f"│ F1-Score       : {row['F1 Score']*100:.2f}%")
#     print(f"└─n")
    print(f"└─n")
# ligne vide

# best_model = df_sorted.iloc[0]
best_model = df_sorted.iloc[0]
# second_model = df_sorted.iloc[1] if len(df_sorted) > 1 else None
second_model = df_sorted.iloc[1] if len(df_sorted) > 1 else None
# third_model = df_sorted.iloc[2] if len(df_sorted) > 2 else None
third_model = df_sorted.iloc[2] if len(df_sorted) > 2 else None
# ligne vide

# print("=" * 90)
print("=" * 90)
# print(f" RÉSUMÉ FINAL - LE MEILLEUR MODÈLE EST : {best_model['Model'].upper()}")
print(f" RÉSUMÉ FINAL - LE MEILLEUR MODÈLE EST : {best_model['Model'].upper()}")
# print("=" * 90)
print("=" * 90)
# ligne vide

print(f"""
 QUE SIGNIFIENT CES RÉSULTATS ?

 Performance Principale:
    → Le modèle '{best_model['Model']}' atteint une exactitude de {best_model['Accuracy']*100:.2f}%
    → Cela signifie qu'il fait les BONNES prédictions {best_model['Accuracy']*100:.2f}% du temps
    → Et se trompe {(100 - best_model['Accuracy']*100):.2f}% du temps

 Quelle est la qualité ?""")
# ligne vide

# if best_model['Accuracy'] >= 0.85:
if best_model['Accuracy'] >= 0.85:
#     print(f"   → EXCELLENTE performance ! ({best_model['Accuracy']*100:.2f}% ≥ 85%)")
    print(f"   → EXCELLENTE performance ! ({best_model['Accuracy']*100:.2f}% ≥ 85%)")
# elif best_model['Accuracy'] >= 0.75:
elif best_model['Accuracy'] >= 0.75:
#     print(f"   → TRÈS BONNE performance ! ({best_model['Accuracy']*100:.2f}% ≥ 75%)")
    print(f"   → TRÈS BONNE performance ! ({best_model['Accuracy']*100:.2f}% ≥ 75%)")
# elif best_model['Accuracy'] >= 0.65:
elif best_model['Accuracy'] >= 0.65:
#     print(f"   → BONNE performance ! ({best_model['Accuracy']*100:.2f}% ≥ 65%)")
    print(f"   → BONNE performance ! ({best_model['Accuracy']*100:.2f}% ≥ 65%)")
# else:
else:
#     print(f"   → Performance acceptable ({best_model['Accuracy']*100:.2f}%)")
    print(f"   → Performance acceptable ({best_model['Accuracy']*100:.2f}%)")
# ligne vide

# if second_model is not None:
if second_model is not None:
#     accuracy_gap = (best_model['Accuracy'] - second_model['Accuracy']) * 100
    accuracy_gap = (best_model['Accuracy'] - second_model['Accuracy']) * 100
#     print(f"n📊 Comparaison avec le 2ème meilleur modèle ('{second_model['Model']}'):")
    print(f"n📊 Comparaison avec le 2ème meilleur modèle ('{second_model['Model']}'):")
#     print(f"   → Différence d'exactitude : +{accuracy_gap:.2f} points de pourcentage")
    print(f"   → Différence d'exactitude : +{accuracy_gap:.2f} points de pourcentage")
#     if accuracy_gap > 5:
    if accuracy_gap > 5:
#         print(f"   → Le meilleur modèle est CLAIREMENT supérieur!")
        print(f"   → Le meilleur modèle est CLAIREMENT supérieur!")
#     elif accuracy_gap > 1:
    elif accuracy_gap > 1:
#         print(f"   → Le meilleur modèle est légèrement supérieur")
        print(f"   → Le meilleur modèle est légèrement supérieur")
#     else:
    else:
#         print(f"   → Les deux modèles sont très proches en performance")
        print(f"   → Les deux modèles sont très proches en performance")
# ligne vide

# print("n" + "=" * 90)
print("n" + "=" * 90)
# print(" CONCLUSION :")
print(" CONCLUSION :")
# print("=" * 90)
print("=" * 90)
print(f"""
Le modèle '{best_model['Model']}' est notre MEILLEUR CHOIX pour prédire les réclamations.
Ses performances sont stables et fiables.
""")
# print("=" * 90)
print("=" * 90)
