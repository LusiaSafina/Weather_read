import pandas as pd

class DataWriter:
    def save_csv(dt_list, name_file):
#    """ сохраняет данные в файл формата .csv с именем name_file """
        df1 = pd.DataFrame(dt_list)
        df1.to_csv(fr'c:\000\{name_file}.csv', index=False)