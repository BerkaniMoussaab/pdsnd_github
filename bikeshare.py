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
         city - name of the city to analyze
         month - name of the month to filter by, or "all" to apply no month filter
         day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york','washington']
    city=input("what city new york,washington or chicago ? \n ").lower()
    while city not in cities  :
        city=input("choose a city new york,washington or chicago ? \n").lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('please enter the month do you want to filter with \n').lower()
    listOfMonths= ['january','february','march','april','juin','july','august','september','october','november','december','all']  
    while month not in listOfMonths:
        month=input('please enter the month do you want to filter with \n').lower()
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('please give the day (all, monday, tuesday, ... sunday) \n').lower()
    Days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    while day not in Days:
        day=input('please give the day (all, monday, tuesday, ... sunday)\n').lower()
        


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
    if city=='chicago':
        city_data='chicago.csv'
    if city=='new york':
        city_data='new_york_city.csv'
    if city=='washington':
        city_data='washington.csv'
    df = pd.read_csv(city_data)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
       months = ['january','february','march','april','juin','july','august','september','october','november','december'] 
       month = months.index(month) + 1
       df = df[df['month'] == month]
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]
      

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('the most popular month is {}'.format(popular_month))


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('the most popular day is {}'.format(popular_day))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most popular start hour is {}'.format(popular_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['End Station'].mode()[0]

    print('Most Popular Start station:', popular_start_station)
    


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    print('Most Popular end station:', popular_end_station )


    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station trip',df.groupby(['Start Station','End Station','Trip Duration']).size().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Difference'] = df['End Time'].dt.hour-df['Start Time'].dt.hour 
    # TO DO: display total travel time
    Total = df['Difference'].sum()
    print (Total)

    
    # TO DO: display mean travel time
    
    print('the mean timee is',df['Difference'].mean())
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User type count',df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('user gender count',df['Gender'].value_counts())
    elif 'Gender' not in df.columns:
        print("sorry we don't have the Gender in the data base for the city of washington")
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
       print('our oldest user is born on',min(df['Birth Year']))
       print('our youngest user is born on',max(df['Birth Year']))
       print('most commun year of birth is',df['Birth Year'].value_counts().keys()[0:1])
    elif 'Birth Year' not in df.columns:
        print("sorry we don't have the Birth date in the data base for the city of washington" )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def displaydata(df):
    #the function display 5 rows of data 
    
    x=input('do you want to show some data (yes/no) \n').lower()
    while x not in ['yes','no']:
         x=input('do you want to show some data (yes/no) ? \n').lower()
        
    if x=='yes':
        ok=True
        i=0
        while ok:
            print(df.iloc[i:i+5])
                
            x=input('do you want to show more rows (yes/no) ?').lower()
            while x not in ['yes','no']:
                x=input('do you want to show more rows (yes/no) ? \n').lower()
            if x=='no':
                ok=False
            elif x=='yes':
                i=i+5
                    
            
            
            
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df2=df.copy()
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        displaydata(df2)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
