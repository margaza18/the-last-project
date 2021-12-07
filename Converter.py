import codecs, json
from WriteExcelTable import WriteExcelTable
import numpy as np


class Converter:
    __data = WriteExcelTable().data
    __numpy_to_list = WriteExcelTable().data.values.tolist()

    def to_json(self):
        filepath = "./to_json.json"
        json.dump(self.__numpy_to_list, codecs.open(filepath, 'w', encoding='utf8', errors='strict'),
                  sort_keys=True,
                  indent=4, default=str)

        print("File has been successfully converted to json!")

    def to_text(self):
        open_file = open('./to_text.txt', 'w')
        for row in self.__numpy_to_list:
            np.savetxt(open_file, row, fmt="%s")
        open_file.close()

        print("File has been successfully converted to text!")
