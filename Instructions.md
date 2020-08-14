<h3>Project Setup Instructions</h3>
- Install, Create and Activate Virtual Environment

	`$ pip install virtualenv`
	
	`$ virtualenv <ENV-NAME>`
	
	`$ ./<ENV-NAME>/Scripts/activate`

- Install dependencies from requirements.txt file

	`$ pip install -r requirements.txt`

- The working directory should be `src`

<hr>

<h3>Task Explanation</h3>
The task is divided into two sub-modules
1. Scraping Module
2. Data Analytics Module
<h4>Scraping Module</h4>
My approach was to scrap the first main page which contains list of all the universities and then traverse the universities list one by one, get `href` of respective university, and get the <u>University Domain</u> which was <b> bonus part.</b><br>
The Module is located at `src.scrapper.Scrapper.py`
<h4>Data Analytics Module</h4>
I used two transformations in order to present the data or information in better way. <br>
<ol>
<li>Total count of universities for each country</li>
<li>Country-wise average ranking of universities</li>
</ol>

The data (for both transformation) always saves in `CSV` file format and located at `src/output/analytical-data/raw-curated-data/`.<br>
I've presented the data in graphical format using `matplotlib` library. The resultant graphs can be viewed at location `src/output/visutal-graph/` which was <b> bonus task</b>. 
