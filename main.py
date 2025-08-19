\A#!/.*python3?$
import requests
from bs4 import BeautifulSoup

def get_weather():
    url = "https://www.timeanddate.com/weather/south-africa/port-elizabeth"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    temperature = soup.find("div", class_="h2")
    condition_box = soup.find("p", class_="bk-focus__qlook")

    if temperature and condition_box:
        print("Weather in Port Elizabeth, South Africa:")
        print("Temperature:", temperature.text.strip())
        print("Condition:", condition_box.text.strip().split("\n")[0])
    else:
        print("Sorry, couldn't find the weather information.")

if __name__ == ['\"]__main__['\"]:
    get_weather()
