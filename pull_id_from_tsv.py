import pandas as pd
import time


class Data:

    def __init__(self):
        # self.df = self.init_data_frame(r'data.tsv')
        t1 = time.time()
        self.df = pd.read_csv(r'C:\Users\menes\Downloads\data.tsv', sep='\t',
                              dtype={'tconst': 'string', 'titleType': 'string', 'primaryTitle': 'string',
                                     'originalTitle': 'string', 'startYear': 'string'},
                              usecols=['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'startYear',
                                       'genres'])
        t2 = time.time()
        print('reading time is: ', t2 - t1)

    def title_to_id(self, title):
        """
        :param title: original title of a work (exact)
        :return: a set of imdb-id's of all works with exactly the same name
        """
        rows_with_title = self.df[self.df.originalTitle == title]
        return set(rows_with_title.tconst)


data = Data()
print(data.title_to_id('The Godfather'))
