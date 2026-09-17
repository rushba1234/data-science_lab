import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Dataset: 10 people, 5 features
# Features: Attendance, Marks, TimeSpent, Assignments, ExamScore
data = {
    'Attendance': [90, 60, 85, 55, 95, 70, 80, 50, 88, 65],
    'Marks':      [85, 45, 78, 40, 92, 55, 75, 35, 82, 50],
    'TimeSpent':  [8,  2,  7,  1,  9,  4,  6,  1,  8,  3],
    'Assignments':[9,  4,  8,  3, 10, 5,  7, 2, 9, 4],
    'ExamScore':  [88, 42, 80, 38, 95, 50, 77, 30, 85, 45],
    'Cheats':     [0,  1,  0,  1,  0,  1,  0,  1,  0,  1]
}

df = pd.DataFrame(data)

# Five input features
X = df[['Attendance', 'Marks', 'TimeSpent',
        'Assignments', 'ExamScore']]

# Target variable
y = df['Cheats']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Decision tree
model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("Predicted values:", y_pred)
print("Actual values:   ", y_test.values)
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Predict a new person
new_person = [[75, 60, 5, 6, 65]]
prediction = model.predict(new_person)

if prediction[0] == 1:
    print("Prediction: Cheating detected")
else:
    print("Prediction: No cheating detected")

