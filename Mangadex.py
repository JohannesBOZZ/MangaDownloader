from pathlib import Path
from datetime import datetime
from pprint import pprint
import sys
from natsort import os_sorted
from typing import Literal
from mal import Manga, MangaSearch, MangaSearchResult
import re
import xml.etree.ElementTree as ET
import xml.dom.minidom
import shutil
import datetime
import MangaDexPy.downloader
import requests
import os
import re
import json
import time
import zipfile
import MangaDexPy
import subprocess


class Mangadex:

    def __init__(self) -> None:
        self.cli = MangaDexPy.MangaDex()
        #self.cli.login("maxb12032005@gmail.com", "yoolider31er")
        self.dictionary: dict
        self.objects: list
        self.downloadFolder = str(Path.home() / "Downloads")
        self.downloadPath = self.downloadFolder + "\\mangaDL"
        self.currentFolder = os.path.dirname(os.path.realpath(__file__))
        self.archiveExtensions = (".cbz", ".zip")
        self.tmpFolder = r"C:\Temp\mangaDownloader"
        self.languageCodes = {
            "": "unknown",
            "ko-ro": "Korean (Romanized)",
            "ja-ro": "Japanese (Romanized)",
            "zh-hk": "Chinese (Traditional)",
            "zh-ro": "Chinese (Romanized)",
            "es-la": "Latin American Spanish",
            "cdj": "cdj",
            "pt-br": "pt-br",
            "ab": "Abkhaz",
            "aa": "Afar",
            "af": "Afrikaans",
            "ak": "Akan",
            "sq": "Albanian",
            "am": "Amharic",
            "ar": "Arabic",
            "an": "Aragonese",
            "hy": "Armenian",
            "as": "Assamese",
            "av": "Avaric",
            "ae": "Avestan",
            "ay": "Aymara",
            "az": "Azerbaijani",
            "bm": "Bambara",
            "ba": "Bashkir",
            "eu": "Basque",
            "be": "Belarusian",
            "bn": "Bengali",
            "bh": "Bihari",
            "bi": "Bislama",
            "bs": "Bosnian",
            "br": "Breton",
            "bg": "Bulgarian",
            "my": "Burmese",
            "ca": "Catalan",
            "ch": "Chamorro",
            "ce": "Chechen",
            "ny": "Chichewa",
            "zh": "Chinese",
            "cv": "Chuvash",
            "kw": "Cornish",
            "co": "Corsican",
            "cr": "Cree",
            "hr": "Croatian",
            "cs": "Czech",
            "da": "Danish",
            "dv": "Divehi",
            "nl": "Dutch",
            "dz": "Dzongkha",
            "en": "English",
            "eo": "Esperanto",
            "et": "Estonian",
            "ee": "Ewe",
            "fo": "Faroese",
            "fj": "Fijian",
            "fi": "Finnish",
            "fr": "French",
            "ff": "Fula",
            "gl": "Galician",
            "ka": "Georgian",
            "de": "German",
            "el": "Greek",
            "gn": "Guarani",
            "gu": "Gujarati",
            "ht": "Haitian",
            "ha": "Hausa",
            "he": "Hebrew",
            "hz": "Herero",
            "hi": "Hindi",
            "ho": "Hiri Motu",
            "hu": "Hungarian",
            "ia": "Interlingua",
            "id": "Indonesian",
            "ie": "Interlingue",
            "ga": "Irish",
            "ig": "Igbo",
            "ik": "Inupiaq",
            "io": "Ido",
            "is": "Icelandic",
            "it": "Italian",
            "iu": "Inuktitut",
            "ja": "Japanese",
            "jv": "Javanese",
            "kl": "Kalaallisut",
            "kn": "Kannada",
            "kr": "Kanuri",
            "ks": "Kashmiri",
            "kk": "Kazakh",
            "km": "Khmer",
            "ki": "Kikuyu",
            "rw": "Kinyarwanda",
            "ky": "Kirghiz",
            "kv": "Komi",
            "kg": "Kongo",
            "ko": "Korean",
            "ku": "Kurdish",
            "kj": "Kwanyama",
            "la": "Latin",
            "lb": "Luxembourgish",
            "lg": "Luganda",
            "li": "Limburgish",
            "ln": "Lingala",
            "lo": "Lao",
            "lt": "Lithuanian",
            "lu": "Luba-Katanga",
            "lv": "Latvian",
            "gv": "Manx",
            "mk": "Macedonian",
            "mg": "Malagasy",
            "ms": "Malay",
            "ml": "Malayalam",
            "mt": "Maltese",
            "mi": "Maori",
            "mr": "Marathi",
            "mh": "Marshallese",
            "mn": "Mongolian",
            "na": "Nauru",
            "nv": "Navajo",
            "nb": "Norwegian Bokmål",
            "nd": "North Ndebele",
            "ne": "Nepali",
            "ng": "Ndonga",
            "nn": "Norwegian Nynorsk",
            "no": "Norwegian",
            "ii": "Nuosu",
            "nr": "South Ndebele",
            "oc": "Occitan",
            "oj": "Ojibwe",
            "cu": "Old Church Slavonic",
            "om": "Oromo",
            "or": "Oriya",
            "os": "Ossetian",
            "pa": "Panjabi",
            "pi": "Pali",
            "fa": "Persian",
            "pl": "Polish",
            "ps": "Pashto",
            "pt": "Portuguese",
            "qu": "Quechua",
            "rm": "Romansh",
            "rn": "Kirundi",
            "ro": "Romanian",
            "ru": "Russian",
            "sa": "Sanskrit",
            "sc": "Sardinian",
            "sd": "Sindhi",
            "se": "Northern Sami",
            "sm": "Samoan",
            "sg": "Sango",
            "sr": "Serbian",
            "gd": "Scottish Gaelic",
            "sn": "Shona",
            "si": "Sinhala",
            "sk": "Slovak",
            "sl": "Slovene",
            "so": "Somali",
            "st": "Southern Sotho",
            "es": "Spanish",
            "su": "Sundanese",
            "sw": "Swahili",
            "ss": "Swati",
            "sv": "Swedish",
            "ta": "Tamil",
            "te": "Telugu",
            "tg": "Tajik",
            "th": "Thai",
            "ti": "Tigrinya",
            "bo": "Tibetan Standard",
            "tk": "Turkmen",
            "tl": "Tagalog",
            "tn": "Tswana",
            "to": "Tonga",
            "tr": "Turkish",
            "ts": "Tsonga",
            "tt": "Tatar",
            "tw": "Twi",
            "ty": "Tahitian",
            "ug": "Uighur",
            "uk": "Ukrainian",
            "ur": "Urdu",
            "uz": "Uzbek",
            "ve": "Venda",
            "vi": "Vietnamese",
            "vo": "Volapük",
            "wa": "Walloon",
            "cy": "Welsh",
            "wo": "Wolof",
            "fy": "Western Frisian",
            "xh": "Xhosa",
            "yi": "Yiddish",
            "yo": "Yoruba",
            "za": "Zhuang",
            "zu": "Zulu"
        }
        self.externalNames = {
            'al': 'AniList',
            'amz': 'Amazon',
            'ap': 'Anime-Planet',
            'bw': 'Book☆Walker',
            'ebj': 'eBookJapan',
            'engtl': 'Official English',
            'kt': 'Kitsu',
            'mal': 'MyAnimeList',
            'mu': 'MangaUpdates',
            'nu': 'NovelUpdates',
            'raw': 'raw',
            'cdj': 'cdj'
        }
        self.externalBaseUrls = {
            'al': 'https://anilist.co/manga/',
            'ap': 'https://www.anime-planet.com/manga/',
            'bw': 'https://bookwalker.jp/',
            'kt': 'https://kitsu.io/manga/',
            'mal': 'https://myanimelist.net/manga/',
            'mu': 'https://www.mangaupdates.com/series.html?id=',
            'nu': 'https://www.novelupdates.com/series/',
            'cdj': 'cdj',
            'raw': '',
            'engtl': '',
        }
    
    def setTempFolder(self, folder:str):
        self.tmpFolder = os.path.join(folder, "mangaDownloader")
        return self
    
    def makeDir(self, directory:str):
        if not os.path.exists(directory):
            os.makedirs(directory)


    def removeFile(self, filePath:str):
        if os.path.isfile(filePath):
            os.remove(filePath)
            

    def createFile(self, filePath:str, content=""):
        if not os.path.isfile(filePath):
            with open(filePath, "w") as f:
                f.write(content)


    def getFileContent(self, filePath:str, mode=Literal["r", "r+", "rb", "w", "w+", "wb", "a", "a+"]):
        try:
            with open(filePath, mode) as f:
                return f.read()
        except OSError as e:
            self.__writeLog(f"OS Error: {e}")
            return ""


    def writeToFile(self, filePath:str, content:str, mode=Literal["r", "r+", "rb", "w", "w+", "wb", "a", "a+"]):
        try:
            with open(filePath, mode) as f:
                f.write(content)
        except OSError as e:
            self.__writeLog(f"OS Error: {e}")


    def sanitizeForWindowsPath(self, path):
        # Remove characters that are not allowed in Windows file paths
        invalid_chars = '<>:"/\|?*\x00\x1f'
        sanitized_path = re.sub(f'[{re.escape(invalid_chars)}]', '', path)

        # Remove trailing dots and spaces
        sanitized_path = sanitized_path.rstrip(' .')

        # Ensure the path is not empty
        if not sanitized_path:
            sanitized_path = "Unnamed"

        return sanitized_path
            
    def __writeLog(self, text:str, printOnConsole=True):
        try:
            with open(f"{self.currentFolder}\\mangadex.log", "x"): pass
        except: pass
        
        try:
            now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            with open(f"{self.currentFolder}\\mangadex.log", "a") as logs:
                logs.write(f"[{now}] {text}\n")
                if printOnConsole:
                    print(f"[{now}] {text}\n")
        except Exception as e:
            print(f"Error occurred: {e}")

    
    def getTachiyomiDict(self, manga:MangaDexPy.manga.Manga):
        """returns a dictionary in the style of the tachiyomi details.json file
        with the data from the self.dictionary that can be obtained from the getNhentaiDict function
        
        return dict
        """
        summaryText = "Alternative Titles:\n" + "\n".join([f"{self.languageCodes[lang]}:\t{title}" for entry in manga.titles for lang, title in entry.items()]) + "\n"

        linkText = []
        for key, x in manga.links.items():
            try:
                if x.startswith("https://"):
                    linkText.append(f"{self.externalNames[key]}:\t{x}")
                else:
                    linkText.append(f"{self.externalNames[key]}:\t{self.externalBaseUrls[key]}{x}")
            except KeyError as keyErr:
                print(str(keyErr))
        linkText = "\n".join(linkText)

        descText = "\n".join([f"{self.languageCodes[lang]}:\t{desc}" for lang, desc in manga.desc.items()])

        summaryText += linkText + "\n" + descText
        status_dict = {
            "unknown": "0",
            "ongoing": "1",
            "completed": "2",
            "licensed": "3",
            "publishing finished": "4",
            "cancelled": "5",
            "on hiatus": "6",
            "hiatus": "6"
        }
        tachiyomiDict = {
            	"title": [value for key, value in manga.title.items()][0],
	            "author": ", ".join([x.name for x in manga.author]),
	            "artist": ", ".join([x.name for x in manga.artist]),
	            "description": summaryText,
	            "genre": ", ".join([name for entry in manga.tags for lang, name in entry.name.items()]),
	            "status": status_dict[manga.status.lower()],
	            "_status values": ["0 = Unknown", "1 = Ongoing", "2 = Completed", "3 = Licensed", "4 = Publishing finished", "5 = Cancelled", "6 = On hiatus"]
        }

        return tachiyomiDict


    def getMalStats(self, malManga:Manga):
        summaryText = f"<a target='_Blanc' href=\"{malManga.url}\">MayAnimeList</a> stats as of {datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y')}:\n"
        
        summaryText += f'<table>'
        summaryText += f"<tr><td width='100px'>Score</td><td>{malManga.score or 'N/A'}</td></tr>"
        summaryText += f"<tr><td width='100px'>Ranked</td><td>#{malManga.rank or 'N/A'}</td></tr>"
        summaryText += f"<tr><td width='100px'>Scored by</td><td>{malManga.scored_by or 'N/A'} users</td></tr>"
        summaryText += f"<tr><td width='100px'>Popularity</td><td>#{malManga.popularity or 'N/A'}</td></tr>"
        summaryText += f"<tr><td width='100px'>Members</td><td>{malManga.members or 'N/A'}</td></tr>"
        summaryText += f"<tr><td width='100px'>Favorites</td><td>{malManga.favorites or 'N/A'}</td></tr>"
        summaryText += "</table>\n\n"
        return summaryText


    def getComicInfoXmlString(self, manga:MangaDexPy.manga.Manga, chapter:MangaDexPy.chapter.Chapter, malManga:Manga, language):
        summaryText = self.getMalStats(malManga)
        
        summaryText += "Alternative Titles:\n<table>" + "".join([f"<tr><td width='160px'>{self.languageCodes[lang]}</td><td>{title}</td></tr>" for entry in manga.titles for lang, title in entry.items()]) + "</table>\n\n"

        linkText = []
        for key, x in manga.links.items():
            try:
                if x.startswith("https://"):
                    linkText.append(f"<tr><td width='160px'>{self.externalNames[key]}</td><td><a target='_Blanc' href=\"{x}\" style='color: var(--primary-color)'>{x}</a></td></tr>")
                else:
                    linkText.append(f"<tr><td width='160px'>{self.externalNames[key]}</td><td><a target='_Blanc' href=\"{self.externalBaseUrls[key]}{x}\" style='color: var(--primary-color)'>{self.externalBaseUrls[key]}{x}</a></td></tr>")
            except KeyError as keyErr:
                print(f"KeyError: {str(keyErr)}")
        linkText = "<table>" + "".join(linkText) + "</table>\n\n"

        descText = "\n\n".join([f"{self.languageCodes[lang]}:\t{desc}" for lang, desc in manga.desc.items()]) + "\n\n\n"
        
        if malManga.synopsis:
            descText += f"MyAnimeList synopsis: {malManga.synopsis}\n\n"
        if malManga.background:
            descText += f"MyAnimeList background: {malManga.background}\n"

        summaryText += linkText + "\n" + descText
        # Create XML structure
        root = ET.Element("ComicInfo")
        root.set("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        # Add elements to XML
        title = ET.SubElement(root, "Title")
        title.text = f" chapter {chapter.chapter}  {chapter.title or ''}"
        series = ET.SubElement(root, "Series")
        series.text = malManga.title
        seriesSort = ET.SubElement(root, "SeriesSort")
        seriesSort.text = malManga.title
        localizedSeries = ET.SubElement(root, "LocalizedSeries")
        localizedSeries.text = malManga.title_english
                
        summary = ET.SubElement(root, "Summary")
        summary.text = summaryText
        web = ET.SubElement(root, "Web")
        urls = [x if x.startswith("https://") else f"{self.externalBaseUrls[key]}{x}" for key, x in manga.links.items()]
        web.text = ','.join(urls) #f"https://mangadex.org/chapter/{chapter.id}"
        dt = datetime.datetime.strptime(chapter.published_at, "%Y-%m-%dT%H:%M:%S%z")
        year = ET.SubElement(root, "Year")
        year.text = str(dt.year)
        month = ET.SubElement(root, "Month")
        month.text = str(dt.month)
        day = ET.SubElement(root, "Day")
        day.text = str(dt.day)
        
        writer = ET.SubElement(root, "Writer")
        writer.text = ", ".join([x.name for x in manga.author])
        penciller = ET.SubElement(root, "Penciller")
        penciller.text = ", ".join([x.name for x in manga.artist])
        translator = ET.SubElement(root, "Translator")
        translator.text = ','.join([x if type(x) == str else x.name for x in chapter.group])
        genre = ET.SubElement(root, "Genre")
        genre.text = manga.type
        tags = ET.SubElement(root, "Tags")
        tags.text = ", ".join([name for entry in manga.tags for lang, name in entry.name.items()])
        character = ET.SubElement(root, "Characters")
        character.text = ",".join([name.name.replace(",", "") for name in malManga.characters])
        
        volume = ET.SubElement(root, "Volume")
        volume.text = chapter.volume
        number = ET.SubElement(root, "Number")
        number.text = chapter.chapter
        languageIso = ET.SubElement(root, "LanguageISO")
        languageIso.text = language
        manga = ET.SubElement(root, "Manga")
        manga.text = "Yes"
        # Convert XML tree to string
        xmlString = ET.tostring(root, encoding="unicode")
        xmlDom = xml.dom.minidom.parseString(xmlString)

        return xmlDom.toprettyxml(indent="    ")


    def getComicInfoXmlStringMalOnly(self, malManga:Manga, chapterNumber:float):
        summaryText = self.getMalStats(malManga)

        if malManga.synopsis:
            summaryText += f"MyAnimeList synopsis: {malManga.synopsis}\n\n"
        if malManga.background:
            summaryText += f"MyAnimeList background: {malManga.background}\n"

        # Create XML structure
        root = ET.Element("ComicInfo")
        root.set("xmlns:xsd", "http://www.w3.org/2001/XMLSchema")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        # Add elements to XML
        title = ET.SubElement(root, "Title")
        title.text = f"Chapter {int(chapterNumber) if chapterNumber == float(int(chapterNumber)) else chapterNumber}"
        series = ET.SubElement(root, "Series")
        series.text = malManga.title
        seriesSort = ET.SubElement(root, "SeriesSort")
        seriesSort.text = malManga.title
        localizedSeries = ET.SubElement(root, "LocalizedSeries")
        localizedSeries.text = malManga.title_english
                
        summary = ET.SubElement(root, "Summary")
        summary.text = summaryText
        web = ET.SubElement(root, "Web")
        web.text = malManga.url
        # dt = datetime.datetime.strptime(chapter.published_at, "%Y-%m-%dT%H:%M:%S%z")
        # year = ET.SubElement(root, "Year")
        # year.text = str(dt.year)
        # month = ET.SubElement(root, "Month")
        # month.text = str(dt.month)
        # day = ET.SubElement(root, "Day")
        # day.text = str(dt.day)
        
        writer = ET.SubElement(root, "Writer")
        writer.text = ",".join([name.replace(",", "") for name in malManga.authors])
        tags = ET.SubElement(root, "Tags")
        tags.text = ",".join(malManga.genres + malManga.themes)
        character = ET.SubElement(root, "Characters")
        character.text = ",".join([name.name.replace(",", "") for name in malManga.characters])
        
        number = ET.SubElement(root, "Number")
        number.text = str(int(chapterNumber) if chapterNumber == float(int(chapterNumber)) else chapterNumber)
        manga = ET.SubElement(root, "Manga")
        manga.text = "Yes"
        # Convert XML tree to string
        xmlString = ET.tostring(root, encoding="unicode")
        xmlDom = xml.dom.minidom.parseString(xmlString)

        return xmlDom.toprettyxml(indent="    ")


    def updateLibrary(self, ids:list, downloadPath="download", language="en", exe:str|None=None, updateAfter:float=48, updateChapterWithoutCover=False):
        """"updateAfter: Time between updates in hours"""
        now = time.time()        
        timestampFile = f"{self.currentFolder}\\mangadexLastUpdate.log"
        self.createFile(timestampFile, str(now))
        
        lastTimestamp = float(self.getFileContent(timestampFile, "r") or 0)
        
        if (now - lastTimestamp) >= (updateAfter * 3600):
            self.downloadMangaCli(ids=ids, downloadPath=downloadPath, language=language, updateChapterWithoutCover=updateChapterWithoutCover)
            self.writeToFile(timestampFile, str(now), "w")
        
        return self


    def downloadMangaCli(self, ids:list[list|str], downloadPath="download", language="en", exe:str|None=None, updateChapterWithoutCover=True, concurrentChapterDownload:Literal[1,2,3,4,5]=1):
        """Downloads one or more manga's with `https://github.com/elboletaire/manga-downloader`
        
        ids:  List with ids a list entry could be just a string with a Mangadex id or a list with Mangadex id and the link for downloading
        or the same as before just with the MyAnimeList ID from Manga
        
        downloadPath:  the path were the manga/manga's is downloaded for example:
        
        ```       
        downloadPath
            {manga title}
                Ch.1.cbz
                Ch.2.cbz
                Ch.3.cbz
                ...
            {manga title}
                Ch.1.cbz
                Ch.1.1.cbz
                ...
        ```
        language:  is the language and uses the ISO 639 language codes like en for English.
        
        exe:  this is the folder from the manga-downloader.exe. When left empty it's assumed that the exe is in the same folder as the Mangadex.py
        
        updateChapterWithoutCover:  reads the chapterCovers.json and it updates the cover and metadata for every chapter that hasn't an entry in the json file
        
        concurrentChapterDownload: How many chapter are downloaded at the same time
        """
        startTime = time.time()
        
        tmpIds = ids
        ids = []
        for x in tmpIds:
            if len(x) > 1 and (type(x) == tuple or type(x) == list):
                ids.append(list(x))
            elif type(x) == tuple or type(x) == list:
                ids.append([x[0], x[0], None])
            else:
                ids.append([x, x, None])
        
            if len(x) == 2:
                ids[-1].append(None)
        
        ids = [tuple(x) for x in ids]
        
        if downloadPath == "download":
            downloadPath = self.downloadPath
            
        downloadedMangaCount = 0
        for mangaId, downloadUrl, malId in ids:
            while True:
                try:
                    try:
                        manga = self.cli.get_manga(mangaId)
                        search = MangaSearch(next(iter(manga.title.values())))
                        isMangadex = True
                    except MangaDexPy.NoContentError as e:
                        search = MangaSearch(mangaId)
                        isMangadex = False
                    break
                except Exception as e:
                    self.__writeLog(f"Exception: {e}\tWaiting for 10 seconds...")
                    time.sleep(10)
            
            if malId is None:
                malId = search.results[0].mal_id
                
            malManga = Manga(int(malId))
            
            print(f"Fetched manga {mangaId}")
            time.sleep(2)
            mangaTitle = self.sanitizeForWindowsPath(malManga.title)

            currentDlPath = f"{downloadPath}\\{mangaTitle}"
            self.makeDir(currentDlPath)


            existingFiles = [x.path for x in os.scandir(currentDlPath) if x.path.endswith(self.archiveExtensions)]
            
            firstChapter = 0.0
            if len(existingFiles) > 0:
                existingFiles = os_sorted(existingFiles)
                chapterNumber = re.findall("(\d+.\d+|\d+)", existingFiles[-1]) or ["-999"]
                firstChapter = float(chapterNumber[-1]) + 1 if chapterNumber[-1] != "-999" else 0.0


            print(f"First Chapter: {firstChapter}")
            print(f"Fetching chapters for {mangaTitle}")
            sleepTime = 10
            chapterNumbers = []
            while isMangadex:
                try:
                    chapters = []
                    x: MangaDexPy.chapter.Chapter
                    for x in manga.get_chapters():
                        if x.chapter and x.chapter.replace(".", "").isnumeric() and x.chapter not in chapterNumbers:
                            chapterNumbers.append(x.chapter)
                            chapters.append(x)
                    break
                except Exception as e:
                    self.__writeLog(f"Exception: {e}\tWaiting for {sleepTime} seconds...")
                    time.sleep(sleepTime)
                    if sleepTime < 60: sleepTime += 10
                
            if len(chapters) == 0:
                self.__writeLog(f"{mangaTitle} has no chapter in the language {language}")

            
            time.sleep(5)
            if isMangadex:
                print(f"Found {len(chapters)} chapters")
                chapters.sort(key=lambda x: float(x.chapter))
                lastChapter = float(chapters[-1].chapter)
                
            lastChapter = 99999.0
                
                
            if exe:
                mangaDownloaderLocation = exe
            else:
                mangaDownloaderLocation = os.path.join(self.currentFolder, "manga-downloader")
                
            if mangaId == downloadUrl:
                Link = f'https://mangadex.org/title/{mangaId}'
            else:
                Link = downloadUrl
            
            cmdCommand = f'"{mangaDownloaderLocation}" {Link} {int(firstChapter)}-{int(lastChapter)} --language {language} --output-dir "{currentDlPath}" --concurrency {concurrentChapterDownload} --filename-template "' + "Ch.{{.Number}}" +'"'
            print(f"CMD Command: {cmdCommand}")
            subprocess.run(cmdCommand)
            
            if updateChapterWithoutCover:
                self.unzipArchivesWithoutCover(currentDlPath)
            else:
                self.unzipArchivesWithoutCover(currentDlPath, firstChapter)
            
            if isMangadex:
                self.addInfoToManga(ids=[(mangaId, downloadUrl, malId)], downloadPath=downloadPath, language=language, updateChapterWithoutCover=updateChapterWithoutCover)
                continue
                
            
            chapterDict:dict[float, MangaDexPy.chapter.Chapter] = {}
            for x in chapters:
                chapterDict[float(x.chapter)] = x
                
            self.addInfoAndCoverToChapter(currentDlPath, manga, chapterDict, malManga, language=language)


    def unzipArchivesWithoutCover(self, currentDlPath:str, startAtChapter:float=0.0, forceUpdateAll:bool=False, updateFirstChapter=True):
        chaptersWithCoversDict = {}
        if os.path.isfile(f"{currentDlPath}\\chapterCovers.json"):
            with open(f"{currentDlPath}\\chapterCovers.json", "r") as f:
                chaptersWithCoversDict = json.load(f)
        print(currentDlPath)
        i = 0
        for x in os_sorted(os.scandir(currentDlPath), key=lambda x: x.name):
            if not x.path.endswith(self.archiveExtensions):
                continue
            
            i += 1
            chapterNumber = re.findall("(\d+.\d+|\d+)", x.name) or ["-999"]
            chapterNumber = chapterNumber[-1]
            
            if not forceUpdateAll and (chapterNumber in chaptersWithCoversDict or float(chapterNumber) < startAtChapter) and i != 1:
                continue
            
            #newFolder = os.path.splitext(x.path)[0]
            newFolder = f"{self.tmpFolder}\\ch.{chapterNumber}"
            self.makeDir(newFolder)
            print(newFolder)
            unziped = False
            with zipfile.ZipFile(x.path, 'r') as unZip:
                unZip.extractall(newFolder)
                unziped = True
            
            if unziped:
                os.remove(x.path)


    def addInfoToManga(self, ids, downloadPath="download", language="en", updateChapterWithoutCover=True, forceUpdateAll:bool=False):
        startTime = time.time()
        
        tmpIds = ids
        ids = []
        for x in tmpIds:
            if len(x) > 1 and (type(x) == tuple or type(x) == list):
                ids.append(list(x))
            elif type(x) == tuple or type(x) == list:
                ids.append([x[0], x[0], None])
            else:
                ids.append([x, x, None])
        
            if len(x) == 2:
                ids[-1].append(None)
        
        ids = [tuple(x) for x in ids]
            
        if downloadPath == "download":
            downloadPath = self.downloadPath
        
        downloadedMangaCount = 0
        for mangaId, downloadUrl, malId in ids:
            while True:
                try:
                    try:
                        manga = self.cli.get_manga(mangaId)
                        search = MangaSearch(next(iter(manga.title.values())))
                        onlyMal = False
                        isMangadex = True
                    except MangaDexPy.NoContentError as e:
                        search = MangaSearch(mangaId)
                        manga = None
                        isMangadex = False
                        onlyMal = True
                    break
                except Exception as e:
                    self.__writeLog(f"Exception: {e}\tWaiting for 10 seconds...")
                    time.sleep(10)
            
            malId = malId or search.results[0].mal_id
            malManga = Manga(int(malId))
            print(f"Fetched manga {mangaId}")
            time.sleep(2)
            mangaTitle = self.sanitizeForWindowsPath(malManga.title)
            
            currentDlPath = f"{downloadPath}\\{mangaTitle}"
            print(currentDlPath)
            self.makeDir(currentDlPath)

            existingFiles = [x.path for x in os.scandir(currentDlPath) if x.path.endswith(self.archiveExtensions)]
            
            firstChapter = 0.0
            if len(existingFiles) > 0:
                existingFiles = os_sorted(existingFiles)
                chapterNumber = re.findall("(\d+.\d+|\d+)", existingFiles[-1]) or ["-999"]
                firstChapter = float(chapterNumber[-1]) if chapterNumber[-1] != "-999" else 0.0
                
                
            if updateChapterWithoutCover:
                self.unzipArchivesWithoutCover(currentDlPath, 0, forceUpdateAll)
            else:
                self.unzipArchivesWithoutCover(currentDlPath, firstChapter, forceUpdateAll)
                
            
            chapters:dict[float, MangaDexPy.chapter.Chapter] = {}
            if not onlyMal:
                print(f"Fetching chapters for {mangaTitle}")
                chapterNumbers = []
                chaptersTmp = manga.get_chapters()
                for x in chaptersTmp:
                    if x.language == language and x.chapter.replace(".", "").isnumeric() and x.chapter not in chapterNumbers:
                        chapterNumbers.append(x.chapter)
                        chapters[float(x.chapter)] = x
                
                for x in chaptersTmp:
                    if x.chapter and x.chapter.replace(".", "").isnumeric() and x.chapter not in chapterNumbers:
                        chapterNumbers.append(x.chapter)
                        chapters[float(x.chapter)] = x
                time.sleep(2)
                print(f"Found {len(chapters)} chapters")
            
            self.addInfoAndCoverToChapter(currentDlPath, manga, chapters, malManga, language)
            


    def addInfoAndCoverToChapter(self, currentDlPath:str, manga:MangaDexPy.manga.Manga|None, chapters:dict[float, MangaDexPy.chapter.Chapter], malManga:Manga, language="en"):
        folderDict = {}
        chaptersWithCoversDict = {}
        if os.path.isfile(f"{currentDlPath}\\chapterCovers.json"):
            with open(f"{currentDlPath}\\chapterCovers.json", "r") as f:
                chaptersWithCoversDict = json.load(f)
        
        mangaTitle = self.sanitizeForWindowsPath(malManga.title)
        
        for folder in os.scandir(self.tmpFolder):
            if folder.path.endswith(self.archiveExtensions):
                continue
            
            if os.path.isdir(folder.path):
                chapterNumber = re.findall("(chapter|ch|c).*?(\d+.\d+|\d+)", folder.name.lower()) or [("Chapter", "-999")]
                folderDict[float(chapterNumber[-1][1])] = folder.path
            
        
        coverDict = {}
        cover: MangaDexPy.cover.Cover
        if manga:
            print(f"Fetching Covers for {mangaTitle}")
            for cover in sorted(manga.get_covers(), key=lambda x: x.created_at):
                coverDict[cover.volume] = cover.url
            print(f"Found {len(coverDict)} covers")
        
        folderToRemove = []
        chapter: MangaDexPy.chapter.Chapter
        defaultCover = coverDict["1"] if "1" in coverDict else None
        
        for currentChapter in folderDict:
            if currentChapter in chapters:
                # chapter is in Mangadex
                chapter = chapters[currentChapter]
                currentFolder = folderDict[currentChapter]
                folderToRemove.append(currentFolder)
                print(currentFolder, "\t", currentChapter)
                xml = self.getComicInfoXmlString(manga, chapter, malManga, language)
                
                try:
                    with open(currentFolder + "\\ComicInfo.xml", "w", encoding="utf-8") as file:
                        file.write(xml)
                except FileNotFoundError as e:
                    print(str(e))
                    
                    
                cbzPath = f"{currentDlPath}\\Ch.{currentChapter if currentChapter % 1 != 0 else int(currentChapter)}.cbz"
                try:
                    if chapter.volume is not None:
                        coverUrl:str = coverDict[chapter.volume]
                    else:
                        coverUrl:str = defaultCover or malManga.image_url

                    res = requests.get(coverUrl)
                    with open(f"{currentFolder}\\0.jpg", "wb") as image:
                        image.write(res.content)
                        if chapter.volume is not None:
                            chaptersWithCoversDict[str(chapter.chapter)] = str(chapter.volume)
                    time.sleep(0.3)
                except Exception as e:
                    print(f"couldn't find any cover for volume {chapter.volume}")
            
            else:
                #chapter isn't in mangadex and only MAL is used
                currentFolder = folderDict[currentChapter]
                folderToRemove.append(currentFolder)
                print(currentFolder, "\t", currentChapter)
                xml = self.getComicInfoXmlStringMalOnly(malManga, float(currentChapter))
                
                try:
                    with open(currentFolder + "\\ComicInfo.xml", "w", encoding="utf-8") as file:
                        file.write(xml)
                except FileNotFoundError as e:
                    print(str(e))
                    
                res = requests.get(defaultCover or malManga.image_url)
                with open(f"{currentFolder}\\0.jpg", "wb") as image:
                    image.write(res.content)
                    chaptersWithCoversDict[str(currentChapter)] = str(currentChapter)
                    
            cbzPath = f"{currentDlPath}\\Ch.{currentChapter if currentChapter % 1 != 0 else int(currentChapter)}.cbz"
            with zipfile.ZipFile(cbzPath, 'w') as cbz:
                for file in os.scandir(currentFolder):
                    cbz.write(file, os.path.basename(file))

        
        with open(f"{currentDlPath}\\details.json", "w") as f:
            try:
                json.dump(self.getTachiyomiDict(manga), f, indent=4)
            except AttributeError: pass
        
        with open(f"{currentDlPath}\\chapterCovers.json", "w") as f:
            json.dump(dict(os_sorted(chaptersWithCoversDict.items(), key=lambda x: x[0])), f, indent=4)
        
        for folder in set(folderToRemove):
            try:
                shutil.rmtree(folder)
            except FileNotFoundError as e:
                self.__writeLog(f"FileNotFoundError - {e}")


    def downloadMangaCovers(self, withId="", withManyIds=[], downloadPath="download"):
        if withId != "":
            withManyIds.append(withId)
            
        if downloadPath == "download":
            downloadPath = self.downloadPath
            
        for id in withManyIds:
            manga = self.cli.get_manga(id)
            mangaTitle = self.sanitizeForWindowsPath([value for key, value in manga.title.items()][0])
            currentDlPath = f"{downloadPath}\\{mangaTitle}"
            self.makeDir(currentDlPath)
            cover: MangaDexPy.cover.Cover
            print(f"Fetching Covers for {mangaTitle}")
            coverCount = 0
            for cover in manga.get_covers():
                coverUrl = cover.url
                res = requests.get(coverUrl)
                coverPath = f"{currentDlPath}\\Volume {cover.volume} {cover.file}"
                with open(coverPath, "wb") as image:
                    image.write(res.content)
                    print(f"Downloaded: {coverPath}")
                    coverCount += 1
                    time.sleep(0.3)
                    
            print(f"Downloaded {coverCount} covers")
            