from pytube import YouTube

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)

try:
    ys = yt.streams.get_highest_resolution()
    
    # mp4_dir = path + yt.title + ".mp4"

    print("Downloading...")
    ys.download(r'downloaded_videos')
    print("Download completed!!")
except Exception as e:
    print("Error: ", e)

