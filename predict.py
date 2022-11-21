import pandas as pd
from sksurv.util import Surv
from sklearn.utils import shuffle
import joblib


##load data
X_test = pd.read_csv("X_test.csv")

##load model
model = joblib.load('GradientBoostingSurvival.pkl')

##get the result and output it in csv format
result_file =model.predict(X_test)
k=['score']
file = pd.DataFrame(result_file,columns=k)
file.to_csv("test_risk_score.csv", index=False)
