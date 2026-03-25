import pandas as pd

def load_data(path):
    df = pd.read_json(path, lines=True)
    df = df[['title', 'summary']]
    df = df.dropna()
    return df