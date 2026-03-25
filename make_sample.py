import pandas as pd

chunks = []

for chunk in pd.read_json("arxiv-metadata-oai-snapshot.json", lines=True, chunksize=500):
    chunk = chunk[['title', 'summary', 'categories']]
    chunk = chunk[chunk['categories'].str.contains("cs.")]
    
    chunks.append(chunk)
    
    if len(chunks)*500 >= 1000:
        break

df = pd.concat(chunks)
df = df.dropna()

df.to_json("sample_data.json", orient="records", lines=True)

print("✅ Sample dataset created")