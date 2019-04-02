import sys
import os
import uuid
import pendulum
from configparser import ConfigParser
import enum


class PROBLEM_TYPE(enum.Enum):

    BINARY_CLASSIFICATION       = 'binary classification'
    REGRESSION                  = 'regression'
    MULTI_CLASS_CLASSIFICATION  = 'multiclass classification'
# end

class MODEL(enum.Enum):

    LOGISTIC_REGRESSION      = 'LogisticRegression'
    DECISION_TREE_CLASSIFIER = 'DecisionTreeClassifier'
    # from sklearn.neighbors import KNeighborsClassifier
    # from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    # from sklearn.naive_bayes import GaussianNB
    # from sklearn.svm import SVC


class USING(enum.Enum):
    NN = 'NN'
# end


def get_utc_timestamp():
    return pendulum.now('UTC')
# end


def display_message(message):
    print('{} {}'.format(get_utc_timestamp(), message))
# end


def main():
    display_message('Starting...')

    display_message('Read configuration settings...') # ................................................................
    parser = ConfigParser()
    parser.read('/home/abjax/PycharmProjects/2019-04-02_py3.7_ml_builder_tool/figs/main.ini')

    prblem_type = parser.get('MAIN',  'PROBLEM_TYPE')
    plot_style  = parser.get('PLOTS', 'STYLE')
    oFile       = parser.get('IO',    'OUT')
    using_nn    = parser.get('USING', 'NN')
    display_message('Configuration settings read.') # ..................................................................

    out = open(oFile, 'wt')

    display_message('About to write imports...') # .....................................................................

    out.write('import sys')
    out.write('\n')
    out.write('import os')
    out.write('\n')
    out.write('import numpy as np')
    out.write('\n')
    out.write('import matplotlib')
    out.write('\n')
    out.write('from matplotlib import pyplot as plt')
    out.write('\n')
    out.write('import pandas as pd')
    out.write('\n')

    if (prblem_type == PROBLEM_TYPE.REGRESSION.value):
        out.write('from sklearn.metrics import mean_squared_error')
        out.write('\n')
    else:
        out.write('# Metrics')
        out.write('\n')
        out.write('from sklearn.metrics import classification_report')
        out.write('\n')
        out.write('from sklearn.metrics import confusion_matrix')
        out.write('\n')
        out.write('from sklearn.metrics import accuracy_score')
        out.write('\n')
    display_message('Imports written.') # ..............................................................................

    out.write('\n')
    out.write('plt.style.use("{}")'.format(plot_style))
    out.write('\n')

    display_message('Closing Out File...')
    out.close()
    display_message('Outfile closed.')

    display_message('Done.')


if __name__ == '__main__':
    main()
