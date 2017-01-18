import os
import pandas as pd
"""
Need a blank and our own id. Sigh.
"""

df = pd.read_excel(os.path.join(os.getcwd(), 'section.xlsx'))
print(df.head())
df.to_csv(os.path.join(os.getcwd(), 'section.csv'), index=False)
