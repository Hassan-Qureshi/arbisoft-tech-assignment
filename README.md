## Project Setup Instructions
- Install, Create and Activate Virtual Environment

	`$ pip install virtualenv`
	
	`$ virtualenv <ENV-NAME>`
	
	`$ ./<ENV-NAME>/Scripts/activate`

- Install dependencies from requirements.txt file

	`$ pip install -r requirements.txt`

- The working directory should be `src`

- The project is fully dynamic the directories, file names, URLs etc are stored in separate file which can be reference from any where inside the project.

<hr>

### Task Explanation
The task is divided into two sub-modules
1. Scraping Module
2. Data Analytics Module
#### Scraping Module
My approach was to scrap the first main page which contains list of all the universities and then traverse the universities list one by one, get `href` of respective university, and get the <u>University Domain</u> from second page which was <b> bonus part.</b><br>
The module is located at `src.scrapper.Scrapper.py` <br>
The scrapped data will be at location `output/scrapped-data/`
#### Data Analytics Module
I used two transformations in order to present the data or information in better way. <br>
<ol>
<li>Total count of universities for each country</li>
<li>Country-wise average ranking of universities</li>
</ol>

The data (for both transformation) always saves in `CSV` file format and located at `src/output/analytical-data/raw-curated-data/`.<br>
I've presented the data in graphical format using `matplotlib` library. The resultant graphs can be viewed at location `src/output/visutal-graph/` which was <b> bonus task</b>. 
