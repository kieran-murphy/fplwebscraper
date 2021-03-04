from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://fantasy.premierleague.com/leagues/1416616/matches/h#")

table = driver.find_element_by_tag_name("table")
fixtures = table.text.split('\n')
fixtures.pop(0)
fixtures.pop(1)
fixtures.pop(4)
fixtures.pop(5)
fixtures.pop(8)
fixtures.pop(9)
fixtures.pop(12)
fixtures.pop(13)
fixtures.pop(16)

"""
final = []
game1 = fixtures[0] + ' ' + fixtures[1] + ' - ' + fixtures[2] + ' ' + fixtures[3]
final.append(game1[3:])
game2 = fixtures[4] + ' ' + fixtures[5] + ' - ' + fixtures[6] + ' ' + fixtures[7]
final.append(game2[3:])
game3 = fixtures[8] + ' ' + fixtures[9] + ' - ' + fixtures[10] + ' ' + fixtures[11]
final.append(game3[3:])
game4 = fixtures[12] + ' ' + fixtures[13] + ' - ' + fixtures[14] + ' ' + fixtures[15]
final.append(game4[3:])
for i in final:
    print(i)
"""

game1 = fixtures[0] + ' ' + fixtures[1] + ' - ' + fixtures[2] + ' ' + fixtures[3]

game2 = fixtures[4] + ' ' + fixtures[5] + ' - ' + fixtures[6] + ' ' + fixtures[7]

game3 = fixtures[8] + ' ' + fixtures[9] + ' - ' + fixtures[10] + ' ' + fixtures[11]

game4 = fixtures[12] + ' ' + fixtures[13] + ' - ' + fixtures[14] + ' ' + fixtures[15]

final = game1[3:] + '\n' + game2[3:] + '\n' + game3[3:] + '\n' + game4[3:] + '\n'

print(final)



driver.quit()
