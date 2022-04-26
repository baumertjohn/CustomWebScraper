# Custom Web Scraper - 100 Days of Code Capstone
# Scape the following and create a csv file with data
# Site to scrape - https://steamdb.info/graph/
# Data to retrieve (Image) / Name / Current Players / All-Time Peak

import csv

from selenium.webdriver import Chrome

WEBPAGE = "https://steamdb.info/graph/"

driver = Chrome(executable_path="./chromedriver.exe")


def main():
    driver.get(WEBPAGE)
    table_data = driver.find_elements_by_tag_name("td")
    name = []
    current_players = []
    all_time_peak = []
    i = 0
    while i < 699:
        i += 2
        name.append(table_data[i].text)
        i += 1
        current_players.append(table_data[i].text)
        i += 2
        all_time_peak.append(table_data[i].text)
        i += 2

    combined_list = list(zip(name, current_players, all_time_peak))
    combined_list.insert(0, ("Name", "Current Players", "All-Time Peak"))

    with open("steamdb_data.csv", "w", newline="", encoding="utf-8") as file:
        write = csv.writer(file)
        write.writerows(combined_list)


if __name__ == "__main__":
    main()
