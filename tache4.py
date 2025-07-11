def count_gender(df):
    # Compter les occurrences de chaque genre
    gender_counts = df['gender'].value_counts()
    
    # Afficher les résultats
    print("Nombre de lignes par genre:")
    print(f"Female: {gender_counts.get('Female', 0)}")
    print(f"Male: {gender_counts.get('Male', 0)}")

