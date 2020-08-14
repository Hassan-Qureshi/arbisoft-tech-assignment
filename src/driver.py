
"""
This file is the entry point of the project
"""
from src.scrapper.Scrapper import Scrapper
from src.analytics.data_curation import DataAnalysis
import os

CWD = os.path.normpath(os.path.abspath(__file__) + os.sep + os.pardir)
os.chdir(CWD)
if __name__ == '__main__':
    # Part - 1 of the Task (Scrap the data)
    scrapper = Scrapper()
    scrapper.run_scrapper()
    # Part - 2 of Task (Perform some analysis)
    da = DataAnalysis()
    # Analysis - 1
    da.plot_total_universities()
    # Analysis - 2
    da.plot_average_ranking_universities()
