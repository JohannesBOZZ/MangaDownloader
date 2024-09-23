# MangaDownloader

[Setup](#Setup)

[Explanation](#Explanation)

[Example](#Example)

## Setup

Execute the requirements.txt with either go to the folder of the requirements.txt and enter the following command or use the absolute path
```
pip install -r requirements.txt
```
## Explanation

The main function you will use is the `downloadMangaCli`, This function is a member function of the class Mangadex.

This function gets a list with one of the following values.

1. Just the Mangadex id as a String or as a list with the String, a Mangadex id looks like this `77bee52c-d2d6-44ad-a33a-1734c1fe696a` and is in the link of a manga from Mangadex.
2. A list with the Mangadex id as the first value and the link for the [manga-downloader](https://github.com/elboletaire/manga-downloader) is the second value. this can be necessary when Mangadex doesn't have all the chapters. The Mangadex id can also be an manga title, but then the second value is absolutely necessary. And if there is no Mangadex id then there will also be no Metadata from Mangadex
3. The same as in point 2 just with the MyAnimeList id as the third value. the MyAnimeList id is also in the link from the manga.

Then you must set a downloadPath, the default is the download folder of your os.

As long as the `manga-downloader.exe` isn't moved you can ignore the exe parameter, else there comes the path of the `manga-downloader.exe`

If `updateChapterWithoutCover` is True the by every call of this function, all manga chapters with cover get extracted and get updated metadata and a cover if there is one.

concurrentChapterDownload is the number of how many chapters will be downloaded simultaneously by the manga downloader.

### Other things
The function `setTempFolder` will change the temp folder. The temp folder is the folder where extracted chapters are stored and deleted afterwards. This folder should ideally be some folder located in the RAM, for this you could use [ImDisk](https://sourceforge.net/projects/imdisk-toolkit/). the default value is the folder `C:\Temp`.

## Example

```python
from Mangadex import Mangadex

mangadex = Mangadex()

ids = [
    ["b0b721ff-c388-4486-aa0f-c2b0bb321512"],# Sousou no Frieren
    ["d8a959f7-648e-4c8d-8f23-f1f3f8e129f3", "https://readmangabat.com/read-bi357727"],# One-Punch Man
    ["77bee52c-d2d6-44ad-a33a-1734c1fe696a", "https://readmangabat.com/read-ij386428", "119022"],# Kage no Jitsuryokusha ni Naritakute
]


mangadex.setTempFolder(r"W:\Temp").downloadMangaCli(ids=ids, downloadPath=r"C:\Manga", updateChapterWithoutCover=True)

```
