import pandas as pd

csv_file_path = './fashionpediaBenchmark/models/official/detection/projects/fashionpedia/dataset/fashionpedia_label_map.csv'


df = pd.read_csv(csv_file_path, sep=':', header=None)

# Now 'df' is a DataFrame containing the contents of the CSV file
print(df.head())  # T
print(df[df[0] == 1][1][0])