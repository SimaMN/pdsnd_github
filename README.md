# US BikeShare Data Exploration Project

## Overview

This project uses Python to explore bike share data from three major cities in the United States—Chicago, New York City, and Washington. The goal is to write code that imports data and computes descriptive statistics to answer questions about bike share usage patterns. Additionally, the project includes an interactive terminal-based script that allows users to filter and explore the data interactively.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Datasets](#datasets)
- [Statistics Computed](#statistics-computed)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To set up the project locally, ensure you have the following software:

1. Python 3, NumPy, and pandas installed (preferably using Anaconda).
2. A text editor like [Sublime](https://www.sublimetext.com) or [Atom](https://atom.io).
3. A terminal application (Terminal on Mac/Linux or Git Bash on Windows).

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/username/bikeshare-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd bikeshare-analysis
   ```
3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The `bikeshare.py` script creates an interactive experience in the terminal, allowing users to filter data by city, month, or day of the week. The script then computes and displays various statistics based on the filtered data. To run the script:

```bash
python bikeshare.py
```

### User Input

The script prompts users with the following questions:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If filtering by month) Which month - January, February, March, April, May, or June?
4. (If filtering by day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

Based on the answers, the script displays relevant statistics. Users also have the option to view raw data 5 rows at a time.

## Features

- **Interactive Filtering**: Users can filter data by city, month, and day.
- **Descriptive Statistics**: Provides insights into popular travel times, stations, trip durations, and user demographics.
- **Raw Data Display**: Users can choose to view raw data in increments of 5 rows.

## Datasets

The datasets used in this project contain randomly selected data for the first six months of 2017 from the following cities:
- **Chicago**: `chicago.csv`
- **New York City**: `new_york_city.csv`
- **Washington**: `washington.csv`

These files contain the following columns:
- **Start Time**: The start time of the trip.
- **End Time**: The end time of the trip.
- **Trip Duration**: The duration of the trip in seconds.
- **Start Station**: The station where the trip started.
- **End Station**: The station where the trip ended.
- **User Type**: The type of user (Subscriber or Customer).

Additional columns for Chicago and New York City:
- **Gender**
- **Birth Year**

## Statistics Computed

The script computes the following statistics:

1. **Popular Times of Travel**:
   - Most common month
   - Most common day of the week
   - Most common hour of the day
2. **Popular Stations and Trips**:
   - Most common start station
   - Most common end station
   - Most frequent trip from start to end
3. **Trip Duration**:
   - Total travel time
   - Average travel time
4. **User Information**:
   - Counts of each user type
   - Counts of each gender (NYC and Chicago only)
   - Earliest, most recent, and most common year of birth (NYC and Chicago only)

## Tips to Improve Your Code

1. **Format your numbers related to time using round()(opens in a new tab) function. It does not make much sense to use decimals like 7.55738383 with seconds/minutes. Instead it should be formatted to 7.6 seconds.**

2. **User inputs should be made case insensitive, which means the input should accept the string of "Chicago" and its case variants, such as "chicago", "CHICAGO", or "cHicAgo".**

3. **You should also implement error handlings so your program does not throw any errors due to invalid inputs. For example, if the user enters "Los Angeles" for the city, the error handling should reject the user input and avoid breaking the codes.**

4. **To further develop your skills in python, you can practice with HackerRank(opens in a new tab), which challenges you with increasingly difficult problems.**

