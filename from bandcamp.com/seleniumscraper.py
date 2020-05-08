from selenium import webdriver
import pandas as pd
from time import sleep

url = 'https://bandcamp.com/'

driver = webdriver.Chrome('D:/Python ML DL/Projects/web-scrapers/chromedriver_win32/chromedriver.exe')
driver.get(url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 

# find and click on Play button
##driver.find_element_by_class_name('playbutton').click()


# dicover tracks and play the second track in the list
##tracks = driver.find_elements_by_class_name('discover-item')
##print(len(tracks))
##tracks[1].click()

# tracks details list
tracks_list = []

# get 80 first tracks (10 pages) : title, artist, and genre, and store them in a list / dataframe
for i in range(1, 11):

	tracks = driver.find_elements_by_class_name('discover-item')

	for track in tracks:
		title = track.find_element_by_class_name('item-title').text
		artist = track.find_element_by_class_name('item-artist').text
		genre = track.find_element_by_class_name('item-genre').text

		track_item = {
			'title':title,
			'artist': artist,
			'genre': genre
		}

		if title == '' and artist=='' and genre=='':
			continue

		tracks_list.append(track_item)

	next_button = [e for e in driver.find_elements_by_class_name('item-page')]
	print(next_button[-1].text)

	next_button[-1].click()
	sleep(5)

df = pd.DataFrame(tracks_list)
print(df)

df.to_excel('bandcamp_tracks.xlsx')

driver.close()
quit()