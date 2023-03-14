import time
import pandas as pd
CITY_DATA = { 'chic': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'wgt': 'washington.csv' }

    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # 1- check for input validation for city
    # ask the user to input city (chicago (chic), new york city (nyc), washington(wgt)
    while True:
        city = input("please, pick a city to analyze:(chic) for chicago or (nyc) for new_york_city or (wgt) for washington:\n").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Opps!! Invalid Input...")
        
        
    # ask the user to input month (jan, feb, ... , jun, all)
    months = ["jan", "feb", "mar", "apr", "may", "jun", "all"]
    while True:
        month = input("please, pick a month (jan, feb, mar, apr, may, jun) to filter data month-wise or type (all) for not filtering:\n").lower()
        if month in months:
            break
        else:
            print("Opps!! incorrect input...")
    
    # ask the user to input day of week (sat , sun, mon ... fri, all)
    days = ["sat", "sun", "mon", "tue", "wed", "thu", "fri", "all"]
    while True:
        day = input("please, pick day of week(sat, sun, mon, tue, wed, thu, fri)to filter or(all) for not filtering:\n").lower()
        if day in days:
            break
        else:
            print("Oh no! invalid input...")

    
    return city, month, day


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
    # data file as a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # converting (Start Time) column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'].str.startswith(month.title())]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.startswith(day.title())]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    most_common_month = df['month'].mode()[0]
    print("Most common month is ", most_common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day is ', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour is ', most_common_hour, 'hours')

    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is', most_common_start) 

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('The most commonly used end station is', most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = 'from' + df['Start Station'] +" to "+ df['End Station'].mode()[0]
    print('Most frequent combination of start station and end station trip', common_trip)

    
    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('Total travel time is', total_trip_duration)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is', mean_travel_time)
    
    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    df['Birth Year'] = df['Birth Year'].astype(int)
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print('Here are users types:\n', user_types)
    # TO DO: Display counts of gender 
    # I used try / except to avoid any difference between cities data 
    try:
        print("Gender is\n", df['Gender'].value_counts())
         # TO DO: Display earliest, most recent, and most common year of birth
            
        print('Earliest year of birth is', df['Birth Year'].min().astype(int))
        print('Most recent of birth is', df['Birth Year'].max().astype(int))
        print('Most common year of birth is', df['Birth Year'].mode()[0].astype(int))    
        
    except:
        print('No filter with gender allowed in Washington city!')

    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)

                

def ask_more_data(df):
    more_data = input("Would you like to view 5 rows of data? Enter yes or no? ").lower()
    index = 0
    pd.set_option('display.max_columns',200)
    while True:
        if more_data == 'no':
            break
        elif more_data == 'yes':
            print(df.iloc[index:index+5])
            more_data = input("Would you like to view 5 more rows of data? Enter yes or no? ").lower()
            index += 5
        else:
            more_data = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
        
    return df
                

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ask_more_data(df)
        
        restart = input('\nWould you like to restart your journey? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()