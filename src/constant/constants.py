CWUR_URL = 'https://cwur.org/2018-19.php'
BASE_URL = CWUR_URL.rpartition('/')[0]
PARSER = 'lxml'

CSV_HEADERS = ['World Rank', 'Institution Name', 'Location', 'Score', 'Domain']
# Directory level constants
OUTPUT_DIR_BASE = 'output'
SCRAPED_DATA_FILES = 'scrapped-data'
ANALYTICAL_DATA = 'analytical-data'

# File Names
UNIVERSITIES_LIST_FILE_NAME = 'ScrappedTop1000Universities.csv'
GRAPH_IMAGES = 'visual-graph'
# Web Response Codes
RESPONSE_OK = 200
