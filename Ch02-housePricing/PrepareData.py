import os
import tarfile
import pandas as pd
from six.moves import urllib
import numpy as np


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


'''----------------TEST SET------------------'''
'''
Train - Test split splits at general 80% and 20% respectively.
Note:- test data set should be consistent through out the training, at least if your data set is of small in size.
if data set is small, stratify dataset to represent all catagory equally, for example if company is surveying in india
with the smaple of 1000 people, to represent 40% women population, sample has to be chosen in proportion.

Note:- To make the test set consistent, use any identifier to create test set.
'''

#Approach 1st: using identifier to split data set.
from zlib import crc32

def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier)) < test_ratio * 2**32

def slip_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_ : is_id_in_test_set(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

#Approch 2nd: using sckit learns test_train_slip
from sklearn.model_selection import train_test_split
def split_using_sckit_lear(data, test_size):
    return train_test_split(data, test_size=0.2, random_state=42)

#Approach 3rd: generating stratified train test set
from sklearn.model_selection import StratifiedShuffleSplit
def stratified_split(data, field):
    splitter = StratifiedShuffleSplit(n_splits=10, test_size=0.2, random_state=42)
    stratum = []
    for train_indices, test_indices in splitter.split(data, data[field]):
        train_set = data.iloc[train_indices]
        test_set = data.iloc[test_indices]
        stratum.append([train_set, test_set])

    return stratum[0]

#Approach 4th: stratified sampling using train_test_split
def stratified_train_test_split(data, field, test_size):
    return train_test_split(data, test_size=test_size, stratify=data[field], random_state=42)
