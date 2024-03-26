import requests
import os
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    # your code here
    #make directory downloads
    if not os.path.exists("./downloads/"):
        os.makedirs("./downloads")
    os.chdir("./downloads")

    print(os.getcwd())

    #download file from url
    for uri in  download_uris:
        r = requests.get(uri, stream=True)
        #get file name from uri

        filename = os.path.basename(uri)

        if (r.status_code == 200):
            with open(filename, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=10240):
                    fd.write(chunk)
                print("Downloaded file {}".format(filename))
            zipfile.ZipFile(filename).extractall()



        else:
            print(r.status_code)


if __name__ == "__main__":
    main()
