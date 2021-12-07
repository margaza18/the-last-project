import matplotlib.pyplot as plt
from WriteExcelTable import WriteExcelTable


class MakePlot:
    __excel_data = WriteExcelTable.data
    __get_all_columns = WriteExcelTable().get_all_columns()

    def make_bar_plot(self):
        print(f"All columns: {self.__get_all_columns}\n")
        first_column = input("Enter first column - X: ")
        second_column = input("Enter second column - Y: ")
        try:
            if first_column and second_column in self.__get_all_columns:
                self.__excel_data.plot(x=second_column, y=first_column, figsize=(10, 10), kind="bar")
                plt.show()
        except TypeError:
            print("No numeric data to plot!")

    def make_line_plot(self):
        print(f"All columns: {self.__get_all_columns}\n")
        first_column = input("Enter first column - X: ")
        second_column = input("Enter second column - Y: ")
        try:
            if first_column and second_column in self.__get_all_columns:
                self.__excel_data.plot(x=second_column, y=first_column, figsize=(10, 10), kind="line")
                plt.show()
        except TypeError:
            print("No numeric data to plot!")

    def make_histogram(self):
        self.__excel_data.plot.hist(bins=12, alpha=0.5)
        plt.show()
