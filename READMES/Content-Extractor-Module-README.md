Goal
-
Extracting the important content bits from the HTML code we saved for each article URL

Input
-
Gets the HTML Code from the column html for each URL in table articles where column ```processed_content_extractor```=```false```

Output
-
Updates(Saves) the following fields in the articles table

*	```domain_name```,
*	```url```,
*	```text```,
*	```keywords(list)```,
*	```authors(list)```,
*	```publish_date```,
*	```tags(list)```,
*	```summary```,
*	```links(list)```,
*	```parse_time```

Technical Implementation
-
Using Newspaper3k Module to parse the HTML and obtain the required fields. Though it doesn't support raw HTML parsing by default but passing the raw HTML to the download method of an article object is a good work around.

[Original Issue for reference](https://github.com/WorldBrain/crawler/issues/4)