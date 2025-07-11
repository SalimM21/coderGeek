import pandas as pd

def load_data(filepath):
    """Charge les données depuis un fichier CSV"""
    return pd.read_csv(filepath)

def clean_data(df):
    # Supprimer les doublons
    df = df.drop_duplicates()
    
    # Supprimer les lignes avec valeurs manquantes
    df = df.dropna()
    
    # Standardiser la colonne gender
    df['gender'] = df['gender'].str.capitalize()
    df = df[df['gender'].isin(['Male', 'Female'])]
    
    return df

def transform_data(df):
    # Exemple de transformation (à adapter)
    if 'birth_date' in df.columns:
        df['birth_date'] = pd.to_datetime(df['birth_date'])
        df['age'] = (pd.to_datetime('today') - df['birth_date']).dt.days // 365
    
    return df

def count_gender(df):
    gender_counts = df['gender'].value_counts()
    print("\nNombre de lignes par genre:")
    print(f"Female: {gender_counts.get('Female', 0)}")
    print(f"Male: {gender_counts.get('Male', 0)}")

def process_data(filepath):    # 1. Chargement
    print("Chargement des données...")
    df = load_data(filepath)
    print("Aperçu initial des données:")
    print(df.head())
    
    # 2. Nettoyage
    print("\nNettoyage des données...")
    df_clean = clean_data(df)
    print("Aperçu après nettoyage:")
    print(df_clean.head())
    
    # 3. Transformation
    print("\nTransformation des données...")
    df_transformed = transform_data(df_clean)
    print("Aperçu après transformation:")
    print(df_transformed.head())
    
    # 4. Analyse et affichage
    count_gender(df_transformed)
    
    return df_transformed