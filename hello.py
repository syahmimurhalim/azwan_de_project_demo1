print("HELLO WORLD")

from datetime import datetime

print(datetime.today().isoformat())

import pandas as pd

URL_DATA = 'https://storage.dosm.gov.my/population/population_malaysia.parquet'

df = pd.read_parquet(URL_DATA)
print(df.head())