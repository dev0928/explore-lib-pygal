import pandas as pd
from datetime import date
import pygal

def extract_data():
    # read states data using Panda's library
    df = pd.read_csv("us-states.csv")
    df['date'] = pd.to_datetime(df['date'])

    # Filter dataset to only have data for July 1, 2020
    date_to_filter = pd.Timestamp(date(2020,7,1))
    df = df[ (df['date'] == date_to_filter ) ]

    # Get top 10 states with most cases by sorting data by descending number of cases
    df.sort_values("cases", inplace=True, ascending=False)
    top_10 = df.head(10)

    # Extract top 10 states
    state_list = list(top_10['state'])
    cases_list = list(top_10['cases'])

    return zip(state_list, cases_list)


def make_chart(data):    
    # Generate Bar chart using default style
    b_chart = pygal.Bar(explicit_size=25)
    b_chart.title = "Top 10 US states with most COVID cases on July 1, 2020 using Pygal"
    for (s, d) in data:
        b_chart.add(s, d)
    b_chart.render_in_browser()


if __name__ == "__main__":
    data = extract_data()
    make_chart(data)