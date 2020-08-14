import os
import pandas as pd
import matplotlib.pyplot as plt
from src.constant import constants
from src.utility import manage_directories as dir_manager

CWD = os.path.normpath(os.path.normpath(os.path.abspath(__file__) + os.sep + os.pardir) + os.sep + os.pardir)
os.chdir(CWD)


class DataAnalysis:
    def __init__(self):
        # For reading csv file
        self.SCRAPPED_FILE_PATH = os.path.join(constants.OUTPUT_DIR_BASE, constants.SCRAPED_DATA_FILES,
                                               constants.UNIVERSITIES_LIST_FILE_NAME)

        self.UNIVERSITIES_TOTAL_COUNT_CSV_FILE = os.path.join(constants.OUTPUT_DIR_BASE,
                                                              constants.ANALYTICAL_DATA,
                                                              constants.RAW_DATA,
                                                              constants.UNIVERSITIES_TOTAL_COUNT_WRT_COUNTRY_FILE_NAME)
        self.UNIVERSITIES_TOTAL_COUNT_GRAPH_FILE = os.path.join(constants.OUTPUT_DIR_BASE,
                                                                constants.ANALYTICAL_DATA,
                                                                constants.GRAPH_IMAGES,
                                                                constants.UNIVERSITIES_TOTAL_COUNT_WRT_COUNTRY_GRAPH_FILE)

        self.UNIVERSITIES_AVERAGE_RANKING_CSV_FILE = os.path.join(constants.OUTPUT_DIR_BASE,
                                                                  constants.ANALYTICAL_DATA,
                                                                  constants.RAW_DATA,
                                                                  constants.UNIVERSITIES_AVERAGE_RANKING_WRT_COUNTRY_FILE_NAME)
        self.UNIVERSITIES_AVERAGE_RANKING_GRAPH_FILE = os.path.join(constants.OUTPUT_DIR_BASE,
                                                                    constants.ANALYTICAL_DATA,
                                                                    constants.GRAPH_IMAGES,
                                                                    constants.UNIVERSITIES_AVERAGE_RANKING_WRT_COUNTRY_GRAPH_FILE)

        # For saving plotted graphs
        OUTPUT_FILE_DIR_FOR_GRAPH = os.path.join(constants.OUTPUT_DIR_BASE, constants.ANALYTICAL_DATA,
                                                 constants.GRAPH_IMAGES)
        # For saving analytical data in csv format
        OUTPUT_FILE_DIR_FOR_RAW_DATA = os.path.join(constants.OUTPUT_DIR_BASE, constants.ANALYTICAL_DATA,
                                                    constants.RAW_DATA)

        dir_manager.create_dir_if_not(OUTPUT_FILE_DIR_FOR_GRAPH)
        dir_manager.create_dir_if_not(OUTPUT_FILE_DIR_FOR_RAW_DATA)

    @staticmethod
    def save_file(df: pd.DataFrame, complete_path: str):
        """
        Saves the file in csv format
        :param df: Dataframe whose data needs to be saved
        :param complete_path: Complete path in having file name and extension
        :return: None
        """
        print("Saving Analytical Data for Average Ranking of Universities at Location ==> '{}'".format(
            complete_path))
        df.to_csv(complete_path, encoding='utf-8', index=False)

    def read_csv(self):
        """
        Read scrapped data CSV file
        :return: dataframe
        """
        try:
            df = pd.read_csv(self.SCRAPPED_FILE_PATH)
            return df
        except Exception as e:

            print(e)

    def get_total_universities(self):
        """
        This method returns a dataframe having total count of universities in given country
        :return: dataframe with two columns Country and Total Universities
        """
        df = self.read_csv()
        total_uni_per_country = df.groupby(['Location'])['Institution Name'] \
            .count() \
            .reset_index() \
            .rename(columns={'Location': 'Country', 'Institution Name': 'Total Universities'})
        return total_uni_per_country

    def plot_total_universities(self):
        """
        This method saves data in csv format and plots after a transformation (curation) for graphical/visual analysis
        :return: None
        """
        total_uni_per_country = self.get_total_universities()
        self.save_file(total_uni_per_country, self.UNIVERSITIES_TOTAL_COUNT_CSV_FILE)
        plt.figure(figsize=(100, 30))
        plt.plot(total_uni_per_country["Country"], total_uni_per_country["Total Universities"]
                 , color='blue', label='Number of Universities in a Country', linewidth=2, markersize=22, marker='o'
                 )
        plt.xticks(fontsize=25, rotation=85);
        plt.grid(linewidth=3)
        plt.legend(fontsize=50);
        plt.suptitle('Country-wise Total Universities Count', fontsize=45)
        plt.xlabel('Countries', fontsize=35);
        plt.ylabel('Total Universities', fontsize=35);
        print("Generating and Saving Graph Image at Location ==> '{}'".format(self.UNIVERSITIES_TOTAL_COUNT_GRAPH_FILE))
        plt.savefig(self.UNIVERSITIES_TOTAL_COUNT_GRAPH_FILE, orientation='portrait', format='png',
                    transparent=False, bbox_inches=None, pad_inches=0.1)
        # plt.show()

    def get_average_ranking(self):
        """
        This method reads scrapped full dataset and apply transformation rule of taking average ranking per country.
        :return: Transformed Dataframe having country and average ranking of it's universities
        """
        df = self.read_csv()
        average_ranking = df.groupby(['Location'])['World Rank'] \
            .mean() \
            .sort_values(ascending=True) \
            .reset_index() \
            .rename(columns={'Location': 'Country', 'World Rank': 'Average Ranking'})
        return average_ranking

    def plot_average_ranking_universities(self):
        """
        This method saves data in csv format and plots after a transformation (curation) for graphical/visual analysis
        :return: None
        """
        average_ranking = self.get_average_ranking()
        self.save_file(average_ranking, self.UNIVERSITIES_AVERAGE_RANKING_CSV_FILE)

        plt.figure(figsize=(60, 30))
        plt.bar(average_ranking["Country"], average_ranking["Average Ranking"]
                , label='Average Ranking of Universities', linewidth=1, edgecolor='black')
        plt.xticks(fontsize=25, rotation=85);
        plt.grid(linewidth=3)
        plt.legend(fontsize=50);
        plt.suptitle('Country-wise Average Ranking of Universities', fontsize=45)
        plt.xlabel('Countries', fontsize=35);
        plt.ylabel('Average Ranking', fontsize=35);
        print("Generating and Saving Graph Image at Location ==> '{}'".format(self.UNIVERSITIES_AVERAGE_RANKING_GRAPH_FILE))

        plt.savefig(self.UNIVERSITIES_AVERAGE_RANKING_GRAPH_FILE, orientation='portrait', format='png',
                    transparent=False, bbox_inches=None, pad_inches=0.1)
        # plt.show()


if __name__ == '__main__':
    da = DataAnalysis()
    da.plot_total_universities()
    da.plot_average_ranking_universities()