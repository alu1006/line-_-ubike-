import requests
r=requests.get('http://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limit=300')
print(r.json())
all_records = r.json()['result']['records']

## 這裡是將資料轉換成pandas的DataFrame
import pandas as pd
df = pd.DataFrame(all_records)
print(df)
# df.to_csv('data.csv')
#每欄的型態
print(df.dtypes)

df['lat'] = df['lat'].astype(float)
df['lng'] = df['lng'].astype(float)
print(df.dtypes)

from geopy.distance import geodesic
for _, row in df.iterrows():
    df['distance'] = geodesic((24.993628, 121.301435), (row['lat'], row['lng'])).meters
df['distance'] = df.apply(lambda row: geodesic((24.993628, 121.301435), (row['lat'], row['lng'])).meters, axis=1)
print(df.head())