import pandas as pd

def show_stats(df: pd.DataFrame):
    print("Statistiques descriptives :")
    print(df.describe())
    print("\n" + "="*50 + "\n")
    print("Informations générales sur le DataFrame :")
    df.info()

    print('omar and hamid')