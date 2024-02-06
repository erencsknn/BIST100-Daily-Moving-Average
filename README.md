# BIST100 Daily Moving Average

## Description

This project is created using Python to process daily stock market data and visualize closing prices, moving averages, and daily returns.

## Used Libraries

- pandas
- numpy
- matplotlib

## Data Source

The project retrieves daily stock market data from a CSV file named 'daily.csv'.

## Data Processing

Data processing steps are as follows:

1. Data is read from the CSV file.
2. Zero values in the data are replaced with NaN.
3. NaN values are filled using linear interpolation.
4. Moving Average (MA) calculations are performed: 20-day MA and 50-day MA.
5. Daily return calculations are made and added to the data.

## Visualization

The project visualizes stock closing prices, 20-day, and 50-day moving averages on a line chart. Additionally, labels on the x-axis are customized to mark specific dates.

## How to Use

1. Download or clone the project files.
2. Add the 'daily.csv' file to the project's main folder.
3. Install the required libraries: pandas, numpy, and matplotlib.
4. Run the project file.
5. Use `plt.show()` command to display the chart.

## Example Output

When the project is run, it will display a chart showing closing prices along with 20-day and 50-day moving averages.
