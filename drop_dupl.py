import pandas as pd

# Read the data from a file (update the filename as needed)
input_file = "Table_Matiere.xlsx"  # Replace with your actual file name
output_file = "Table_Matiere_nodup.xlsx"

# Load the data into a pandas DataFrame
df = pd.read_excel(input_file)

# Remove duplicate rows based on the 'Subject' column only
df_cleaned = df.drop_duplicates(subset=['nom_matière'])

# Save the cleaned data to a new file
df_cleaned.to_excel(output_file, index=False)

print(f"Duplicate rows based on 'Subject' removed. Cleaned data saved to '{output_file}'.")
