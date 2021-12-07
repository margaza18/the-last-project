import pandas as pd


class ReadExcelTable:
    @classmethod
    def read_table(cls, filepath):
        excel_data = pd.read_excel(filepath)
        data_frame = pd.DataFrame(excel_data)
        return data_frame
