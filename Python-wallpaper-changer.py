import praw
from ctypes import windll
"""
Project which changes my wallpaper to anything in a selection of the top 5
in the subreddit wallpapers.


Reddit has strict rules on bots which say that you can't have more than 1 request
every 2 seconds, I was searching through some cool reddit modules for python in
the subreddit "learnPython" and i found this praw, which is an excellent webscraper
built for Reddit.
"""

def chooseWallpaper():
    """
    This function returns the url of the chosen Wallpaper from the frontpage of
    the "hot" section of the selected subreddit where the title contains 1920
    (Assuming that the user is looking for a wallpaper with resolution 1920x1080p)
    """
    wallpaperCount = 1
    wallpaperUrlList = []
    for wallpaper in subreddit.get_hot(limit = 25):
        if ("1920" in wallpaper.title) and ("i.i" in wallpaper.url):
            print (wallpaperCount," : ",wallpaper.title)
            wallpaperUrlList = wallpaperUrlList + [wallpaper.url]
            wallpaperCount+=1
    
    wallpaperIndex = int(input("Enter the number of the wallpaper that you want: "))
    return wallpaperUrlList[wallpaperIndex-1]


user_agent = "Wallpaper 0.1"
r = praw.Reddit(user_agent = user_agent)
subreddit = r.get_subreddit("wallpapers")

chosenUrl = chooseWallpaper()

SPI_SETDESKWALLPAPER = 20 
windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, chosenUrl , 0)
