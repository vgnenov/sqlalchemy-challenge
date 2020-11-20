# Surfs Up!

![Screenshot](Screenshots/surf.jpg "Screenshot")

# Purpose
Analyze the climate of Hawaii to determine the best location for a vacation stay.

## Process
Utilizing Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database.  The following analysis will be completed using SQLAlchemy ORM queries, Pandas and Matplotlib.

### Precipitation Analysis
- Design a query to retrieve the last 12 months of precipitation data
- Select only the date and prcp values
- Load the query results into a Pandas DataFrame and set the index to the date column
- Sort the DataFrame values by date
- Plot the results using the DataFrame plot method