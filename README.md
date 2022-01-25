# Vacation_Weather_w_SQLAlchemy
This project aims to analyze weather data in Hawaii by utilizing SQLAlchemy ORM queries, Pandas, and Matplotlib.

We begin by loading in a SQL Database and then begin to query it using a python interface. Loading the desired data into a 
Pandas dataframe then streamlines the process.

From this the following is created:
- rainfall in inches vs time bar graph
- the total number of weather stations and the top ten weather stations
- the average, maximum, minimum, and number of observations per station
- a bar chart with number of observations per time for the top ten stations

The next part of the project involves utilizing flask in order to return jsons of desired data to the user. More specifically, precipitation, a list of stations,
the total number of observations for a specified station, and the min/average/min temperatures of a given date range. 

To do so, the following is done:
- return all available routes 
- define routes to be used by the user with specified arguements to be given as inputs
- convert returned data into a dictionary, then into a json object
- print to the local console using flask

The final portions of the project comes in analyzing the differences in the weather data between the months of June and December, followed by looking at a desired
date range with the goal of estimating the weather for the following year. First an unpaired t-test is used to compare the means of the two months. Second a box and whisker plot is used to showcase the quartiles, min, max, mean, and outliers of the a desired date range. This determines how the weather was like the previous year
when planning a potential trip for next year. 

