#!/usr/bin/python3.7
import collections
import operator
import os
from pickle import dump, load

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import (AdaBoostClassifier, GradientBoostingClassifier,
                              RandomForestClassifier)
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (RepeatedStratifiedKFold, StratifiedKFold,
                                     cross_val_predict)
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from metric import apbd, apbd_norm, precision_at_k


RandomState = np.random.seed(1)


def get_truebugs_mapping(Y_test, indices_test):
    truebugs = []
    tb_map = {}
    for i in range(len(indices_test)):
        id_ = indices_test[i]
        class_ = Y_test[i]
        if class_ == 1 or class_ == "TrueBug":  # buggy
            truebugs.append(id_)
        tb_map[id_] = class_    
    return truebugs, tb_map


def prioritize_probBased_afterCV(predict_proba, y_pred):
    prio_aux = []
    for i in range(len(indices)):
        id_ = indices[i]
        pred = y_pred[i]
        p_nonbuggy = predict_proba[i][0]
        p_buggy = predict_proba[i][1]
        prio_aux.append([id_, pred, p_buggy, p_nonbuggy])
    
    # Prioritize classification based on class probability
    prioritized = prio_aux[:]
    prioritized = sorted(prioritized, key = operator.itemgetter(0))  
    prioritized = sorted(prioritized, key = operator.itemgetter(3))  
    prioritized = sorted(prioritized, key = operator.itemgetter(2), reverse=True) 

    prio_b_srtd, prio_nb_srtd = [], []
    for p in prioritized:
        if p[1] == 1:
            prio_b_srtd.append(p[0])
        elif p[1] == 0:
            prio_nb_srtd.append(p[0])
    prio_final = [i[0] for i in prioritized]
    prioritized = prio_final[:]

    return prioritized, prio_b_srtd, prio_nb_srtd


def get_y_plot_list(prioritized, truebugs, tb_map):
    count_tb = 0
    accum_tb = 0.0
    y_plot_list = []
    for i in prioritized:
        if tb_map[i]:
            count_tb += 1
        accum_tb = count_tb/len(truebugs) * 100
        y_plot_list.append(accum_tb)
    return y_plot_list



if __name__ == '__main__':
    #================================================================================
    dict_classifiers = collections.OrderedDict()
    dict_classifiers["GradientBoostingClassifier"] = GradientBoostingClassifier()
    dict_classifiers["RandomForest"] = RandomForestClassifier()
    dict_classifiers["LogisticRegression"] = LogisticRegression()
    dict_classifiers["NearestNeighbors"] = KNeighborsClassifier()
    dict_classifiers["DecisionTree"] = DecisionTreeClassifier()
    dict_classifiers["LinearSVM"] = SVC(probability=True)
    dict_classifiers["NeuralNet"] = MLPClassifier(alpha = 1)
    dict_classifiers["NaiveBayes"] = GaussianNB()
    dict_classifiers["AdaBoost"] = AdaBoostClassifier()
    dict_classifiers["GaussianProcess"] = GaussianProcessClassifier()
                                    
    clf_name = "RandomForest"
    clf_name = "LogisticRegression"
    clf_name = "NearestNeighbors"
    clf_name = "DecisionTree"
    clf_name = "LinearSVM"
    clf_name = "NeuralNet"
    clf_name = "NaiveBayes"
    clf_name = "AdaBoost"
    clf_name = "GaussianProcess"
    clf_name = "GradientBoostingClassifier"

    clf = dict_classifiers[clf_name]
    #================================================================================

    n_splits, n_repeats = 10, 30
    outdir = "results"
    df = pd.read_csv("data/training.csv")
    indices = df.index
    truebugs, tb_map = get_truebugs_mapping(df['BUGGY'].values, indices)    

    #================================================================================
    # RANDOM
    #================================================================================
    ## Preparation
    y_col = 'BUGGY'
    x_cols = list(df.columns.values)
    x_cols.remove(y_col)
    y = df[y_col].values
    X = df[x_cols].values
    ## CV
    clf_dummy = DummyClassifier()
    predict_proba = cross_val_predict(clf_dummy, X, y, cv=n_repeats, method='predict_proba')
    y_pred = cross_val_predict(clf_dummy, X, y, cv=n_repeats)
    ## Prioritization
    prioritized, prio_b_srtd, prio_nb_srtd = prioritize_probBased_afterCV(predict_proba, y_pred)
    ## Metrics
    rand_apbd = apbd_norm(prioritized, truebugs)
    print("="*80)
    print("APBD Results")
    print("Random Prioritization")
    print("(NORM)APBD: {}".format(rand_apbd))
    ## Plot
    random_y_plot_list = get_y_plot_list(prioritized, truebugs, tb_map)

    #================================================================================
    # RVprio
    #================================================================================    
    selected_features = load(open(os.path.join("data", "features_selected.data"), "rb"))
    selected_features.append('BUGGY')
    df = df[selected_features]
    ## Preparation
    y_col = 'BUGGY'
    x_cols = list(df.columns.values)
    x_cols.remove(y_col)
    y = df[y_col].values
    X = df[x_cols].values
    ## CV
    predict_proba = cross_val_predict(clf, X, y, cv=n_repeats, method='predict_proba')
    y_pred = cross_val_predict(clf, X, y, cv=n_repeats)
    ## Prioritization
    prioritized, prio_b_srtd, prio_nb_srtd = prioritize_probBased_afterCV(predict_proba, y_pred)
    ## Metrics
    gbc_apbd = apbd_norm(prioritized, truebugs)
    print("RVprio (classifier={})".format(clf_name))
    print("(NORM)APBD: {}".format(gbc_apbd))
    print("="*80)
    print("Prioritized test suite: {}".format(prioritized))
    print("="*80)
    ## Plot
    gbc_y_plot_list = get_y_plot_list(prioritized, truebugs, tb_map)

    #================================================================================
    # Optimal
    #================================================================================
    tb = set(prioritized).intersection(set(truebugs))
    nb = set(prioritized).difference(set(truebugs))
    prioritized = list(tb)+list(nb)
    ## Metrics
    optimal_reg_apbd = apbd(prioritized, truebugs)
    optimal_apbd = apbd_norm(prioritized, truebugs)
    ## Plot
    optimal_y_plot_list = get_y_plot_list(prioritized, truebugs, tb_map)

    #================================================================================
    # Plot
    #================================================================================
    clf_label = r'\textsc{RVprio} prioritization'
    clf_abbrev = r'\textsc{RVprio}'
    x_list = range(1, len(prioritized)+1)
    plt.style.use('ggplot')
    plt.rcParams['xtick.color']='black'
    plt.rcParams['ytick.color']='black'
    plt.rcParams['axes.labelcolor']='black'
    plt.rcParams['legend.fontsize']=12
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.figure(figsize=(8.0,4.1))
    plt.plot(x_list, optimal_y_plot_list, color='blue', linestyle=':', linewidth=1.5, label='Optimal prioritization')
    plt.plot(x_list, gbc_y_plot_list, color='green', linestyle='-', linewidth=1.75, label=clf_label)
    plt.plot(x_list, random_y_plot_list, color='red', linestyle='--', linewidth=1.5, label='Random prioritization')
    plt.text(800, 90, "nAPBD ({}): {}\%".format(clf_abbrev, int(gbc_apbd*100)), fontsize=14)
    plt.text(800, 50, "nAPBD (Random): {}\%".format(int(rand_apbd*100)), fontsize=14)
    plt.xlabel(r'\# of violations analyzed', fontsize=16)
    plt.ylabel(r'\% of true bugs revealed', fontsize=16)    
    plt.legend(loc="lower right")
    plt.savefig(os.path.join(outdir, 'apbd_{}.pdf'.format(clf_name)), bbox_inches="tight", pad_inches=0)
    plt.show()
