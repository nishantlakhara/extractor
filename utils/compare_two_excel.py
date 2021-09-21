import pandas as pd
import numpy as np


def main():
    excel_1 = 'Book1'
    excel_2 = 'Book3'
    ext = '.xlsx'
    sheets_dict1 = pd.read_excel(excel_1 + ext, sheet_name=None)
    sheets_dict2 = pd.read_excel(excel_2 + ext, sheet_name=None)

    # Check for differences
    for key in sheets_dict1:
        df1 = sheets_dict1[key]
        df2 = sheets_dict2[key]

        # Check for differences
        comparison_values = df1.values == df2.values
        print(comparison_values)

        # Index of the Cell with False value
        rows, cols = np.where(comparison_values == False)
        for item in zip(rows, cols):
            df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]])

        # print df1
        print(df1)
        df1.to_excel(f'./{excel_1}_{excel_2}_{key}_sheet_diff.xlsx', index=False, header=True)

if __name__ == "__main__":
    main()