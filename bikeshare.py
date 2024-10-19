import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city
    city = ''
    while city not in CITY_DATA:
        city = input("Please enter a city (chicago, new york city, washington): ").lower()
        if city not in CITY_DATA:
            print("Invalid input. Please try again.")

    # Get user input for month
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    while month not in months:
        month = input("Please enter a month (all, january, february, march, april, may, june): ").lower()
        if month not in months:
            print("Invalid input. Please try again.")

    # Get user input for day
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in days:
        day = input("Please enter a day (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ").lower()
        if day not in days:
            print("Invalid input. Please try again.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    # Filter by month
    if month != 'all':
        month_index = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Month'] == month_index]

    # Filter by day
    if day != 'all':
        df = df[df['Day of Week'] == day.title()]

    return df


def time_stats(df):
    """Displaying statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['Month'].mode()[0]
    print(f'Most common month: {["January", "February", "March", "April", "May", "June"][most_common_month - 1]}')

    # Display the most common day of week
    most_common_day = df['Day of Week'].mode()[0]
    print(f'Most common day of week: {most_common_day}')

    # Display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Hour'].mode()[0]
    print(f'Most common start hour: {most_common_hour}')

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f'Most commonly used start station: {most_common_start_station}')

    # Display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f'Most commonly used end station: {most_common_end_station}')

    # Display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    most_frequent_trip = df['Trip'].mode()[0]
    print(f'Most frequent combination of start station and end station trip: {most_frequent_trip}')

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def trip_duration_stats(df):
    """Display statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total travel time: {round(total_travel_time / 60, 2)} minutes')

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean travel time: {round(mean_travel_time / 60, 2)} minutes')

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print(user_type_counts)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print("Gender data not available.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print(f'Earliest year of birth: {int(earliest_year)}')
        print(f'Most recent year of birth: {int(recent_year)}')
        print(f'Most common year of birth: {int(most_common_year)}')
    else:
        print("Birth year data not available.")

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data in increments of 5 rows."""
    start_loc = 0
    view_data = input("Would you like to see the raw data? Enter 'yes' or 'no': ").lower()
    
    if view_data == 'yes':
        while start_loc < len(df):
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            if start_loc < len(df):
                more_data = input("Do you want to see 5 more rows? Enter 'yes' or 'no': ").lower()
                if more_data != 'yes':
                    break
            else:
                print("End of data.")
    elif view_data == 'no':
        pass
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)  # Call to display raw data

        restart = input('\nWould you like to restart? Enter yes or no: ').lower()
        while restart not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
            restart = input('\nWould you like to restart? Enter yes or no: ').lower()
        
        if restart != 'yes':
            break


if __name__ == "__main__":
    main()
