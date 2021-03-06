import pandas as pd
import time


class Data:

    def __init__(self):
        print('Reading from the csv-file..')
        t1 = time.time()
        self.df = pd.read_csv(r'C:\Users\menes\Downloads\data.tsv', sep='\t',
                              dtype={'tconst': 'string', 'titleType': 'string', 'primaryTitle': 'string',
                                     'originalTitle': 'string', 'startYear': 'string'},
                              usecols=['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'startYear',
                                       'genres'])
        self.df.originalTitle = self.df.originalTitle.str.upper()
        self.df.titleType = self.df.titleType.str.upper()
        # self.df = pd.read_csv(r'data.tsv', sep='\t',
        #                       dtype={'tconst': 'string',
        #                              'originalTitle': 'string', 'startYear': 'string'},
        #                       usecols=['tconst', 'originalTitle', 'startYear',
        #                                'genres'])
        t2 = time.time()
        print('reading time is: ', t2 - t1, '\n')

    def title_to_id(self, title, content_type, year):
        """
        :param content_type:
        :param year:
        :param title: original title of a work (exact)
        :return: a set of imdb-id's of all works with exactly the same name
        """
        rows_with_title = self.df[self.df.originalTitle == title]
        if content_type is not None:
            rows_with_title = rows_with_title[rows_with_title.titleType == content_type]
        if year is not None:
            rows_with_title = rows_with_title[rows_with_title.startYear == year]
        return set(rows_with_title.tconst)

    def get_extended_names(self):
        print('\nZipping the titles and the years..')
        t1 = time.time()
        zipped = zip(self.df.originalTitle, self.df.startYear)
        print('zipping took: ', time.time() - t1)
        return zipped

# data = Data()
# print(data.title_to_id('The Godfather'))
