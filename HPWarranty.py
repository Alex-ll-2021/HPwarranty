import csv
import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

//This
def process_serial_numbers(input_file, output_file):
    options = webdriver.ChromeOptions()


options.add_experimental_option("detach", True)

with open(input_file, "r") as csv_file:
    reader = csv.DictReader(csv_file)
fieldnames = ["SerialNumber", "WarrantyStartDate", "WarrantyEndDate"]

with open(output_file, "a", newline="") as output_csv:
    writer = csv.DictWriter(output_csv, fieldnames=fieldnames)

for row in reader:
    driver = webdriver.Chrome(options=options)
url = "https://support.hp.com/au-en/check-warranty"
driver.get(url)
time.sleep(3)

serial_number = row["SerialNumber"]
try:
    input_box = driver.find_element(By.ID, "inputtextpfinder")
input_box.clear()
input_box.send_keys(serial_number)
submit_button = driver.find_element(By.ID, "FindMyProduct")
submit_button.click()
time.sleep(5)
html_source = driver.page_source
start_date_div = driver.find_element(By.XPATH, "//div[contains(@class, 'startDatecontainer')]")
start_date_str = start_date_div.text.split(":")[1].strip()
start_date = datetime.strptime(start_date_str, "%B %d, %Y").date()

try:
    end_date_div = driver.find_element(By.XPATH, "//div[contains(@class, 'endDatecontainer')]")
end_date_str = end_date_div.text.split(":")[1].strip()
end_date = datetime.strptime(end_date_str, "%B %d, %Y").date()
except NoSuchElementException:
end_date = None

writer.writerow(
    {"SerialNumber": serial_number, "WarrantyStartDate": start_date, "WarrantyEndDate": end_date}
)

except Exception as e:
print(f"Error processing serial number '{serial_number}': {str(e)}")

driver.quit()

input_file = "C:/Temp/input.csv"
output_file = "C:/Temp/output.csv"
process_serial_numbers(input_file, output_file)