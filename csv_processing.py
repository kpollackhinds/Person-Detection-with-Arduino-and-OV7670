import pandas as pd

data_df = pd.read_csv('acceleration_data_test2.csv')
acceleration_df = data_df[[' Ax', ' Ay', ' Az']].copy()
#gyroscope_df = data_df['Gx ', 'Gy ', 'Gz ']
# print(data_df.head())

print(acceleration_df.head())