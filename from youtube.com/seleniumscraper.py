from selenium import webdriver
import pandas as pd

url = 'https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg/videos?view=0&sort=p&flow=grid'

browser = webdriver.Chrome('/web-scrapers/chromedriver_win32/chromedriver.exe')
browser.get(url)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 

videos = browser.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

videos_list = []

for video in videos:
	title = video.find_element_by_xpath('.//*[@id="video-title"]').text
	views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
	when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text

	vid_item = {
	    'title': title,
	    'views': views,
	    'posted': when
	}

	videos_list.append(vid_item)


df = pd.DataFrame(videos_list)
print(df)

df.to_csv('youtube_channel_videos.csv')
df.to_excel('youtube_channel_videos.xlsx')

browser.close()
quit()
