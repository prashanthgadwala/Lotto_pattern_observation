import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/prashanthgadwala/PycharmProjects/Lotto_pattern_observation/Lotto.csv'
column_names = ['Tag', 'Monat', 'Jahr', 'Zahl1', 'Zahl2', 'Zahl3', 'Zahl4', 'Zahl5', 'Zahl6', 'Superzahl']

# Load data into a Pandas DataFrame
lottery_df = pd.read_csv(file_path, usecols=column_names)

# Calculate frequency of each number
num_frequency = pd.concat([lottery_df[col].value_counts().sort_index() for col in column_names[3:-2]], axis=1)
num_frequency.columns = column_names[3:-2]

# Plot frequency of each number
num_frequency.plot(kind='bar', figsize=(10, 6))
plt.title('Frequency of Each Number in Lottery Draws')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.show()

# Calculate frequency of the Super Number
super_num_frequency = lottery_df['Superzahl'].value_counts().sort_index()

# Plot frequency of the Super Number
super_num_frequency.plot(kind='bar', figsize=(6, 4), color='orange')
plt.title('Frequency of Super Number in Lottery Draws')
plt.xlabel('Super Number')
plt.ylabel('Frequency')
plt.show()
