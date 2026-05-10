 !pip show scikit-learn

!pip install --upgrade scikit-learn


!pip show scikit-learn

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

from google.colab import drive
drive.mount('/content/drive')


# Path to the CSV file on your Google Drive
csv_path = '/content/drive/MyDrive/paysim dataset.csv'
# Read the CSV file into a Pandas DataFrame
data = pd.read_csv(csv_path)
df=pd.DataFrame(data)
# Display the first few rows of the DataFrame
df.head(10)

df.info()

df.isnull().sum()

df['isFraud'].value_counts()

df['type'].value_counts()

sns.countplot(df,x='isFraud')
plt.title("1 Fraud                         0 non-Fraud")

sns.countplot(df,x='type')
plt.title("Frequencies of transaction types")

# Group by "TransactionType" and calculate the mean of "isFraud"
fraud_percentage_by_type = df.groupby('type')['isFraud'].mean() * 100
# Create a bar plot
plt.bar(fraud_percentage_by_type.index, fraud_percentage_by_type.values)
# Adding labels and title
plt.xlabel('Transaction Type')
plt.ylabel('Fraud Percentage')
plt.title('Fraud Percentage by Transaction Type')

# Rotate x labels for better readability
plt.xticks(rotation=45)

# Display the plot
#plt.tight_layout()
plt.show()



data = df.loc[df['type'].isin(['CASH_OUT', 'TRANSFER'])]
print('The new data now has ', len(data), ' transactions.')

print('Number of transactions where the transaction amount is negative: ' +
str(sum(data['amount'] < 0)))



print('Number of transactions where the transaction amount is equal to zero: ' +
str(sum(data['amount'] == 0)))


no_Ofzero=sum(data['oldbalanceOrg']==0)
total=len(data['oldbalanceDest'])
percentage=(no_Ofzero/total)*100
print(f"Percentage of transactions where originators initial balance is 0: {percentage:.2f}")


labels = ['Initial Balance 0', 'Initial Balance Not 0']
sizes = [percentage, 100 - percentage]
colors = ['gold', 'lightskyblue']
explode = (0.1, 0)  # explode the 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Percentage of Transactions where originators Initial Balance 0")
plt.show()







no_Ofzero=sum(data['newbalanceDest']==0)
total=len(data['newbalanceDest'])
percentage=(no_Ofzero/total)*100
#print(f"Percentage of transactions where  destination's final balance is 0:{percantage:.2f}")

#pie plot
import matplotlib.pyplot as plt

# Data
labels = ['Final Balance 0', 'Final Balance Not 0']
sizes = [percentage, 100 - percentage]  # Corrected calculation
colors = ['gold', 'lightskyblue']
explode = (0.1, 0)  # Explode the first slice

# Create pie plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.title("Percentage of Transactions where destination's final balance is 0")

# Display the plot
plt.show()


tolerance = 1e-6
not_accuratly_captured=sum(np.abs(data['oldbalanceOrg']-data['amount']==data['newbalanceOrig'])<tolerance)
total=len(data['newbalanceOrig'])
percentage=(not_accuratly_captured/total)*100
print(f"% transactions where originator balances are not accurately captured:{percentage:.2f} ")


labels = [ 'Not Accurately Captured','Accurately Captured']
sizes = [percentage,100 - percentage ]
colors = ['lightskyblue', 'gold']
explode = (0, 0.1)  # Explode the "Not Accurately Captured" slice

# Create pie plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.title("Percentage of Transactions with Inaccurate Originator Balances")

# Display the plot
plt.show()

tolerance = 1e-6
not_accuratly_captured=sum(np.abs(data['amount']+data['oldbalanceDest']==data['newbalanceDest'])<tolerance)
total=len(data['newbalanceDest'])
percentage=(not_accuratly_captured/total)*100
print(f"% transactions where destination's balances are not accurately captured:{percentage:.2f} ")


# Data for the pie plot
labels = ["Accurately Captured", "Not Accurately Captured"]
sizes = [100 - percentage, percentage]
colors = ['lightskyblue', 'gold']
explode = (0, 0.1)  # Explode the "Not Accurately Captured" slice

# Create pie plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.title("Percentage of Transactions with Inaccurate Destination Balances")

# Display the plot
plt.show()

#for fraudulant data

fraud_count=0
for i in range(len(data['isFraud'])):
  if data['isFraud'].values[i] ==1 :
    fraud_count=fraud_count+1
print(fraud_count)

value_count=0
for i in range(len(data['isFraud'])):
  if data['isFraud'].values[i] ==1 and data['oldbalanceOrg'].values[i]==0 :
    value_count=value_count+1
print(value_count)


percentage=(value_count/fraud_count)*100
print(f"% of fraudulent transactions where initial balance of originator is 0: {percentage:2f}")

labels = ["Initial Balance Not 0", "Initial Balance 0"]
sizes = [100 - percentage, percentage]
colors = ['lightskyblue', 'gold']
explode = (0, 0.1)  # Explode the "Initial Balance 0" slice

# Create pie plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.title("Percentage of Fraudulent Transactions where initial balance of originator is 0")

# Display the plot
plt.show()

#for non fraudulant data

fraud_count=0
for i in range(len(data['isFraud'])):
  if data['isFraud'].values[i] ==0 :
    fraud_count=fraud_count+1
print(fraud_count)

value_count=0
for i in range(len(data['isFraud'])):
  if data['isFraud'].values[i] ==0 and data['oldbalanceOrg'].values[i]==0 :
    value_count=value_count+1
print(value_count)


percentage=(value_count/fraud_count)*100
print(f"% of non fraudulent transactions where initial balance of originator is 0: {percentage:2f}")

labels = ["Initial Balance Not 0", "Initial Balance 0"]
sizes = [100 - percentage, percentage]
colors = ['lightskyblue', 'gold']
explode = (0, 0.1)  # Explode the "Initial Balance 0" slice

# Create pie plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.001f%%', shadow=True, startangle=140)

plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
plt.title("Percentage of Non Fraudulent Transactions where initial balance of originator is 0")

# Display the plot
plt.show()

data1 = data.drop(['nameOrig', 'nameDest','isFlaggedFraud','step'], axis=1)
print(data1.head())
len(data1)

from sklearn.model_selection import train_test_split
train_data,test_data=train_test_split(data1,test_size=0.3,random_state=21)
print("len of train data",len(train_data))
print("len of test data",len(test_data))



#training data
x_train=train_data.drop(["isFraud"],axis=1)
y_train=train_data["isFraud"]



#testing data
x_test=test_data.drop("isFraud",axis=1)
y_test=test_data["isFraud"]



print(type(y_train))

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder

#numerical features
num_feats=x_train.drop("type",axis=1)
num_feats_pipe=Pipeline([
    ("scalar",MinMaxScaler())
    ])
num_feats_preprocessed=num_feats_pipe.fit_transform(num_feats)

#catagorical features
cat_feats=x_train[["type"]]
cat_feats_pipe=Pipeline([
    ("encoder",OneHotEncoder())
    ])
cat_feats_preprocessed=cat_feats_pipe.fit_transform(cat_feats)
print(num_feats)



from sklearn.compose import ColumnTransformer
num_list=list(num_feats)
cat_list=list(cat_feats)

final_pipeline=ColumnTransformer([
    ("num",num_feats_pipe,num_list),
    ("cat",cat_feats_pipe,cat_list)])
X_train_preprocessed=final_pipeline.fit_transform(x_train)
print(x_train)
X_train_preprocessed

X_test_preprocessed = final_pipeline.fit_transform(x_test)
X_test_preprocessed

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

log_model=model.fit(X_train_preprocessed,y_train)

y_train_pred = log_model.predict(X_train_preprocessed)
y_train_pred

y_test_pred=log_model.predict(X_test_preprocessed)
y_test_pred

from sklearn.metrics import confusion_matrix

# Compute the confusion matrix
cm = confusion_matrix(y_train, y_train_pred)

# Create a heatmap to visualize the confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted Labels ")
plt.ylabel("True Labels ")
plt.title(" Train Confusion Matrix")
plt.show()


from sklearn.metrics import confusion_matrix

# Compute the confusion matrix
cm = confusion_matrix(y_test, y_test_pred)

# Create a heatmap to visualize the confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted Labels ")
plt.ylabel("True Labels ")
plt.title(" Test Confusion Matrix")
plt.show()


from sklearn.metrics import f1_score

f1 = f1_score(y_train,y_train_pred)
print("F1 Score of train data:", f1)

f2 = f1_score(y_test,y_test_pred)
print("F1 Score of test data:", f2)



from sklearn.ensemble import RandomForestClassifier

# Create a Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=21)

# Train the model on your training data
rf_model.fit(X_train_preprocessed,y_train)

# Make predictions on your testing data
y_test_pred_rf = rf_model.predict(X_test_preprocessed)



# Make predictions on your training data
y_train_pred_rf = rf_model.predict(X_train_preprocessed)
y_train_pred_rf
y_test_pred_rf

from sklearn.metrics import f1_score
f1 = f1_score(y_train,y_train_pred_rf)
print("F1 Score of train data:", f1)

f2 = f1_score(y_test,y_test_pred_rf)
print("F1 Score of test data:", f2)

from sklearn.metrics import classification_report
report = classification_report(y_test, y_test_pred_rf)
print(report)

from sklearn.metrics import confusion_matrix

# Compute the confusion matrix
cm = confusion_matrix(y_train, y_train_pred_rf)

# Create a heatmap to visualize the confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted Labels ")
plt.ylabel("True Labels ")
plt.title(" Train Confusion Matrix")
plt.show()


from sklearn.metrics import confusion_matrix

# Compute the confusion matrix
cm = confusion_matrix(y_test, y_test_pred_rf)

# Create a heatmap to visualize the confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted Labels ")
plt.ylabel("True Labels ")
plt.title(" Test Confusion Matrix")
plt.show()


# import xgboost as xgb

# # Create an XGBoost classifier
# xgb_model = xgb.XGBClassifier(n_estimators=100, random_state=42)

# # Train the model on your training data
# xgb_model.fit(X_train_preprocessed,y_train)

# # Make predictions on your testing data
# y_test_pred_xgb = xgb_model.predict(X_test_preprocessed)


# # Make predictions on your training data
# y_train_pred_xgb = rf_model.predict(X_train_preprocessed)
# y_train_pred_xgb
# y_test_pred_xgb

# f1 = f1_score(y_train,y_train_pred_xgb)
# print("F1 Score of train data:", f1)

# f2 = f1_score(y_test,y_test_pred_xgb)
# print("F1 Score of test data:", f2)

# from sklearn.metrics import confusion_matrix

# # Compute the confusion matrix
# cm = confusion_matrix(y_train, y_train_pred_xgb)

# # Create a heatmap to visualize the confusion matrix
# plt.figure(figsize=(6, 4))
# sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
# plt.xlabel("Predicted Labels ")
# plt.ylabel("True Labels ")
# plt.title(" Train Confusion Matrix")
# plt.show()


# from sklearn.metrics import confusion_matrix

# # Compute the confusion matrix
# cm = confusion_matrix(y_test, y_test_pred_xgb)

# # Create a heatmap to visualize the confusion matrix
# plt.figure(figsize=(6, 4))
# sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
# plt.xlabel("Predicted Labels ")
# plt.ylabel("True Labels ")
# plt.title(" Test Confusion Matrix")
# plt.show()


from sklearn.svm import SVC

# Create an SVM classifier with an RBF kernel
svm_classifier = SVC(kernel='rbf', C=1.0)

# Train the SVM model
svm_classifier.fit(X_train_preprocessed, y_train)


y_train_pred_svm=svm_classifier.predict(X_train_preprocessed)
y_test_pred_svm=svm_classifier.predict(X_train_preprocessed)

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

f1=f1_score(y_train,y_train_pred_svm)
print("f1 score of train is ",f1)
f2=f1_score(y_test,y_test_pred_svm)
print(("f1 score of test is ",f2))


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_train,y_train_pred_svm)

# Create a heatmap to visualize the confusion matrix

plt.figure(figsize=(6,4))
sns.heatmap(cm,annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted Labels")
plt.ylabel("True labels")
plt.title(" Train Confusion Matrix")
plt.show()

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_test_pred_svm)

# Create a heatmap to visualize the confusion matrix

plt.figure(figsize=(6,4))
sns.heatmap(cm,annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted Labels")
plt.ylabel("True labels")
plt.title(" Test Confusion Matrix")
plt.show()

# from joblib import dump, load

# # Save your model to a file
# joblib.dump(rf_model, 'banking_app_rf.joblib')


# loaded_model=load("banking_app_rf.joblib")

#pre=loaded_model.predict(X_train_preprocessed)



# import joblib
# # Save your model to a file
# joblib.dump('xgb_model', 'banking_application_xgb.pkl')


# import joblib
# # Save your model to a file
# joblib.dump('lgb_model', 'banking_application_lgb.pkl')


# pickle.dump(model, open('xgb_model.pkl', 'wb'))


