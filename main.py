import requests
from bs4 import BeautifulSoup
from termcolor import colored
import platform

url = 'https://www.githubstatus.com/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

count_successes = 0
dic_components = {'property': [], 'status': []}
components = soup.find_all('div', class_='component-inner-container')

for component in components:
    property = component.find('span', class_='name').get_text().strip()
    status = component.find('span', class_='component-status').get_text().strip()

    if (status == 'Operational'):
        count_successes = count_successes + 1

    dic_components['property'].append(property)
    dic_components['status'].append(status)

operational_system = platform.system()

if (operational_system == 'Linux'):
    print(colored('Current status:', 'yellow'))
    for i in range(len(components)):
        if (dic_components['status'][i] == 'Operational'):
            print(dic_components['property'][i], '-'*(75 - len(dic_components['property'][i])), colored(dic_components['status'][i], 'green'))
        else:
            print(dic_components['property'][i], '-'*(75 - len(dic_components['property'][i])), colored(dic_components['status'][i], 'red'))
    if (count_successes == len(components)):
        print(colored('✔️ - All Systems Operational', 'green'))
    elif (count_successes > 0):
        print(colored('❗ - Not all operating systems', 'yellow'))
    else:
        print(colored('❌ - None of the operating systems', 'red'))
else:
    print('Current status:')
    for i in range(len(components)):
        if (dic_components['status'][i] == 'Operational'):
            print(dic_components['property'][i], '-'*(75 - len(dic_components['property'][i])), dic_components['status'][i])
        else:
            print(dic_components['property'][i], '-'*(75 - len(dic_components['property'][i])), dic_components['status'][i])
    if (count_successes == len(components)):
        print('OK - All Systems Operational')
    elif (count_successes > 0):
        print('! - Not all operating systems', 'yellow')
    else:
        print('X - None of the operating systems')