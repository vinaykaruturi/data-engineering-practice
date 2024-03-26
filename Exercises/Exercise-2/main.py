import requests
import re
import pandas

# You need to download a file of weather data from a government website. files that are sitting at the following specified location.
#
# https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/
#
# You are looking for the file that was Last Modified on 2022-02-07 14:03, you can't cheat and lookup the file number yourself. You must use Python to scrape this webpage, finding the corresponding file-name for this timestamp, 2022-02-07 14:03
#
# Once you have obtained the correct file, and downloaded it, you must load the file into Pandas and find the record(s) with the highest HourlyDryBulbTemperature. Print these record(s) to the command line.
#
# Generally, your script should do the following ...
#
# Attempt to web scrap/pull down the contents of https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/
# Analyze it's structure, determine how to find the corresponding file to 2022-02-07 14:03 using Python.
# Build the URL required to download this file, and write the file locally.
# Open the file with Pandas and find the records with the highest HourlyDryBulbTemperature.
# Print this to stdout/command line/terminal.



def main():
    url ="https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    response=requests.get(url)
    #read the content of response
    # print(response.text)
    matchedLine=""
    for  line in response.text.splitlines():
        # print (line)
        #if line contains 2022-02-07 14:03
        if "2024-01-19 10:04" in line:
            matchedLine=line
            break

    print(matchedLine)
    #get the word that is enclosed in "" after href=
    matches=re.findall(r'href="([^"]*)"',matchedLine)

    if len(matches)>0:
        response=requests.get(url+matches[0])
        if(response.status_code==200):
            with open("weather_data.csv","wb") as f:
                f.write(response.content)
        #csv has header so we can read it as dataframe
        df=pandas.read_csv("weather_data.csv",sep=",")
        #find the records with the highest HourlyDryBulbTemperature.

        print(df.query("HourlyDryBulbTemperature==HourlyDryBulbTemperature.max()")["HourlyDryBulbTemperature"])

    pass


if __name__ == "__main__":
    main()
