from pytube import YouTube
url=input('paste the url of video you want to download:-\n')
yt=YouTube(url)
res=input('enter the prefered resolution of video:\n')
stream=yt.streams.get_by_resolution(res)
print(stream)
stream.download("C:\\Users\\chaya\\Downloads")
print("download complete")