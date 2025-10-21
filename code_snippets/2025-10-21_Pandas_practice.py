import pandas as pd

# create a mini dataset
data = {
        'Plant' : ['Marigold', 'GoldenRod', 'Salvia', 'Oak'],
        'Photon_Count_Day1': [100, 199, 99, 201],
        'Photon_Count_Day2': [121, 215, 111, 233],
        'Soil_pH': [6, 6.9, 7.3, 6.8]}

# Create a DataFrame
df = pd.DataFrame(data)

# Definition of row labels
row_labels = ['MG', 'GR', 'SV', 'OK']

# Specifiy row labels
df.index = row_labels

print(df)

# Print out plant column as Pandas series (Uses single[])
print(df['Plant'])

# Print out plant column as Pandas DataFrame (uses double[[]])
print(df[['Plant']])

# Print DataFrame wiht Plant and Soil_pH columns
print(df[['Plant', 'Soil_pH']])

# Print first observation for marigold
print(df.loc['MG', 'Photon_Count_Day1'])
print(df.iloc[0, 1])

# Print sub-DataFrame
print(df.loc[['MG', 'OK'],['Photon_Count_Day1', 'Soil_pH']])
print(df.iloc[[0, 3], [1, 3]])

# Print Photon_Count_Day2 column as seris and the DataFrame using both .loc and .iloc
print(df.loc[:, 'Photon_Count_Day2'])
print(df.iloc[:, 2])
print(df.loc[:, ['Photon_Count_Day2']])
print(df.iloc[:, [2]])

# Print out Photon_Count_Day1 and Soil_pH as DataFrame
print(df.loc[:,['Photon_Count_Day1', 'Soil_pH']])