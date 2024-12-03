import pandas as pd
import matplotlib.pyplot as plt

# File paths for the datasets
census_file_path = '/Users/abigailarace/Desktop/census_data.csv'
county_codes_file_path = '/Users/abigailarace/Desktop/county_codes.csv'

# Load the datasets
census_data = pd.read_csv(census_file_path)
county_codes = pd.read_csv(county_codes_file_path)

# Inspect the datasets
print("Census Data Overview:")
print(census_data.head())
print("\nCounty Codes Overview:")
print(county_codes.head())

# Filter for Davidson County
# Find the StateICP and County codes for Davidson County
davidson_county_code = county_codes[(county_codes['State'] == 'Tennessee') & 
                                    (county_codes['County'].str.contains('Davidson', na=False))]
state_icp_code = davidson_county_code['STATEICP'].iloc[0]
county_code = davidson_county_code['County cod'].iloc[0]

# Filter census data for Davidson County and the years 1820, 1830, and 1840
filtered_data = census_data[(census_data['stateicp'] == state_icp_code) & 
                            (census_data['county'] == county_code) & 
                            (census_data['year'].isin([1820, 1830, 1840]))]

# Group by year and sum the total population
population_by_year = filtered_data.groupby('year')['ntotal'].sum()

print("\nPopulation by Year (Davidson County):")
print(population_by_year)

# Plot the population change
plt.figure(figsize=(8, 6))
plt.plot(population_by_year.index, population_by_year.values, marker='o', linestyle='-', color='blue')
plt.title('Population Change in Davidson County (1820-1840)')
plt.xlabel('Year')
plt.ylabel('Total Population')
plt.xticks(population_by_year.index)  # Ensure correct x-axis labels
plt.grid(True)
plt.show()
