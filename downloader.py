# By Yayo
from pytube import YouTube

def downloader(link: str) -> None:    
    global yt
    yt = YouTube(link) 

    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    print("Rating of video: ", yt.rating)

    try:
        ys = yt.streams.get_highest_resolution()
        
        # mp4_dir = path + yt.title + ".mp4"

        print("Downloading...")
        ys.download(r'/home/yayo/Documentos/Programación/downloaded_videos')
        print("Download completed!!")
    except Exception as e:
        print("Error: ", e)

def main() -> None:
    link = input("Enter the link of YouTube video you want to download:  ")
    downloader(link)

if __name__ == '__main__':
    main() 
