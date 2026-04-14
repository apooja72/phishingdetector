import pandas as pd

def load_url_data(path):
    df = pd.read_csv(path, sep=None, engine='python')
    return df['url'].values, df['label'].values

def load_email_data(path):
    df = pd.read_csv(path, sep=None, engine='python')
    return df['text'].values, df['label'].values

def load_attachment_data(path):
    df = pd.read_csv(path, sep=None, engine='python')
    return df['filename'].values, df['label'].values