import csv
from datetime import datetime
from matplotlib import pyplot as plt 

filename = 'sitka_weather_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
        
    # Get high and low temperatures from file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        if row[7]:
            high = int(row[7])
            highs.append(high)           
        else:
            print("Missing data in highs!")
            highs.append(None)
            
        if row[8]:
            low = int(row[8])
            lows.append(low)
        else:
            print("Missing data in lows!")
            lows.append(None) 

    print("Length of dates:", len(dates))
    print("Length of highs:", len(highs))
    print("Length of lows:", len(lows))
    
    # Filter out None values
    filtered_data = [(date, high, low) for date, high, low in zip(dates, highs, lows) if high is not None and low is not None]
    dates, highs, lows = zip(*filtered_data)

# Plotting data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c ='red', alpha = 0.5)
    plt.plot(dates, lows, c='blue', alpha= 0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    #format plot.
    fig.autofmt_xdate()
    plt.title("Monthly high and low temperatures", fontsize=24)
    plt.xlabel('', fontsize = 16)
    plt.ylabel("temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
