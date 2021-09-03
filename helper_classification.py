import numpy as np
import scipy.stats as stats
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier

def clean(val):
	val = val/2
	return val

def multiply(a, b):
    return a * b

def get_started(data): 
      data.columns = [column.lower().replace(' ', '_').replace('#_','') for column in data.columns]
      print("shape dataframe: ", data.shape, data.info())

def regressor_code (data, i, model):
    y = data[i]
    X = data.drop([i],axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("r2 score: ", r2_score(y_test, predictions), ", MAE: ", mean_absolute_error(y_test, predictions), ", RMSE: ", mean_squared_error(y_test, predictions, squared=False))
    score = model.score(X_test, y_test)
    print ("score: ", score)    

def chi_square_execute(data, columns=[]):
    for i in columns:
        for j in columns:
            if i != j:
                chi_square(data, i, j)
    
def chi_square(data, m, n):
    data_crosstab = pd.crosstab(data[m], data[n], margins=True, margins_name="Total")
    # significance level
    alpha = 0.05
    # Calcualtion of Chisquare test statistics
    chi_square = 0
    rows = data[m].unique()
    columns = data[n].unique()
    for i in columns:
        for j in rows:
            O = data_crosstab[i][j]
            E = data_crosstab[i]['Total'] * data_crosstab['Total'][j] / data_crosstab['Total']['Total']
            chi_square += (O-E)**2/E
    print("\n--------------------------------------------------------------------------------------")
    print("\n--------------------------------------------------------------------------------------")
    print("H₀: column", m, " and column", n, "are independent, i.e. no relationship")
    print("H₁: column", m, " and column", n, "are independent, i.e. ∃ a relationship")
    print("α = 0.05")
   

# The p-value approach
    print("The p-value approach: The p-value approach to hypothesis testing in the decision rule")
    p_value = 1 - stats.norm.cdf(chi_square, (len(rows)-1)*(len(columns)-1))
    conclusion = "Failed to reject the null hypothesis."
    if p_value <= alpha:
        conclusion = "Null Hypothesis is rejected."
        
    print("chisquare-score is:", chi_square, " and p value is:", p_value)
    print(conclusion)
    
    # The critical value approach

    print("The critical value approach: The critical value approach to hypothesis testing in the decision rule")
    critical_value = stats.chi2.ppf(1-alpha, (len(rows)-1)*(len(columns)-1))
    conclusion = "Failed to reject the null hypothesis."
    if chi_square > critical_value:
        conclusion = "Null Hypothesis is rejected."
        
    print("chisquare-score is:", chi_square, " and p value is:", critical_value)
    print(conclusion)
    
    
    
def boxcox_transform(data):
    numeric_cols = data.select_dtypes(np.number).columns
    _ci = {column: None for column in numeric_cols}
    for column in numeric_cols:
        data[column] = np.where(data[column]<=0, np.NAN, data[column]) 
        data[column] = data[column].fillna(data[column].mean())
        transformed_data, ci = stats.boxcox(data[column])
        data[column] = transformed_data
        _ci[column] = [ci] 
    return data, _ci

def percantage_null(data):
    nulls = pd.DataFrame(data.isna().sum()*100/len(data), columns=['percentage'])
    print(nulls.sort_values('percentage', ascending = False))
    
    
def value_counts(data):
    for col in data:
        print(data[col].value_counts(), '\n')
        
def replace_by_mean(data, columns = []):
    for i in columns:
        data[i].fillna(data[i].mean(), inplace = True)

def regressor_code (data, X, y, model):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("r2 score: ", r2_score(y_test, predictions), ", MAE: ", mean_absolute_error(y_test, predictions), ", RMSE: ", mean_squared_error(y_test, predictions, squared=False))
    score = model.score(X_test, y_test)
    print ("score: ", score)

def money(s):
    if s.startswith('€'):
        s = s[1:]
    multiplier = None
    if s.endswith('M'):
        s = s[:-1]
        multiplier = 1e6
    elif s.endswith('B'):
        s = s[:-1]
        multiplier = 1e9
    elif s.endswith('K'):
        s = s[:-1]
        multiplier = 1e3
    f = float(s)
    if multiplier:
        f = f * multiplier
    return f


def split_year(x):
  years = [int(i) for i in x.split() if i.isdigit()]
  if (('loan') not in str(x).lower()):
    if len(years) == 2: 
      x = years[1] - years[0]
      return int(x)
    elif len(years) == 1: 
      x = 1 
    else: 
      return 0
  else: 
    return 0

def get_statistics(data, in_columns=[]):
    for column in in_columns: 
        print(column)
        print("Maximum: ", round(data[column].max(), 2), ", Minimum: ", round(data[column].min(), 2))
        print("Mean: ", round(data[column].mean(), 2), ", Standard Deviation: ", round(data[column].std(), 2))
        print("")
        

def remove_outliers(data, threshold=1.5, in_columns=[], skip_columns=[]):
    for column in in_columns:
        if column not in skip_columns:
            upper = np.percentile(data[column],75)
            lower = np.percentile(data[column],25)
            iqr = upper - lower
            upper_limit = upper + (threshold * iqr)
            lower_limit = lower - (threshold * iqr)
            data = data[(data[column]>lower_limit) & (data[column]<upper_limit)]
    return data

def using_KNNClassifier(y_train,X_train,y_test,X_test,n):
    
    model = KNeighborsClassifier()
    classification = KNeighborsClassifier(n_neighbors=n)
    classification.fit(X_train, y_train)
    predictions = classification.predict(X_test)
    score = classification.score(X_test, y_test)
    print("accuracy score:", score)
    y_pred = model.predict(X_test)
    predictions = classification.predict(X_test)
    print(confusion_matrix(y_test, predictions))
    
    cf_matrix = confusion_matrix(y_test, predictions)
    group_names = ['True No', 'False No',
                   'False Yes', 'True Yes',]

    group_counts = ["{0:0.0f}".format(value) for value in cf_matrix.flatten()]
    group_percentages = ["{0:.2%}".format(value) for value in cf_matrix.flatten()/np.sum(cf_matrix)]
    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names,group_counts,group_percentages)]
    labels = np.asarray(labels).reshape(2,2)
    sns.heatmap(cf_matrix, annot=labels, fmt='', cmap='Blues')


def unique_val(df):
    for col_names in list(df):
        print("\n" + col_names)
        print(df[col_names].unique(), '\n')

def clean_headers(df):
    df.columns = [x.lower().replace(" ", "_") for x in df.columns]
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
            , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    keep = ['_']
    cols = df.columns
    new_col_names = []
    for col in cols:
        new_col = ''
        for alphabet in col:
            if (alphabet in num) or (alphabet in char) or (alphabet in keep):
                new_col += alphabet
        new_col_names.append(new_col)

    df.columns = new_col_names
    return df

# df['contract_num'] = df['contract'].apply(contract_num)