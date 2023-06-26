from yt_dlp import YoutubeDL
option = {
	"outtmpl": "movie.webm",
	"format": "bestvideo"
}
ydl = YoutubeDL(option)
result = ydl.download(['https://www.youtube.com/shorts/sjXT0vG8Usc'])

print("result:", result)
