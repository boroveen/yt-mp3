from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pyfzf.pyfzf import FzfPrompt
import os.path

#config
Dir="/home/toblack/Музыка"

if os.path.isfile('yt-dlp_linux'):
    print("yt-dlp found")
else:
    print ("download yt-dlp")
    os.system("wget https://github.com/yt-dlp/yt-dlp/releases/download/2023.01.06/yt-dlp_linux;chmod +x ./yt-dlp_linux")

sear = input("search: ")
search = "https://www.youtube.com/results?search_query=" + sear
#print(search)
options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get(search)
videos = driver.find_elements(By.ID, "video-title")

fzf = FzfPrompt()

sear_list = []
for i in range(len(videos)):
#    print(videos[i].text)
    sear_l = videos[i].text
    sear_list.append(sear_l)
    if i == 10:
        break
target_half=fzf.prompt(sear_list)
#print(target_half[0])
vibor2=target_half[0]
for i in range(len(videos)):
    name = videos[i].text
    if name == vibor2:
#        print(videos[i].get_attribute('href'))
        if videos[i].get_attribute('href') is not None:
            zzzz = videos[i].get_attribute('href')
driver.close()

command = "./yt-dlp_linux -f 'ba' -x --audio-format mp3 -o '" + Dir + "/%(title)s.%(ext)s' " + zzzz
os.system(command)
