import pandas as pd

def extractor(connection_obj, query):
    print("EXTRACTOR 시작!")
    df = pd.read_sql(
        sql=query,
        con=connection_obj
        )
    
    return df