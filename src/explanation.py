import shap
from matplotlib import pyplot as plt


def report_model(model, X_train):
    explainer = shap.Explainer(model.model)
    shap_values = explainer(X_train)
    shap.summary_plot(shap_values, X_train)
