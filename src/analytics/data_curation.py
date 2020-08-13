import os
import pandas as pd
import matplotlib.pyplot as plt
from src.constant import constants

CWD = os.path.normpath(os.path.normpath(os.path.abspath(__file__) + os.sep + os.pardir) + os.sep + os.pardir)
os.chdir(CWD)


OUTPUT_FILE_DIR = os.path.join(constants.OUTPUT_DIR_BASE, constants.SCRAPED_DATA_FILES)
SCRAPPED_FILE_NAME = os.path.join(OUTPUT_FILE_DIR, constants.UNIVERSITIES_LIST_FILE_NAME)
df = pd.read_csv(SCRAPPED_FILE_NAME)

total_uni_per_country = df.groupby(['Location'])['Institution Name'] \
                          .count() \
                          .reset_index() \
                          .rename(columns={'Location':'Country', 'Institution Name':'Total Universities'})
plt.figure(figsize=(100,30))
plt.plot(total_uni_per_country["Country"], total_uni_per_country["Total Universities"]
        ,color='blue', label='Number of Universities in a Country', linewidth=2, markersize=22, marker='o'
        )
plt.xticks(fontsize=25, rotation=85);
plt.grid(linewidth=3)
plt.legend(fontsize=50);
plt.suptitle('Country-wise Total Universities Count', fontsize=45)
plt.xlabel('Countries', fontsize=35);
plt.ylabel('Total Universities', fontsize=35);
plt.savefig('total-universities-count.png', orientation='portrait', format='png',
        transparent=False, bbox_inches=None, pad_inches=0.1)
# plt.show()


# =============================

average_ranking = df.groupby(['Location'])['World Rank'] \
                    .mean() \
                    .sort_values(ascending=True) \
                    .reset_index() \
                    .rename(columns={'Location':'Country', 'World Rank':'Average Ranking'})

plt.figure(figsize=(60,30))
plt.bar(average_ranking["Country"], average_ranking["Average Ranking"]
        , label='Average Ranking of Universities',linewidth=1, edgecolor='black')
plt.xticks(fontsize=25, rotation=85);
plt.grid(linewidth=3)
plt.legend(fontsize=50);
plt.suptitle('Country-wise Average Ranking of Universities', fontsize=45)
plt.xlabel('Countries', fontsize=35);
plt.ylabel('Average Ranking', fontsize=35);
plt.savefig('average-ranking.png', orientation='portrait', format='png',
        transparent=False, bbox_inches=None, pad_inches=0.1)
# plt.show()