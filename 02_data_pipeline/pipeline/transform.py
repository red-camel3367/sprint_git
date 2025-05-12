def transformer(pandas_df):
    print("TRANSFORMER 시작!")
    t_df = pandas_df.value_counts('type1').to_frame().reset_index()
    
    return t_df