import pandas as pd
from nltk.tokenize import  word_tokenize
from nltk.stem.snowball import SnowballStemmer as s_stem

def toknize_and_stem(text):
    tokens=word_tokenize(text)
    stemmed = [s_stem("english").stem(t) for t in tokens]
    return stemmed

def process_csv(csv_path="gemma_data_set_prompt_recover_1.csv"):
    df=pd.read_csv(csv_path)
    df['tokenize&stem']=df['original_text'].apply(toknize_and_stem)
    df['tokenize&stem'].to_csv("output.csv",index=False)
    print(df['tokenize&stem'])

process_csv()