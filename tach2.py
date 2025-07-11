


from src.clean import clean_data

def pipeline_complet():
    df = charger_donnees('data.csv')
    df = clean_data(df)
    df = transformer_donnees(df)
    afficher_apercu(df)
    count_gender(df)
