import pandas as pd
def import_csv_to_dataframe(file_path):
    try:
        df=pd.read_csv()
        print("CSV file successfully imported into DataFrame!")
        return df
    except FileNotFoundError:
        print("Error: File not Found")
    except pd.errors.EmptyDataError:
        print("Error: File is empty")
    except pd.errors.ParserError:
        print("Error: File could not be parsed.")
def export_dataframe_to_csv(df, file_path):
    try:
        df.to_csv(file_path, index=False)
        print("DataFrame successfully exported to CSV File!")
    except Exception as e:
        print(f"Error{e}")
if __name__=="__main__":
    file_path='input.csv'
    df=input_csv_to_dataframe(file_path)
    if df is not None:
        print(df)
        output_path='output.csv'
        export_dataframe_to_csv(df, output_path)
