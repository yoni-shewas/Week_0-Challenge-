import pandas as pd


def clean_data(filename):
    try:
        # read csv file
        df = pd.read_csv(filename)

        # remove missing and duplicates value
        df = df.dropna()
        df = df.drop_duplicates()
        df = df.reset_index(drop=True)

        # measurements from modules and sensors that are irrelevant
        df = df.drop('ModA (W/m²)', axis=1)
        df = df.drop('ModB (W/m²)', axis=1)
        # cleaning data of the modules used
        df = df.drop('Cleaning (1 or 0)', axis=1)
        # temperature of modules used
        df = df.drop('TModA (°C)', axis=1)
        df = df.drop('TModB (°C)', axis=1)
        # standard deviation of modules used
        df = df.drop('WSstdev (m/s)', axis=1)
        df = df.drop('WDstdev', axis=1)
        # comments
        df = df.drop('Comments', axis=1)

        # Save cleaned data to a new CSV file
        cleaned_filename = f"cleaned_data/{filename}"
        df.to_csv(cleaned_filename, index=False)
        print("Data cleaned and saved to cleaned_data")

    except Exception as e:
        print(f'An error occurred: {e}')


# Example usage:
# Call the clean_data() function from statistical_analysis.py module and pass the filename
# For example:
# from data_cleaning import clean_data
# filename = "your_dataset.csv"  # Provide the filename here
# clean_data(filename)
