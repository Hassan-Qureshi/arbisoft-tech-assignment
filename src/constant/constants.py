CWUR_URL = 'https://cwur.org/2018-19.php'
BASE_URL = CWUR_URL.rpartition('/')[0]
PARSER = 'lxml'

CSV_HEADERS = ['World Rank', 'Institution Name', 'Location', 'Score', 'Domain']
# Directory level constants
OUTPUT_DIR_BASE = 'output'
SCRAPED_DATA_FILES = 'scrapped-data'
ANALYTICAL_DATA = 'analytical-data'
GRAPH_IMAGES = 'visual-graph'
RAW_DATA = 'raw-curated-data'
# File Names
UNIVERSITIES_LIST_FILE_NAME = 'ScrappedTop1000Universities.csv'

UNIVERSITIES_TOTAL_COUNT_WRT_COUNTRY_FILE_NAME = 'UniversitiesCountForEachCountry.csv'
UNIVERSITIES_TOTAL_COUNT_WRT_COUNTRY_GRAPH_FILE = 'UniversitiesCountForEachCountry.png'

UNIVERSITIES_AVERAGE_RANKING_WRT_COUNTRY_FILE_NAME = 'UniversitiesAvgerageRankingForEachCountry.csv'
UNIVERSITIES_AVERAGE_RANKING_WRT_COUNTRY_GRAPH_FILE = 'UniversitiesAvgerageRankingForEachCountry.png'

# Web Response Codes
RESPONSE_OK = 200
