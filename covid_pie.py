import pandas as pd
import pygal
from datetime import date
from pygal.style import Style

def extract_data():
    # read states data using Panda's library
    df = pd.read_csv("us-states.csv")
    df['date'] = pd.to_datetime(df['date'])

    # Filter dataset to only have data for July 1, 2020
    date_to_filter = pd.Timestamp(date(2020,7,1))
    df = df[ (df['date'] == date_to_filter ) ]

    # Find total cases in all states
    df['total'] = df['cases'].sum() 

    # Get top 5 states by sorting data by descending number of cases
    df.sort_values("cases", inplace=True, ascending=False)
    top_5 = df.head(5)

    # Extract states and top 5 states and cases percent to total
    state_list = list(top_5['state'])
    cases_percent = list((top_5['cases']/top_5['total']) * 100)

    return zip(state_list, cases_percent)


def make_chart(data):
    # Create custom styles
    custom_style = Style(colors=('#DB8274', '#338391', '#D3A3D9', '#900C3F', '#D4D068'))

    # Generate Pie chart using custom style
    pie_chart = pygal.Pie(explicit_size=25, style=custom_style)
    pie_chart.title = 'Top 5 US states with most COVID cases on July 1, 2020 (in %)'
    for (s, d) in data:
        pie_chart.add(s, round(d, 2))
    pie_chart.render_in_browser()


if __name__ == "__main__":
    data = extract_data()
    make_chart(data)