import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june","all"]
days   = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"] 

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n')
    print('-'*40)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter your city \n').lower()
    while city not in cities:
            print("You've entered wrong city, please check you entered right city!!")
            city = input('Enter your city \n').lower()            
    print('-'*40)
    
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter  your month or enter all to choose all months \n').lower()
    while month not in months:
            print("You've entered wrong month, please check you entered right month!!")
            month = input('Enter  your month or enter all to choose all months months \n').lower()   
    print('-'*40)
    
    
    day = input('Enter your day or enter all to choose all days  \n').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in days:
            print("You've entered wrong day, please check you entered right day!!")
            day = input('Enter your day or enter all to choose all days \n').lower()

    
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
       # months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    # find the most common month 
    popular_month = df['month'].mode()[0]
    # display the most frequent Month 
    print('Most Frequent Month is:',months[popular_month - 1].title())

    # TO DO: display the most common day of week   
    # find the most common day of week  
    popular_day = df['day_of_week'].mode()[0]
    # display the most frequent day of week 
    print('Most Frequent Day of Week is:', popular_day)

    
    # TO DO: display the most common start hour
    # 1- convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    # 2-  extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
   
    # 3 -  find the most common hour 
    popular_hour = df['hour'].mode()[0]
    # 4-  display the most common start hour
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    tot_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    df['Total Duration'] = tot_duration
    days = tot_duration.days
    hours = tot_duration.seconds // 3600
    minutes = tot_duration.seconds % 3600 // 60
    seconds = tot_duration.days % 3600 % 60
    
    print("The Total Travel Time is: {}day(s), {}hours(s), {}minute(s), {}second(s)".format(days, hours, minutes, seconds))
    
    # TO DO: display mean travel time
    
    tot_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days = tot_duration.days
    hours = tot_duration.seconds // 3600
    minutes = tot_duration.seconds % 3600 // 60
    seconds = tot_duration.days % 3600 % 60    
    print("The Average Travel Time is: {}day(s), {}hours(s), {}minute(s), {}second(s)".format(days, hours, minutes, seconds))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular station and trip."""

    print('\nCalculating The Most Popular Station and Trip...\n')
    start_time = time.time()

    # Display most common start station 
    most_start_station = df['Start Station'].mode()[0]
    print("The Most Used Start Station is {}".format(most_start_station))
    
    # Display most common end station 
    most_end_station = df['End Station'].mode()[0]
    print("The Most Used End Station is {}".format(most_end_station))
    

    #Display the most common trip
    df['Trip'] = df["Start Station"] + "-" + df["End Station"]
    most_trip = df['Trip'].mode()[0]
    print("The Most Used Trip is {}".format(most_trip))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count     =   df['User Type'].value_counts()
    print("\n",user_type_count)
    
    
    try:
        # Display counts of gender
        gender_count    =   df['Gender'].value_counts()
        print('\nBike riders gender split: \n', gender_count)
    
    # Calculate earliest, most recent, and most common year of birth
        earliest_yob    =   (df['Birth Year'].fillna(0).astype('int64')).min()
        most_recent_yob =   (df['Birth Year'].fillna(0).astype('int64')).max()
        most_common_yob =   (df['Birth Year'].fillna(0).astype('int64')).mode()[0]
        
    # Display earliest, most recent, and most common year of birth
        print('\n Earliest birth year :  ',earliest_yob)
        print('\n Most recent birth year :  ',most_recent_yob)
        print('\n Most common birth year :  ',most_common_yob)
    # dealing with Washington
    except KeyError:
        print('This data is not available for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
   
    # setting counter for the rows 
    counter = 0

    # collecting user input
    choice = input('To View the next 5 rows of data in chuncks type: Yes \n').lower()

   # Validating user input
    while choice not in ['yes', 'no']:
        print('Invalid Choice!! , pleas enter yes or no')
        choice = input('To View the next 5 rows of data in chuncks type: Yes \n').lower()

    # action based on yes 
    while choice == 'yes':
        print(df.iloc[counter:counter+5])
        counter  = counter + 5
        choice   = input('Do you want to display 5 more rows? yes or no: ').lower()

   # action based on no
    if choice == 'no':
        print('\nExiting...')    
    

def main():
    while True:
        city, month, day = get_filters()
        print("The entered city is {}, and the enterd month is {}, and the entered day is {}".format(city, month, day).title())
        
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)      
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
    main()
	



