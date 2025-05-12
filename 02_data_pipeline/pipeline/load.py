def loader(pandas_df, connection_obj, table_name):
    print("LOADER 시작!")
    try:
        pandas_df.to_sql(
            name=table_name,
            con=connection_obj,
            if_exists='replace',
            index=False
        )
        print("POSTGRESQL에 테이블 저장 완료!")
    except:
        print("저장이 제대로 되지 않았습니다.")