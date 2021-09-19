import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker

# Section 2 - Loading and Selecting Data
df = pd.read_csv(
    'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv',
    parse_dates=['Date'])
countries = ['Canada', 'Germany', 'United Kingdom', 'US', 'France', 'China']
df = df[df['Country'].isin(countries)]

print("Data Loaded")

# Section 3 - Creating a Summary Column
df['Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)

df = df.pivot(index='Date', columns='Country', values='Cases')
countries = list(df.columns)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries

print("Summary Created")

# Section 5 - Calculating Rates per 100,000
populations = {
    'Canada': 37664517,
    'Germany': 83721496,
    'United Kingdom': 67802690,
    'US': 330548815,
    'France': 65239883,
    'China': 1438027228
}
percapita = covid.copy()
for country in list(percapita.columns):
    percapita[country] = percapita[country] / populations[country] * 100000

print("Rates Calculated")

colors = {
    'Canada': '#045275',
    "China": "#089099",
    "France": "#7CCBA2",
    "Germany": "#FCDE9C",
    "US": "#DC3977",
    "United Kingdom": "#7C1D6F"
}
plt.style.use('fivethirtyeight')
plot = covid.plot(figsize=(12, 8),
                  color=list(colors.values()),
                  linewidth=5,
                  legend=False)

plot.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('# of Cases')

for country in list(colors.keys()):
    plot.text(x=covid.index[-1],
              y=covid[country].max(),
              color=colors[country],
              s=country,
              weight='bold')

#plot.text(x = covid.index[1], y = int(covid.max().max())+45000, s = "Covid-19 Cases by Country", fontsize = 23, weight = 'bold', alpha = .75)
plt.title('Covid Cases by Country')
plot.text(x=covid.index[1],
          y=int(covid.max().max()) + 15000,
          s="",
          fontsize=16,
          alpha=.75)
plot.text(x=percapita.index[1], y=-100000, s="")
plt.tight_layout()
# plt.show()


plt.savefig("img.jpg")
print("File Saved")
