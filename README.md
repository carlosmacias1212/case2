# case2

# Data Set:
The data is read in from a csv file. The data describes multiple characteristics of individual loans including job titles, employment length, loan amount, etc. Overall the data set did not seem to be fully normalized which may not be an issue if it is read only. There were some records that contained null values which could negatively affect data queries. Another issue when it comes to reading in the csv file into a database is that for the technologies that I used it took a long time to load in the data and not all of it was able to be inserted into the table. 

# Feature Set:
The feature set created was related to the 5 visualizations and the data that would be coming in and out of those functions given some parts of the data displayed in each individual graph/chart.

# Interest Rate Model

The interest rate model created utilized 2 algorithms to calculate the interest rate for an individual. The first algorithm would take into account the verification status of the individuals annual income. Annual income that is more thoroughly verified receives less additional interest. The second algorithm considered the amount of time the individual has been employed at their current job. Longer employment times receive less interest. Some data cleansing that would need to be considered would be making sure that NULL values are not being considered.

# Improvments
The data from csv could benefit from some normalization in order to allocate the necessery attributes for this interest rate model into one location. In terms of the model I also think that more time would allow me to come up with a more mathematical method for calculating interest that takes into account more attributes of the data set. During my implementation I assumed that the data would already be cleansed in order to not factor that into my model and feature set. 
