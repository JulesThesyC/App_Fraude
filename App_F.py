
from re import M
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from scikitplot.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall
from sklearn.metrics import precision_score, recall_score


def main():
    st.title("Application de Machine Learning pour la détection de Fraude sur les cartes bancaire")
    st.subheader("Auteur : Jules COLONAS")
    
if __name__ == '__main__':
    main()