from consolemenu import *
from consolemenu.items import *

from Converter import Converter
from MakePlot import MakePlot
from WriteExcelTable import WriteExcelTable

menu = ConsoleMenu("Laboratory work", "FIT 6 group, 1 year")

################################################
# WriteExcelTable
# - write_table()
# - write_column()
# - get_all_columns()
write_excel_table = WriteExcelTable()

# MakePlot
# - make_plot("type"), type - bar,line,pie
# - make_histogram()
make_graph = MakePlot()

# Converter
# to_json()
# to_text()
converter = Converter()
################################################

print_excel_table = FunctionItem("Print excel table", write_excel_table.write_table, args=None, kwargs=None,
                                 menu=ConsoleMenu,
                                 should_exit=False)

print_excel_table_column = FunctionItem("Print excel column", write_excel_table.write_column, args=None, kwargs=None,
                                        menu=ConsoleMenu, should_exit=False)

show_line_plot_from_table = FunctionItem("Show line plot", make_graph.make_line_plot, args=None, kwargs=None,
                                         menu=ConsoleMenu, should_exit=False)

show_bar_plot_from_table = FunctionItem("Show bar plot", make_graph.make_bar_plot, args=None, kwargs=None,
                                        menu=ConsoleMenu, should_exit=False)

show_histogram_from_table = FunctionItem("Show histogram", make_graph.make_histogram, args=None, kwargs=None,
                                         menu=ConsoleMenu, should_exit=False)

convert_to_json = FunctionItem("Convert to json", converter.to_json, args=None, kwargs=None,
                               menu=ConsoleMenu, should_exit=False)
convert_to_text = FunctionItem("Convert to txt", converter.to_text, args=None, kwargs=None,
                               menu=ConsoleMenu, should_exit=False)

menu.append_item(print_excel_table_column)
menu.append_item(show_line_plot_from_table)
menu.append_item(show_bar_plot_from_table)
menu.append_item(show_histogram_from_table)
menu.append_item(convert_to_json)
menu.append_item(convert_to_text)
menu.show()
