### Goal of this module:

A module that indexes a postgreSQL DB with Elastic-Search. It will also be responsible for searches against the ES documents.


### Input:
Search phrase: `/api/search?q=<search-phrase>` 

### Output: 
JSON response containing the most relevant articles in elastic search that match the search keywords.
Relevance is computed in the following order:
- Title
- Keywords
- tags
- NLP (Automatic Analysis done by Newspaper3k)
- Summary (Summary delivered by the page itself)
- authors
- text

### Technical Implementation:
#### Step 1: Initial index of postgreSQL DB in ES
A django `python manage.py reindex` command will be implemented for reindexing the DB


#### Step 2: Setup Periodic task that will sync the DBS

#### Step 3: Expose an /api/search/ end-point in the django app that makes use of ES MODULE
A search api will be exposed on `/api/search?q=<search-phrase>` 
If `q` is not supplied, a `match_all` query will be used
