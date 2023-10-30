import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest, f_classif
import pickle
import seaborn as sns
from tqdm.notebook import tqdm

X = pickle.load(open('features_combined.npy','rb'))
y = pickle.load(open('output_combined.npy','rb'))

# Split the data into training and test sets (80-20 split)
print("Train test split...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier(max_depth=20, n_estimators=100)


xscaler = StandardScaler()
X_train_scaled = xscaler.fit_transform(X_train)
X_test_scaled = xscaler.transform(X_test)

print("\n\nFitting to the best Random Forest Model....")
rf_classifier.fit(X_train_scaled, y_train.values.ravel())

# pickle.dump(rf_classifier, open('./rf_model.pkl','wb'))
# Test the best model on the held-out test set
y_pred = rf_classifier.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on test set: {accuracy:.2f}")

k_best = SelectKBest(score_func=f_classif, k=25)  # You can adjust 'k' as needed
X_train_selected = k_best.fit_transform(X_train, y_train)
X_test_selected = k_best.transform(X_test) 


plt.figure(figsize = (12, 8))
bins = [i/20 for i in range(20)] + [1]
y_proba = rf_classifier.predict_proba(X_test)
classes = rf_classifier.classes_
roc_auc_ovr = {}
for i in tqdm(range(len(classes))):
    # Gets the class
    c = classes[i]
    
    # Prepares an auxiliar dataframe to help with the plots
    df_aux = X_test.copy()
    df_aux['class'] = [1 if y == c else 0 for y in y_test.values]
    df_aux['prob'] = y_proba[:, i]
    df_aux = df_aux.reset_index(drop = True)
    
    # Plots the probability distribution for the class and the rest
    ax = plt.subplot(2, 3, i+1)
    sns.histplot(x = "prob", data = df_aux, hue = 'class', color = 'b', ax = ax, bins = bins)
    ax.set_title(c)
    ax.legend([f"Class: {c}", "Rest"])
    ax.set_xlabel(f"P(x = {c})")
    
    # Calculates the ROC Coordinates and plots the ROC Curves
    ax_bottom = plt.subplot(2, 3, i+4)
    tpr, fpr = get_all_roc_coordinates(df_aux['class'], df_aux['prob'])
    plot_roc_curve(tpr, fpr, scatter = False, ax = ax_bottom)
    ax_bottom.set_title("ROC Curve OvR")
    
    # Calculates the ROC AUC OvR
    roc_auc_ovr[c] = roc_auc_score(df_aux['class'], df_aux['prob'])
plt.tight_layout()
#plt.savefig('./Supplementary_Figure_Random_forest.png',dpi=300)
