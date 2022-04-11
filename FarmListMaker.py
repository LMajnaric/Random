import re
import time
from math import ceil

import pyautogui as pya
import pyperclip

# navest broj liste da se zna koju stotinu treba dodat , 1 je prva
start_time = time.time()

x_koordinate = [1166, 736]
clubs = [1042, 844]
# list_name = [1044,714]
troop_index = 5  # legionar = 1, pret = 2, imp = 3 etc.

text = pyperclip.paste()

koordinate = re.findall('\({1}-?\d{1,3}\|-?\d{1,3}\)', text)
# pop = re.findall('\n\		(\d{1,3})', text)     # za inactive...it

# Preko gettera je regex {1}-?\d{1,3}\|-?\d{1,3}\s
# Preko inactivesearch.it je regex \({1}-?\d{1,3}\|-?\d{1,3}\)
# print(pop)
print(koordinate)
n = []
y = 0
for y in range(len(koordinate)):
    n.append(re.split('\|', str(koordinate[y])))

# pya.click(clubs,clicks=2)
# pya.press('backspace',presses=5,interval=0.1)
# if n[i]> 100:
#     pya.typewrite()

print(len(n))

for x in range(int(ceil(len(n) / 100))):
    create_new_list = list(pya.locateAllOnScreen(r"create_new_list.png", confidence=0.6))
    pya.click(create_new_list[-1])
    time.sleep(0.35)
    pya.typewrite(str(x + 1))
    time.sleep(1)
    pya.press('tab', presses=troop_index)
    time.sleep(1)
    pya.typewrite('2')
    time.sleep(1)
    create = pya.locateCenterOnScreen(r"create.png", confidence=0.6)
    pya.click(create)
    time.sleep(1)

    # pya.scroll(-500) #dodat ako je lista x preko broja da se addnewtarget ne vidi više u screenu
    # time.sleep(5)
    arrow_down = list(pya.locateAllOnScreen(r"arrow_down.png", confidence=0.75,
                                            region=(1560, 540, 50, 1000)))
    pya.click(arrow_down[-1])
    time.sleep(2)
    for i in range(100):
        if x > 7:  # adjust ovaj broj ovisno o veličini ekrana i koliko lista već postoji
            pya.scroll(-100 * (x - 6))
            time.sleep(5)
        add_new_target = pya.locateCenterOnScreen(r"target.png", confidence=0.6)
        pya.click(add_new_target)
        time.sleep(1)
        pya.click(x_koordinate, clicks=2)
        time.sleep(0.35)
        pya.press('backspace', presses=5, interval=0.01)
        pya.typewrite(n[i + x * 100][0], interval=0.1)
        pya.press('tab')
        pya.press('backspace', presses=5, interval=0.1)
        pya.typewrite(n[i + x * 100][1], interval=0.15)
        time.sleep(0.35)
        pya.press('enter')
        ok = pya.locateCenterOnScreen(r'ok.png', confidence=0.8)
        if (ok != None):
            time.sleep(0.5)
            pya.click(ok)
        else:
            pass
        time.sleep(0.5)
        pya.moveTo(100, 500)
        pya.scroll(-50)
        time.sleep(0.5)
    pya.press('pgup', presses=10)
    time.sleep(3)

    # pya.scroll(-800) #ista stvar kao i prošli scrollovi
    time.sleep(5)
    arrow_up = pya.locateCenterOnScreen(r"arrow_up.png", confidence=0.8)
    pya.click(arrow_up)
    pya.press('pgup', presses=1)
    time.sleep(4)

print("Time to complete :", time.time() - start_time)
