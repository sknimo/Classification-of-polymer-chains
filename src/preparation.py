import pandas as pd
import data.make_datasets as datafunc


f_name = '../data/raw/Dataset.csv'
raw_data = pd.read_csv(f_name)

# generating a more reliable dataset and storing it in interim folder
new_data = datafunc.distribution_generation(raw_data)
new_dist = pd.DataFrame(new_data,columns=['chain_length','weight_fraction'])
new_dist.to_csv('../data/interim/chain_distribution.csv',index=False)
