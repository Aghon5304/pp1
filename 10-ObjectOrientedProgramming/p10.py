class Music():
    def __init__(self,song,album,year,author):
        self.song = song
        self.album = album 
        self.year = year
        self.author = author
    
    def __str__(self):
        return "Song: " + self.song +"\nAlbum: "+ self.album + "\nYear: "+ str(self.year)+"\nAuthor: "+self.author
    
muzyka = Music("this fire","Franz Ferdinand",2004,"Franz Ferdinand")
muzyka2 = Music("utuwadasda","album",123,"auror")
print(muzyka)
print(muzyka2)