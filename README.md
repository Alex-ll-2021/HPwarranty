Unfortunately, the HP warranty API is still not working. I have written this script for work purposes. 
It's not perfect, but it's good enough to save some time on querying warranty.

This script uses Python webscraping with the HP warranty website. 
Since I am in Australia, I have included "au-en" in the URL to streamline the process: https://support.hp.com/au-en/check-warranty

Pre-requirements:

Python 3
Selenium package
Chromedriver (https://chromedriver.chromium.org/downloads) configured in the PATH
The input CSV should have the following format:
SerialNumber
SerialNumber1
SerialNumber2

The output CSV will have the following format:
SerialNumber, WarrantyStartDate, WarrantyEndDate
SerialNumber1, 2023-06-30, 2024-06-30
SerialNumber2, 2022-11-02, 2024-11-02

The HP website uses JavaScript to load the HTML and retrieves the query result to display on a new web page. Therefore, traditional methods of static web scraping will not work in this case.

This application uses Selenium with Chromedriver to mimic user actions. It opens the HP warranty site, inputs the serial number in the input box, and clicks on the submit button.

Limitations:

I have set the timeout to 3 seconds for loading the warranty website and 5 seconds for querying the result. However, the actual loading time may vary depending on the network speed and HP server status. You may need to adjust these timings based on your network conditions.

Known Issues:

The script highly relies on the availability and responsiveness of the HP server. If the server is down or experiencing issues, it may affect the script's functionality.

There may be cases where certain serial numbers do not yield any results. In such cases, additional information may be required to retrieve the warranty details. As a solution, I plan to implement a warning system to alert the user about such cases and skip them during the processing.

Alex 04/Jun/2023
