import os
import json
import pandas as pd
#

excel_df = pd.read_excel(os.path.join(os.getcwd(), 'section.xlsx'))
#excel_df[['model', 'pk']].to_json(os.path.join(os.getcwd(), 'section.json'), orient='records')
dict_1 = excel_df[['model', 'pk']].to_dict(orient='records')

output = {}
df_size = len(excel_df)
dict_df = excel_df[excel_df.columns.difference(['model', 'pk'])].to_dict(orient='index')

# with open(os.path.join(os.getcwd(), 'section.json')) as data_file:
    #json_data = json.load(data_file)

# for value in json_data:
   #value["fields"] = {}

# d = json_data[0].get('fields')

#for k, dict_):
    #dict_1["fields"] = {v2}

print(dict_1)
