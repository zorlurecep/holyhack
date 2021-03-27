import pandas as pd
import time


class Data:

    def __init__(self):
        self.df = self.init_data_frame(r'data.tsv')
        self.titles_and_ids = dict(zip(self.df.primaryTitle, self.df.tconst))

    def init_data_frame(self, data_path):
        t1 = time.time()
        df = pd.read_csv(data_path, sep='\t',
                         dtype={'tconst': 'string', 'titleType': 'string', 'primaryTitle': 'string',
                                'originalTitle': 'string', 'startYear': 'string'},
                         usecols=['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'startYear',
                                  'genres'])  # read the csv file
        # (put 'r' before the path string to address any special characters in the path, such as '\').
        # Don't forget to put the file name at the end of the path + ".csv"
        t2 = time.time()
        print('reading time is: ', t2 - t1)

        return df

    def title_to_id(self, title):
        return self.titles_and_ids[title]


# data = Data()
# print(data.title_to_id('The God Father'))
# t1 = time.time_ns()
# print(data.df.loc[600000:600006, 'primaryTitle'])
# t2 = time.time_ns()
# print('\nfinding time 1 is: ', (t2 - t1)/1000000)
# time.sleep(1)
#
# t1 = time.time_ns()
# print(data.df[600000:600006]['primaryTitle'])
# t2 = time.time_ns()
# print('\nfinding time 2 is: ', (t2 - t1)/1000000)
# time.sleep(1)
#
# t1 = time.time_ns()
# print(data.df[600000:600001]['primaryTitle'])
# t2 = time.time_ns()
# print('\nfinding time 3 is: ', (t2 - t1)/1000000)
