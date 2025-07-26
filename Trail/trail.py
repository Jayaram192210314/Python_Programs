import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from xgboost import XGBRFClassifier
from sklearn.metrics import accuracy_score

# Load dataset
url = 'C:\\Users\\sn302\\OneDrive\\Desktop\\kyphosis.csv'
df = pd.read_csv(url)

# Data preprocessing
X = df[['Age', 'Number', 'Start']]
y = df['Kyphosis']

# Encode target variable y
le_y = LabelEncoder()
y = le_y.fit_transform(y)

# Encode categorical variables
label_encoders = {}
for column in X.select_dtypes(include='object').columns:
    label_encoders[column] = LabelEncoder()
    X[column] = label_encoders[column].fit_transform(X[column])

# List to store accuracy values
accuracy_values = []

# Run the training and evaluation process 10 times
for i in range(10):
    # Train-test split with different random state each time
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=i)

    # Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # XGBRFClassifier model
    xgbrf_model = XGBRFClassifier()
    xgbrf_model.fit(X_train_scaled, y_train)

    # Calculate accuracy
    xgbrf_accuracy = accuracy_score(y_test, xgbrf_model.predict(X_test_scaled))
    accuracy_values.append(xgbrf_accuracy)

# Print the accuracy values
for i, acc in enumerate(accuracy_values):
    print(f"Accuracy {i+1}: {acc*100:.2f}%")
