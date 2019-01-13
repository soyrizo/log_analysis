# Log Analysis Reporting Tool
The log analysis reporting tool is used for running against the 'news' database provided [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). There are a pre-defined set of questions to be answered.

# Usage
Prerequisites: ensure 'news' database is installed and psql has the appropriate user and permissions to execute the python script.

`python3 log_analysis_reporting_tool.py`

# Questions
The tool answers three questions listed below.
  1) What are the most popular three articles of all time?
  2) Who are the most popular article authors of all time?
  3) On which days did more than 1% of requests lead to errors?

# Answers (Output)
See [output](output.txt)

# License
Log Analysis Reporting Tool is released under the [MIT License](https://choosealicense.com/licenses/mit/).
