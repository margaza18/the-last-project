from ReadExcelTable import ReadExcelTable
from Tkinter import open_window_dialog

import pandas as pd


class WriteExcelTable:
    __read_excel_table = ReadExcelTable()
    data = ReadExcelTable.read_table(open_window_dialog())

    def write_table(self):
        print(self.data)

    def write_column(self):
        print(f"Columns: {self.get_all_columns()}\n")
        selected_column = input("Enter column name: ")

        if selected_column in self.get_all_columns():
            data_frame = pd.DataFrame(self.data, columns=[selected_column])
            print(data_frame)

    def get_all_columns(self):
        return self.data.columns.values
