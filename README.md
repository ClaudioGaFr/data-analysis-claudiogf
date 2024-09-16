# data-analysis-claudiogf
Title: Exploratory Data Analysis of Parking Tickets: Trends, Infractions, and Insights (2023-2024)

This project consists of an exploratory data analysis based on parking ticket data collected for the years 2023 and 2024, providing detailed information on parking violation locations, dates, bylaws and sections violated, ticket status, and infractions types.

Dataset used: Parking-tickets_2023, Parking-tickets_2024:

Block: Number of the block where the violation happened
Street: The street on which the violation happened
EntryDate: Date when the ticket was issued
Bylaw: Number of the law and/or regulation broken
Section: The exact section of the regulation broken
Status: Status of the ticket, such as paid/unpaid
InfractionText: A text describing the type of violation.
Year: When the ticket was issued, here being 2023.
BI_ID: Each ticket has an identifier number

1.Data Collection:

A parking ticket issued for the years 2023 and 2024 constitutes the dataset in this project. Each dataset has data about the violation of parking, starting with the block and street where the violation occurred, date of issuance, bylaw and section violated, status of the ticket, and description of violation.

The source is local parking enforcement records. The data are in CSV format. The data was given for the years 2023 and 2024 as separate data sets.

Data file formats:

parking-tickets_2023.csv: It includes all data about parking tickets from Year 2023.
parking-tickets_2024.csv: It is a comma-separated values file, parking tickets data starting from the year 2024.

<img width="710" alt="Screenshot 2024-09-15 at 18 43 54" src="https://github.com/user-attachments/assets/148a9c67-b7f8-4479-8b3a-b7023e1c9c96">

Combination of both years

<img width="633" alt="Screenshot 2024-09-15 at 18 44 46" src="https://github.com/user-attachments/assets/7ba323af-9a60-4bf2-b131-ef3987ab6b1d">

Descriptive analysis based on the dataset combined:
Once the data has been loaded, the next thing to do is get the statistical summary of the numerical variables of the dataset. That will include, but not be limited to, information like:

Average
Median
Standard deviation
Minimum and maximum value
Quartiles
It provides an initial impression of the distribution of data in the dataset. It also highlights unusual values​​ or inconsistencies in the data. In Python, descriptive statistics for variables can be performed using the method

<img width="473" alt="Screenshot 2024-09-15 at 18 50 06" src="https://github.com/user-attachments/assets/25f4305f-86e4-4029-9032-57835466c64e">

On the terminal results:

<img width="550" alt="Screenshot 2024-09-15 at 18 51 09" src="https://github.com/user-attachments/assets/2e278605-ca86-43fe-b7cb-90a045133137">

Data Visualization: 

Temporal distribution of violations:

The bar chart below examines the distribution of violations by month and years. You can find seasonal patterns-for example, whether there are particular months where more or fewer parking tickets were issued.

Objective: Find out monthly trends and compare data for the year 2023 and 2024.
Approach: seaborn.countplot() produces a bar chart that shows the number of violations occurring each month of the years 2023 and 2024 separately.

<img width="520" alt="Screenshot 2024-09-15 at 19 00 06" src="https://github.com/user-attachments/assets/36a358b8-a7dd-4dea-b730-dbb8fd6c6049">

Results: The graph will show peaks in certain months or seasons of the year regarding ticket issuance. For example, you can observe that during the summer months, more tickets are given due to more traffic, and during winter months, fewer tickets are given.

View Violations by Street:

Here, we can visualize streets that have issued the highest number of parking violations. This will be useful in finding areas where illegal parking or violation of rules is more common.

Objective: Determine what streets have the most parking tickets.
Method: Use seaborn.barplot() to create a bar chart of the top 10 streets with the most violations.

<img width="526" alt="Screenshot 2024-09-15 at 19 02 27" src="https://github.com/user-attachments/assets/60a92709-2f1c-4f3c-8a83-3ba3bdd102f1">

Outputs: This plot allows us to find places within city boundaries that have the highest number of violations; this can be used for practical purposes, like urban planning or resource allocation for traffic supervision.

Viewing most common violations:

In this step, a visualization of the most common types of violations is made. This means that you are able to see what kind of parking violations are more common and might need the highest priority from authorities.

Objective: Determine what are the most common types of violations.
Method: The bar chart represents the InfractionText column for the top 10 common types of infractions.

<img width="473" alt="Screenshot 2024-09-15 at 19 04 23" src="https://github.com/user-attachments/assets/caed15d7-2dde-442a-84a2-f83be66a85ce">

All this analysis based on the dataset already combined, and also cleaned, this is the pyhton code that i use for the data visualization:

<img width="644" alt="Screenshot 2024-09-15 at 18 57 39" src="https://github.com/user-attachments/assets/4f787c7a-23d2-4d7d-814f-4a47080e91cf">

Numeric Variables Heatmap:

In the presence of numeric variables in the data set, a correlation matrix is to be created as a heatmap that would help in understanding the presence of any strong correlation between the numeric variables.

Objective: To determine the correlation between the numeric variables Block and Year.
Method: seaborn.heatmap() is used to visualize the correlation between numerical variables.

<img width="472" alt="Screenshot 2024-09-15 at 19 08 17" src="https://github.com/user-attachments/assets/36f8986f-bb15-472b-88eb-157850cb1443">

Results: The following heatmap shows whether there is a strong relationship between numerical variables: In such a case, if there was an overall greater pattern of violations in blocks or for specific years, it would have appeared in this heat map.

Detailed heatmap

<img width="481" alt="Screenshot 2024-09-15 at 19 16 39" src="https://github.com/user-attachments/assets/4b713d3a-f306-4e89-8e96-0f4bcefa31b3">

Explanations of the Variables:

Block: Block number in which the parking violation took place.
Year: The year the ticket was issued; either 2023 or 2024.
Month: This column is derived from the EntryDate column - the month that this ticket was issued.
Status_Numeric: This numeric variable is derived from the status of the ticket. Examples are 1 for "IS" presumably meaning "paid" or "issued," and 0 for other statuses.
Infraction_Count_Street: Count of infractions per street, sum of the number of tickets issued on each street.
Bylaw: Number of the by-law violated. For this example, it is treated as numeric.
What this heat map is showing?
Block: Where the violation took place
Year and Month: Temporals of the violations.
Status: Whether a violation was paid or it is in another state.
Infraction Count per Street: This would allow you to see if there are streets where infractions occur more than others.

Predicted Insights:
Strong Correlations: In general, the correlations between some variables can occur, such as Month vs. Infraction_Count_Street, due to a typical month which would normally receive more tickets in an area.
Weak or No Correlations: In cases that the correlation value near 0 between two variables, this suggests that there is no significant relationship existing between them.

On this step, the data is following visualizations which are select that can be used to get different outlooks on parking violations. This includes visualizations of:

Monthly distribution of tickets.
Top violating streets.
The most common violations.
Numerical variable correlations include block and year.
These visualizations will provide an efficient and powerful visual comprehension of data that helps you to spot trends-which would be important for future decisions in either urban planning or parking monitoring.

Insigths and findings

Temporal Trends:

From this analysis in the bar chart, it was observed that parking violations did not occur monthly with uniform distribution. For instance, other months, probably summer months, had a higher conglomeration of tickets. It may be that during those parts of the year, enforcement becomes more necessary because of events, holidays, or improved weather conditions.
Geographic Trends:

The top streets with the most parking violations showed that the infractions are issued in a very geographical manner. Other streets had fewer violations than others, and this could be influenced by factors such as high traffic areas, adjacency to commercial zones, or even lack of parking facilities.
Indeed, the same block number analysis showed that there were relatively consistent trends across the blocks studied, little time-shift between 2023 and 2024.
Top Violations:

The bar chart for the most prevalent violations showed that many of the parking violations were repeated offenses due to either not paying enough in the various parking meters or failing to stay within the time limits. This could be improved with better signage, clearer rules, or more enforcement in those spots.
No Strong Correlations:

The heat map for the correlations indicated very weak correlations between most numeric variables, suggesting that violations are somewhat evenly distributed across blocks and years with no real patterns to particular streets or time segments. This would thus propose that parking behavior across the years of this dataset is somewhat consistent year over year and similarly consistent from one area of the city to another.

Conclusion

From this exploratory data analysis of parking tickets in detail for the years 2023 and 2024, we can infer that:

Time-Based Patterns:

There is a definite time-based trend in parking violations. There are certain months that are particularly infamous in terms of the number of infractions. A finding like this could help city officials plan enforcement strategies whereby patrols are increased during high periods or parking restrictions are varied during months that would see heavy traffic.

Geographical Distribution:

Not all violations occur uniformly throughout the city: some streets or blocks have far more parking violations than others, a function of a flawed enforcement effort or perhaps parking rules that could be altered. Or this might simply show the lack of any sort of parking infrastructure in those zones.

Type of Violations Consistent:

Time limit and parking meter infractions are some of the types which top this data set. Being in a position to minimize such frequent infractions by way of better signage, clear rules, or more efficient enforcement will lower the number of overall tickets distributed.
Uncorrelated Key Variables

This correlation analysis suggests that variables such as Block and Year are poorly related-that is, parking violations are spread out rather uniformly across the city and time periods with no large geographic and temporal trends. Such a finding would indicate that infractions are more likely to be driven by situational factors than large-scale changes across time and location.

Tools used on pyhton:

1. Pandas:
Pandas were greatly utilized in loading, cleaning, and manipulating data. The library allowed flexible and efficient data structures called DataFrames to work with large volumes of data.
Key Pandas functions and techniques:
pd.read_csv(): To load the CSV files with parking ticket data for the year 2023 and 2024.
DataFrame.describe(): To generate descriptive statistics for the dataset.
groupby() and transform(): Used in the calculation of infractions on a street.
apply(): To change categorical data like Status into numeric format for analysis.

2. Matplotlib:
The Matplotlib library was used in creating various forms of visualizations, including bar charts and histograms, which could represent important trends within the data more succinctly.
Techniques used:
plt.plot(), plt.bar(), and plt.show(): These were employed to develop line plots and bar charts for displaying the visual representation of data.
plt.title(), plt.xlabel(), and plt.ylabel(): These functions were called to give a name to a chart and the axes for better readability and interpretation.

3. Seaborn:
Seaborn is relied on to provide more developed visualizations, especially in the development of detailed and elegant-looking charts and heatmaps.
Methods applied:
ns.heatmap(): To plot heatmaps of correlations between numeric variables.
ns.countplot(): Plot bar charts of the number of parking violations by month and year, so time-based trends would be easy to spot.
ns.barplot(): For top 10 streets by number of tickets and top 10 infractions by number of tickets issued.
