# -*- coding: utf-8 -*-
"""Kymbat Baisapina outpeer project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12WiLlV0FfyQJ0wo5W5DfRUUhyC7QEjeW
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split , GridSearchCV

hobbyplz= pd.read_csv('/content/Hobby_Data.csv')

hobbyplz.head()

hobbyplz.describe()

hobbyplz["Predicted Hobby"].unique()

hobbyplz.isna().sum()

hobbyplz_int=hobbyplz.select_dtypes(include=["int64"])
hobbyplz_obj=hobbyplz.select_dtypes(include=["object"]).columns
hobbyplz_obj

encoder=LabelEncoder()
for col in hobbyplz_obj:
    hobbyplz[col] = encoder.fit_transform(hobbyplz[col])
    labels = {i: label for i, label in enumerate(encoder.classes_)}
    print(col,labels)

import matplotlib.pyplot as plt
import seaborn as sns

# Set the figure size
plt.figure(figsize=(10, 5))

# Calculate the correlation matrix
c = hobbyplz[["Olympiad_Participation", 'Scholarship', 'School', 'Fav_sub',
       'Projects', 'Medals', 'Career_sprt', 'Act_sprt', 'Fant_arts',
       'Won_arts', "Predicted Hobby"]].corr()

# Create the heatmap
sns.heatmap(c, cmap="BrBG", annot=True)

# Show the plot
plt.title("Correlation Matrix Heatmap")
plt.show()

X=hobbyplz.drop(columns=["Predicted Hobby"])
X.columns
y=hobbyplz["Predicted Hobby"]
import plotly.express as px
for column in X:
    fig = px.density_heatmap(hobbyplz, x=column, y=y, template='ggplot2')
    fig.update_layout(
        title=f"Density Heatmap of {column}",
        height=300,
    )
    fig.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import numpy as np

# Initialize Logistic Regression
log_reg = LogisticRegression(max_iter=1000)

# Train the model
log_reg.fit(X_train, y_train)

# Make predictions
y_pred = log_reg.predict(X_test)

# Evaluate Logistic Regression
accuracy = accuracy_score(y_test, y_pred)

# Use 'weighted' average for multiclass precision
precision = precision_score(y_test, y_pred, average='weighted')

# Use 'weighted' average for multiclass recall
recall = recall_score(y_test, y_pred, average='weighted')

# Use 'weighted' average for multiclass f1-score
f1 = f1_score(y_test, y_pred, average='weighted')

roc_auc = roc_auc_score(y_test, log_reg.predict_proba(X_test), multi_class='ovr') # For multiclass ROC AUC

# Print evaluation metrics
print("Logistic Regression:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"ROC AUC: {roc_auc:.4f}")

# Get the number of classes
n_classes = len(np.unique(y_test))

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test, log_reg.predict_proba(X_test)[:, i], pos_label=i)
    roc_auc[i] = roc_auc_score(y_test == i, log_reg.predict_proba(X_test)[:, i]) # For multiclass ROC AUC

# Plot ROC curves for each class
for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], label=f"Class {i} (AUC = {roc_auc[i]:.4f})")

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic (ROC) curve for multiclass')
plt.legend(loc="lower right")
plt.show()

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import numpy as np

# Initialize Decision Tree Classifier
decision_tree = DecisionTreeClassifier(random_state=42)

# Train the model
decision_tree.fit(X_train, y_train)

# Make predictions
y_pred = decision_tree.predict(X_test)

# Evaluate Decision Tree
accuracy = accuracy_score(y_test, y_pred)
# Change 'average' to 'weighted' for multiclass classification
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
# For multiclass ROC AUC, use 'ovr' or 'ovo'
roc_auc = roc_auc_score(y_test, decision_tree.predict_proba(X_test), multi_class='ovr')

# Print evaluation metrics
print("Decision Tree:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"ROC AUC: {roc_auc:.4f}")

# Get the number of classes
n_classes = len(np.unique(y_test))

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test, decision_tree.predict_proba(X_test)[:, i], pos_label=i)
    roc_auc[i] = roc_auc_score(y_test == i, decision_tree.predict_proba(X_test)[:, i]) # For multiclass ROC AUC

# Plot ROC curves for each class
for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], label=f"Class {i} (AUC = {roc_auc[i]:.4f})")

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic (ROC) curve for multiclass')
plt.legend(loc="lower right")
plt.show()

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import numpy as np

# Initialize Random Forest Classifier
random_forest = RandomForestClassifier(random_state=42)

# Train the model
random_forest.fit(X_train, y_train)

# Make predictions
y_pred = random_forest.predict(X_test)

# Evaluate Random Forest
accuracy = accuracy_score(y_test, y_pred)
# Use 'weighted' average for multiclass precision
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
# For multiclass ROC AUC, use 'ovr' (one-vs-rest)
roc_auc = roc_auc_score(y_test, random_forest.predict_proba(X_test), multi_class='ovr')

# Print evaluation metrics
print("Random Forest:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"ROC AUC: {roc_auc:.4f}")

# Get the number of classes
n_classes = len(np.unique(y_test))

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test, random_forest.predict_proba(X_test)[:, i], pos_label=i)
    roc_auc[i] = roc_auc_score(y_test == i, random_forest.predict_proba(X_test)[:, i]) # For multiclass ROC AUC

# Plot ROC curves for each class
for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], label=f"Class {i} (AUC = {roc_auc[i]:.4f})")

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic (ROC) curve for multiclass')
plt.legend(loc="lower right")
plt.show()

from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Initialize XGBoost Classifier
xgb = XGBClassifier(random_state=42, use_label_encoder=False, eval_metric='logloss')

# Train the model
xgb.fit(X_train, y_train)

# Make predictions
y_pred = xgb.predict(X_test)

# Evaluate XGBoost
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
# Set average='weighted' for multiclass recall
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
# Adjust ROC AUC calculation for multiclass
roc_auc = roc_auc_score(y_test, xgb.predict_proba(X_test), multi_class='ovr')

# Plot ROC Curve
# Get the number of classes
n_classes = len(np.unique(y_test))

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test, xgb.predict_proba(X_test)[:, i], pos_label=i)
    roc_auc[i] = roc_auc_score(y_test == i, xgb.predict_proba(X_test)[:, i]) # For multiclass ROC AUC

# Plot ROC curves for each class
for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], label=f"Class {i} (AUC = {roc_auc[i]:.4f})")

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic (ROC) curve for multiclass')
plt.legend(loc="lower right")
plt.show()
print("Random Forest:")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall:}")
print(f"F1 Score: {f1:}")
print(f"ROC AUC: {roc_auc:}")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV, cross_val_score

# Assuming these are the models you've already trained
# Replace the values below with your actual results

model_performance = {
    'Model': ['Logistic Regression', 'Decision Tree', 'Random Forest', 'XGBoost'],
    'Accuracy': [0.9097,  0.8754, 0.9315 , 0.9065420560747663],
    'Precision': [0.9097, 0.8767,0.9321, 0.909237958303379],
    'Recall': [0.9097, 0.8754,0.9315, 0.9065420560747663],
    'F1-Score': [0.9091,  0.8758,0.9313,0.9064629884403119],
    'ROC AUC': [ 0.9815,0.9059,0.9916,0.9806750136091452]

}

# Convert dictionary to DataFrame
performance_df = pd.DataFrame(model_performance)

# Display the table
print(performance_df)

# Plot F1-Score Comparison
plt.figure(figsize=(10, 6))
sns.barplot(x='Model', y='F1-Score', data=performance_df, palette='viridis')
plt.title('F1-Score Comparison Between Models')
plt.ylabel('F1-Score')
plt.xticks(rotation=45)
plt.show()

xgb_params = [{
    'n_estimators': range(10, 50, 10),
    'learning_rate': [0.1, 0.5, 1.0],
    'max_depth': range(3,21,2)
}]

xgb = XGBClassifier()
xgb_grid_search = GridSearchCV(xgb, xgb_params, scoring='f1', cv=5, verbose=False, n_jobs=-1)
xgb_grid_search.fit(X_train, y_train)

best_xgb_params = xgb_grid_search.best_params_  # Changed lr_grid_search to xgb_grid_search
print(best_xgb_params)

