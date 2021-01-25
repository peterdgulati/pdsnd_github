import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
      city = input("\nEnter name of the city would you like to analyze? chicago, new york city or washington\n")
      city = city.lower()
      if city not in ('chicago', 'new york city', 'washington'):
        print("Please use one of the city mentioned above.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nEnter name of the month would you like to filter by? january, february, march, april, may, june or type 'all' to apply no month filter\n")
      month = month.lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Please use month from january to june or use all if not sure.")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nEnter name of the day would you like to filter by? monday, tuesday, wednesday, thursday, friday, saturday, sunday or type 'all' to apply no month filter\n")
      day = day.lower()
      if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print("Please use day of the week from above or use all if not sure!.")
        continue
      else:
        break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
      # use the index of the months list to get the corresponding int
      months = ['january', 'february', 'march', 'april', 'may', 'june']
      month = months.index(month) + 1

      # filter by month to create the new dataframe
      df = df[df['month'] == month]

      # filter by day of week if applicable
      if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month is: ",popular_month, "\n")

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of week  is: ", popular_day, "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is: ", popular_hour , "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most common start station is: ", popular_start_station , "\n")

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ", popular_end_station , "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['Combine station'] = df['Start Station'] + ' and ' + df['End Station']
    Combine_station = df['Combine station'].mode()[0]
    print(" The most frequent combination of start station and end station trip: ", Combine_station,"\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Trip_Duration = df['Trip Duration'].sum()
    print("The total travel time is:", Trip_Duration, "\n")

    # TO DO: display mean travel time
    Trip_Duration = df['Trip Duration'].mean()
    print("The mean travel time is:", Trip_Duration, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(" The counts of user types: ", user_types, "\n")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
      gender_types = df['Gender'].value_counts()
      print(" The counts of gender: ", gender_types, "\n")
    else:
      print("There is no data available to be displayed for Gender \n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
      earliest = int(df['Birth Year'].min())
      print('The earliest year of birth: ', earliest, "\n")

      most_recent = int(df['Birth Year'].max())
      print('The most recent year of birth: ', most_recent, "\n")

      most_common = int(df['Birth Year'].mode()[0])
      print('The most common year of birth: ', most_common, "\n")

    else:
      print("There is no data available to be displayed for Birth Year \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    x = 1
    while True:
     raw = input('\nWould you like to see some raw data? Enter yes or no.\n')
     if raw.lower() == 'yes':
        print(df[x:x+5])
        x = x+5
     else:
        break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
