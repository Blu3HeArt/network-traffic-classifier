import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.tree import export_text

data = pd.read_csv("network_connections.csv")
df = pd.DataFrame(data)

#print(df.head())
expected_labels = ['duration_seconds','bytes_sent','bytes_received','packets_sent','failed_logins',]
label_counts = df[expected_labels].value_counts()
#print(label_counts)
#print(df.shape)
missing_labels = df.isnull().sum()
#print(f"Missing Values: {missing_labels}")
#print(df.dtypes)

# X and Y values
X = df[expected_labels]
y = df['label']
#print(X.head())
#print(y.head())
#print(X.shape)
#print(y.shape)

#training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42,stratify=y)
#print(pd.DataFrame(X_train).head())
#print(pd.DataFrame(X_test).head())
#print(pd.DataFrame(y_train).head())
#print(pd.DataFrame(y_test).head())

# Create and train the decision tree classifier
model = DecisionTreeClassifier(random_state=42, max_depth=3)
model.fit(X_train, y_train)
#print("Decision Tree Classifier trained successfully.")

#make predictions on the test set
y_pred = model.predict(X_test)
#print(y_pred)
#print(y_test)

#calculate accuracy and confusion matrix
from sklearn.metrics import accuracy_score, confusion_matrix
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred, labels=['normal', 'suspicious'])
#print(f"Accuracy: {accuracy}")
#print(f"Confusion Matrix:\n{cm}")

#New connections to classify
new_connections = pd.DataFrame({
    'duration_seconds': [50,5],
    'bytes_sent': [3000, 1000],
    'bytes_received': [20000, 250],
    'packets_sent': [35,20],
    'failed_logins': [0,9]
})
predictions = model.predict(new_connections)
for i, connection in new_connections.iterrows():
    print(f"Connection {i+1}: {connection.to_dict()} - Predicted Label: {predictions[i]}")

#Inspect the decision tree structure
tree_rules = export_text(model, feature_names=list(X.columns))
#print("Decision Tree Rules:" + tree_rules)

#test a limited number of new connections
new_connections_limited = pd.DataFrame({
    'duration_seconds': [2],
    'bytes_sent': [200],
    'bytes_received': [100],
    'packets_sent': [3],
    'failed_logins': [0]
})
predictions_limited = model.predict(new_connections_limited)
for i, connection in new_connections_limited.iterrows():
    print(f"Connection {i+1}: {connection.to_dict()} - Predicted Label: {predictions_limited[i]}")