#import modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Importing all necessary modules
#import plotly.express as px
#import plotly.graph_objects as go
#from plotly.subplots import make_subplots
#import warnings
#from scipy import stats
#from sklearn.preprocessing import StandardScaler
#from sklearn.decomposition import PCA
#from sklearn.cluster import KMeans
#import country_converter as coco

# Configuration
#warnings.filterwarnings('ignore')
#plt.style.use('seaborn-v0_8')
#sns.set_palette("husl")

# Configuration Plotly pour Kaggle
#import plotly.io as pio
#pio.renderers.default = "notebook"


#Custom function 
def predict_GovRevnGDP(GeoEco_stats, model):
    #if type(GeoEco_stats) == dict:
    df = pd.DataFrame.from_dict(GeoEco_stats,orient = 'columns')
    #else:
        #df = GeoEco_stats
    #df = df.drop('interestRateReal1',axis=1)
    #df = df.dropna()
    #df = df.drop(columns=['country_id1', 'country', 'year1','_id','_updatedDate','_createdDate','_owner'])
    df = df.drop(columns=['interestRateReal1','country_id1', 'country', 'year1','_id','_updatedDate','_createdDate','_owner'])
    X=df.drop('governmentRevenueOfGdp1',axis=1)
    y=df['governmentRevenueOfGdp1']
    #results = []
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    #model.fit(X, y)
    y_pred = model.predict(X_test)
    #y_pred = model.predict(X)
    #return y_pred
    #Compare Actual vs Predicted
    Predictions = pd.DataFrame(y_pred).reset_index(drop = True).rename(columns ={0:"Predicted"})
    Actual = pd.DataFrame(y_test).reset_index(drop = True).rename(columns ={"governmentRevenueOfGdp1":"Actual"})
    compare_GovRevGDP = pd.concat([Predictions,Actual],axis = 1)
    return compare_GovRevGDP.to_dict(orient='records')
    #return compare_GovRevGDP.style.set_caption("Government Revenue of %GDP Comparison")
