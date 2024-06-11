## Dataset Description
The dataset includes 244 instances that regroup a data of two regions of Algeria,namely the Bejaia region located in the northeast of Algeria and the Sidi Bel-abbes region located in the northwest of Algeria.

122 instances for each region. 

The period from June 2012 to September 2012. 
The dataset includes 11 attribues and 1 output attribue (class)
The 244 instances have been classified into fire (138 classes) and not fire (106 classes) classes.

Source: https://archive.ics.uci.edu/dataset/547/algerian+forest+fires+dataset

## Dataset columns
1. Date : (DD/MM/YYYY) Day, month ('june' to 'september'), year (2012)
Weather data observations 
2. Temp : temperature noon (temperature max)  in Celsius degrees: 22 to 42
3. RH : Relative Humidity in %: 21 to 90 
4. Ws :Wind speed in km/h: 6 to 29 
5. Rain: total day in mm: 0 to 16.8
FWI Components  
6. Fine Fuel Moisture Code (FFMC) index from the FWI system: 28.6 to 92.5 
7. Duff Moisture Code (DMC) index from the FWI system: 1.1 to 65.9 
8. Drought Code (DC) index from the FWI system:  7 to 220.4
9. Initial Spread Index (ISI) index from the FWI system: 0 to 18.5 
10. Buildup Index (BUI) index from the FWI system: 1.1 to 68
11. Fire Weather Index (FWI) Index: 0 to 31.1
12. Classes: two classes, namely   Fire and not Fire

## Model Comparisons
The goal is to compare different regression models to predict the class based on the given attributes.

Linear Regression

Mean Absolute Error (MAE): 0.5468
Root Mean Square Error (RMSE): 0.7395
R2 Score: 0.9848
Ridge Regression

MAE: 0.5642
RMSE: 0.7512
R2 Score: 0.9843
Lasso Regression

MAE: 1.1332
RMSE: 1.0645
R2 Score: 0.9492
ElasticNet Regression

MAE: 1.8822
RMSE: 1.3719
R2 Score: 0.8753

## Hyperparameter Tuning Results
Using cross-validation techniques to fine-tune the hyperparameters of Ridge, Lasso, and ElasticNet models:

RidgeCV

MAE: 0.5642
Mean Squared Error (MSE): 0.6949
R2 Score: 0.9843
Best Alpha: 1.0
LassoCV

MAE: 0.5642
MSE: 0.6949
R2 Score: 0.9843
Best Alpha: 1.0
ElasticNetCV

MAE: 0.5642
MSE: 0.6949
R2 Score: 0.9843
Best Alpha: 1.0

## Analysis and Insights
Linear Regression and Ridge Regression perform similarly, achieving high R2 scores, indicating that they explain a significant portion of the variance in the data.
Lasso Regression has a lower R2 score compared to Linear and Ridge, implying less explanatory power.
ElasticNet Regression shows the lowest performance among the four models, indicating it might not be well-suited for this dataset without further tuning.
The hyperparameter tuning for RidgeCV, LassoCV, and ElasticNetCV yielded similar performance metrics, with the best alpha value found to be 1.0 for all.
