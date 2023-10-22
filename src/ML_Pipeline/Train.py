# Import necessary libraries and modules
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Define a function to calculate AUC (Area Under the Curve) for ROC (Receiver Operating Characteristic)
def get_auc(labels, scores):
    fpr, tpr, thresholds = roc_curve(labels, scores)
    auc_score = auc(fpr, tpr)
    return fpr, tpr, auc_score

# Define a function to plot a metric
def plot_metric(ax, x, y, x_label, y_label, plot_label, style="-"):
    ax.plot(x, y, style, label=plot_label)
    ax.legend()
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

# Define a function to summarize predictions and plot ROC curve
def prediction_summary(labels, predicted_score, info, plot_baseline=True, axes=None):
    if axes is None:
        axes = [plt.subplot(1, 2, 1)]

    fpr, tpr, auc_score = get_auc(labels, predicted_score)
    plot_metric(axes[0], fpr, tpr, "False positive rate", "True positive rate", "{} AUC = {:.4f}".format(info, auc_score))
    if plot_baseline:
        plot_metric(axes[0], [0, 1], [0, 1], "False positive rate", "True positive rate", "baseline AUC = 0.5", "r--")

    plt.show()
    return axes, auc_score

# Define a function to create a figure for plotting
def figure():
    fig_size = 4.5
    f = plt.figure()
    f.set_figheight(fig_size)
    f.set_figwidth(fig_size * 2)

# Define a function to split data into training and testing sets
def data_split(data, test_ratio):
    pdf_train, pdf_test = train_test_split(data, test_size=test_ratio, random_state=123)
    return pdf_train, pdf_test

# Define a function to fit a RandomForestClassifier model
def fit_model(training_df, select_features, target_var):
    pdf_train, pdf_test = data_split(training_df, 0.2)
    
    X_train = pdf_train[select_features]
    X_train['is_train'] = 1

    X_test = pdf_test[select_features]
    X_test['is_train'] = 0

    X = pd.concat([X_train, X_test])
    X = pd.get_dummies(data=X)

    X_train = X[X.is_train == 1]
    X_test = X[X.is_train == 0]

    X_train.drop(['is_train'], axis=1, inplace=True)
    X_test.drop(['is_train'], axis=1, inplace=True

    # Create a RandomForestClassifier model and fit it to the training data
    scikit_rf = RandomForestClassifier(n_estimators=100, random_state=1234, max_depth=6, n_jobs=-1)
    scikit_rf.fit(X_train, pdf_train[target_var])

    # Make predictions using the model on the test data
    predictions_scikit_rf = scikit_rf.predict_proba(X_test)
    pdf_test['p1'] = predictions_scikit_rf[:, 1]

    return scikit_rf
