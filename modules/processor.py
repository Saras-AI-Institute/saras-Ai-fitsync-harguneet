import pandas as pd

def load_data():
    """
    Load the CSV file, handle missing values, and return a cleaned DataFrame.
    """
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv('data/health_data.csv')
    
    # Handle missing values:
    # Fill missing 'Steps' with the median value of the column
    df['Steps'].fillna(df['Steps'].median(), inplace=True)
    
    # Fill missing 'Sleep_Hours' with 7.0
    df['Sleep_Hours'].fillna(7.0, inplace=True)
    
    # Fill missing 'Heart_Rate_bpm' with 68
    df['Heart_Rate_bpm'].fillna(68, inplace=True)
    
    # For other columns, fill missing values with their respective median
    other_columns = ['Calories_Burnt', 'Active_Minutes']
    for column in other_columns:
        df[column].fillna(df[column].median(), inplace=True)
    
    # Convert 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])

    return df

def calculate_recovery_score(df):
    """
    Calculate and add a 'Recovery_score' column to the DataFrame.
    The score is based on Sleep_Hours, Heart_Rate_bpm, and Steps.
    """

    # Initialize the Recovery Score column
    df['Recovery_score'] = 0.0

    # Calculate the score based on Sleep Hours
    # Good sleep (>= 7 hours) increases the score
    # Poor sleep (< 6 hours) significantly reduces the score
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_score'] += 40
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_score'] -= 30

    # Calculate the score based on Heart Rate
    # Lower heart rate is better for recovery
    df['Recovery_score'] += (-0.5) * (df['Heart_Rate_bpm'] - 68)

    # Calculate the score based on Steps
    # More steps are generally good, but excessive activity can be bad
    df['Recovery_score'] += df['Steps'].apply(lambda x: 20 if x < 12000 else -10)

    # Ensure the score stays within 0 to 100
    df['Recovery_score'] = df['Recovery_score'].clip(0, 100)

    return df

def process_data():
    """
    Main function to process data for the Streamlit dashboard.
    This function loads data, calculates recovery scores, and returns the processed DataFrame.
    """

    df = load_data()                # Call load_data to get the cleaned DataFrame
    df = calculate_recovery_score(df)  # Add the Recovery Score by calling calculate_recovery_score
    return df                            # Return the final processed DataFrame

# ... code continues ...