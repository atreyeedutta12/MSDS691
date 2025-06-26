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
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
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
    if type(GeoEco_stats) == dict:
        df = pd.DataFrame(GeoEco_stats)
    else:
        df = GeoEco_stats
    #df = df.drop(columns=['Interest Rate (Real, %)'])
    #df = df.dropna()
    #df = df.drop(columns=['country_id', 'country_name', 'year'])
    X=df.drop('Government_Revenue_GDP',axis=1)
    y=df['Government_Revenue_GDP']
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    y_pred = model.predict(X_test)
    return y_pred
