import pandas as pd 
df = pd.read_csv("top_1000_youtubers.csv")
Turkish = df.loc[(df["Audience Country"]=="Turkey")]
