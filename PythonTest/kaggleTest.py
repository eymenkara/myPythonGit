import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Create filepath
melbourne_filepath = "/Users/eymenkara/Desktop/melb_data.csv"

# Import datasheet
melbourne_data = pd.read_csv(melbourne_filepath)

# Summarize data
print(melbourne_data.describe())

# Display columns
print(melbourne_data.columns)

# Drop missing data
print(melbourne_data.count())
melbourne_data = melbourne_data.dropna(axis=0)
print(melbourne_data.count())

# Selecting prediction target
y = melbourne_data.Price

# Selecting features
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[features]

# Checking data
print(X.describe())
print(X.head())

# Splitting data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# Defining and fitting model
model = DecisionTreeRegressor(random_state=1)
model.fit(train_X, train_y)

# Trying out predictions
print("Making predictions for the following 5 houses:")
print(val_X.head())
print("The predictions are")
print(model.predict(val_X.head()))
print(val_y.head())

# Model Validation
val_predictions = model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))