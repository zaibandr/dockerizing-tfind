import requests as r
import random
import time

from find_torrent.scraper.parsers.rutor import rutor_to_torrent
from find_torrent.scraper.parsers.extratorrent import extratorrent_to_torrent

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'rutor.info',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
    'X-Compress': 1
}

proxy_list = [
      {
        "ip": "41.86.149.210",
        "port": 80,
        "type": 1,
        "anonymity": "Low",
        "uptime": 0.58,
        "checked": "2016-12-07T04:55:42",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Niger",
          "nameRu": "Нигерия",
          "iso3166a2": "NG"
        }
      },
      {
        "ip": "217.128.175.129",
        "port": 80,
        "type": 1,
        "anonymity": "High",
        "uptime": 0.19,
        "checked": "2016-12-06T05:07:38",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "France",
          "nameRu": "Франция",
          "iso3166a2": "FR"
        }
      },
      {
        "ip": "41.188.49.210",
        "port": 8080,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 89.2,
        "checked": "2016-12-06T04:53:48",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Madagascar",
          "nameRu": "Мадагаскар",
          "iso3166a2": "MG"
        }
      },
      {
        "ip": "103.4.165.244",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 183.68,
        "checked": "2016-12-06T04:52:50",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Indonesia",
          "nameRu": "Индонезия",
          "iso3166a2": "ID"
        }
      },
      {
        "ip": "197.220.193.137",
        "port": 443,
        "type": 1,
        "anonymity": "Low",
        "uptime": 5.22,
        "checked": "2016-12-06T04:50:31",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Zambia",
          "nameRu": "Замбия",
          "iso3166a2": "ZM"
        }
      },
      {
        "ip": "80.188.79.138",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 3.41,
        "checked": "2016-12-06T04:50:02",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Czechia",
          "nameRu": "Чехия",
          "iso3166a2": "CZ"
        }
      },
      {
        "ip": "94.20.61.124",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.18,
        "checked": "2016-12-06T04:49:54",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Azerbaidjan",
          "nameRu": "Азербайджан",
          "iso3166a2": "AZ"
        }
      },
      {
        "ip": "186.250.96.77",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 2.98,
        "checked": "2016-12-06T04:48:18",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Brazil",
          "nameRu": "Бразилия",
          "iso3166a2": "BR"
        }
      },
      {
        "ip": "92.222.107.189",
        "port": 3128,
        "type": 1,
        "anonymity": "High",
        "uptime": 1.61,
        "checked": "2016-12-06T04:47:53",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Germany",
          "nameRu": "Германия",
          "iso3166a2": "DE"
        }
      },
      {
        "ip": "59.47.125.10",
        "port": 9797,
        "type": 1,
        "anonymity": "Low",
        "uptime": 4.64,
        "checked": "2016-12-06T04:47:42",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "124.88.67.30",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 5.56,
        "checked": "2016-12-06T04:47:21",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "114.57.31.210",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 8.14,
        "checked": "2016-12-06T04:47:11",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Indonesia",
          "nameRu": "Индонезия",
          "iso3166a2": "ID"
        }
      },
      {
        "ip": "27.223.10.171",
        "port": 8998,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 2.86,
        "checked": "2016-12-06T04:46:54",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "203.130.205.169",
        "port": 3128,
        "type": 1,
        "anonymity": "Low",
        "uptime": 56.68,
        "checked": "2016-12-06T04:45:51",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Indonesia",
          "nameRu": "Индонезия",
          "iso3166a2": "ID"
        }
      },
      {
        "ip": "124.88.67.10",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.3,
        "checked": "2016-12-06T04:44:51",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "92.222.107.62",
        "port": 3128,
        "type": 1,
        "anonymity": "High",
        "uptime": 1.04,
        "checked": "2016-12-06T04:44:51",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Germany",
          "nameRu": "Германия",
          "iso3166a2": "DE"
        }
      },
      {
        "ip": "124.88.67.10",
        "port": 843,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.21,
        "checked": "2016-12-06T04:44:48",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "201.55.143.1",
        "port": 3128,
        "type": 1,
        "anonymity": "Low",
        "uptime": 3.7,
        "checked": "2016-12-06T04:44:42",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Brazil",
          "nameRu": "Бразилия",
          "iso3166a2": "BR"
        }
      },
      {
        "ip": "124.88.67.10",
        "port": 81,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 4.89,
        "checked": "2016-12-06T04:44:27",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "117.74.121.146",
        "port": 80,
        "type": 1,
        "anonymity": "Low",
        "uptime": 3.38,
        "checked": "2016-12-06T04:44:25",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Indonesia",
          "nameRu": "Индонезия",
          "iso3166a2": "ID"
        }
      },
      {
        "ip": "213.192.37.186",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 0.2,
        "checked": "2016-12-06T04:44:20",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Czechia",
          "nameRu": "Чехия",
          "iso3166a2": "CZ"
        }
      },
      {
        "ip": "83.221.208.217",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 1.3,
        "checked": "2016-12-06T04:44:19",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Russia",
          "nameRu": "Россия",
          "iso3166a2": "RU"
        }
      },
      {
        "ip": "124.88.67.83",
        "port": 82,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.22,
        "checked": "2016-12-06T04:44:08",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "103.247.101.102",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 6.93,
        "checked": "2016-12-06T04:43:58",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Indonesia",
          "nameRu": "Индонезия",
          "iso3166a2": "ID"
        }
      },
      {
        "ip": "197.51.39.130",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 7.89,
        "checked": "2016-12-06T04:43:34",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Egypt",
          "nameRu": "Египет",
          "iso3166a2": "EG"
        }
      },
      {
        "ip": "178.32.218.91",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 5.31,
        "checked": "2016-12-06T04:43:12",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "France",
          "nameRu": "Франция",
          "iso3166a2": "FR"
        }
      },
      {
        "ip": "184.49.233.234",
        "port": 8080,
        "type": 1,
        "anonymity": "Medium",
        "uptime": 2.97,
        "checked": "2016-12-06T04:42:41",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "USA",
          "nameRu": "США",
          "iso3166a2": "US"
        }
      },
      {
        "ip": "125.253.125.200",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 3.12,
        "checked": "2016-12-06T04:42:31",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Vietnam",
          "nameRu": "Вьетнам",
          "iso3166a2": "VN"
        }
      },
      {
        "ip": "186.94.250.200",
        "port": 8080,
        "type": 1,
        "anonymity": "High",
        "uptime": 15.29,
        "checked": "2016-12-06T04:42:28",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Venezuela",
          "nameRu": "Венесуэла",
          "iso3166a2": "VE"
        }
      },
      {
        "ip": "113.53.255.196",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 4.89,
        "checked": "2016-12-06T04:41:58",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Thailand",
          "nameRu": "Таиланд",
          "iso3166a2": "TH"
        }
      },
      {
        "ip": "213.130.26.38",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 2.14,
        "checked": "2016-12-06T04:41:23",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Ukraine",
          "nameRu": "Украина",
          "iso3166a2": "UA"
        }
      },
      {
        "ip": "82.114.82.62",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 1.12,
        "checked": "2016-12-06T04:41:13",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Serbia",
          "nameRu": "Сербия",
          "iso3166a2": "rs"
        }
      },
      {
        "ip": "83.241.46.175",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 0.69,
        "checked": "2016-12-06T04:40:49",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Latvia",
          "nameRu": "Латвия",
          "iso3166a2": "LV"
        }
      },
      {
        "ip": "49.231.150.233",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.79,
        "checked": "2016-12-06T04:40:45",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Thailand",
          "nameRu": "Таиланд",
          "iso3166a2": "TH"
        }
      },
      {
        "ip": "112.214.73.253",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 1.25,
        "checked": "2016-12-06T04:40:45",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Korea",
          "nameRu": "Корея",
          "iso3166a2": "KR"
        }
      },
      {
        "ip": "92.222.109.55",
        "port": 3128,
        "type": 1,
        "anonymity": "High",
        "uptime": 1.37,
        "checked": "2016-12-06T04:40:44",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Germany",
          "nameRu": "Германия",
          "iso3166a2": "DE"
        }
      },
      {
        "ip": "92.42.249.229",
        "port": 6666,
        "type": 1,
        "anonymity": "Low",
        "uptime": 5.28,
        "checked": "2016-12-06T04:40:34",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Serbia",
          "nameRu": "Сербия",
          "iso3166a2": "rs"
        }
      },
      {
        "ip": "183.89.57.199",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 7.31,
        "checked": "2016-12-06T04:38:31",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Thailand",
          "nameRu": "Таиланд",
          "iso3166a2": "TH"
        }
      },
      {
        "ip": "120.52.73.98",
        "port": 8086,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 2.26,
        "checked": "2016-12-06T04:38:02",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "120.52.73.97",
        "port": 8086,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 2.35,
        "checked": "2016-12-06T04:37:58",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "218.56.132.156",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 0.49,
        "checked": "2016-12-06T04:37:56",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "120.52.73.98",
        "port": 93,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 3.5,
        "checked": "2016-12-06T04:37:55",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "189.202.216.137",
        "port": 80,
        "type": 1,
        "anonymity": "Low",
        "uptime": 1.46,
        "checked": "2016-12-06T04:37:54",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Mexico",
          "nameRu": "Мексика",
          "iso3166a2": "MX"
        }
      },
      {
        "ip": "120.52.73.98",
        "port": 90,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.31,
        "checked": "2016-12-06T04:37:48",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "120.52.73.98",
        "port": 100,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.74,
        "checked": "2016-12-06T04:37:47",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "120.52.73.98",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 1.21,
        "checked": "2016-12-06T04:37:42",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "120.52.73.98",
        "port": 8090,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.32,
        "checked": "2016-12-06T04:37:41",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "124.88.67.14",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.19,
        "checked": "2016-12-06T04:37:39",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "124.88.67.19",
        "port": 83,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.22,
        "checked": "2016-12-06T04:37:39",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "120.52.73.98",
        "port": 8081,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 1.06,
        "checked": "2016-12-06T04:37:39",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "95.170.222.106",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 1.97,
        "checked": "2016-12-06T04:37:33",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Iraq",
          "nameRu": "Ирак",
          "iso3166a2": "IQ"
        }
      },
      {
        "ip": "120.52.73.97",
        "port": 8080,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.36,
        "checked": "2016-12-06T04:37:32",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "212.80.167.93",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.71,
        "checked": "2016-12-06T04:37:31",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Spain",
          "nameRu": "Испания",
          "iso3166a2": "ES"
        }
      },
      {
        "ip": "120.52.73.98",
        "port": 98,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.4,
        "checked": "2016-12-06T04:37:31",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "211.170.156.163",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.23,
        "checked": "2016-12-05T16:48:50",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Korea",
          "nameRu": "Корея",
          "iso3166a2": "KR"
        }
      },
      {
        "ip": "202.102.58.230",
        "port": 80,
        "type": 1,
        "anonymity": "Low",
        "uptime": 0.14,
        "checked": "2016-12-05T05:08:31",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "202.138.240.195",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 15.5,
        "checked": "2016-12-05T05:06:44",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Indonesia",
          "nameRu": "Индонезия",
          "iso3166a2": "ID"
        }
      },
      {
        "ip": "157.7.137.74",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.3,
        "checked": "2016-12-05T05:05:14",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Japan",
          "nameRu": "Япония",
          "iso3166a2": "JP"
        }
      },
      {
        "ip": "202.43.73.12",
        "port": 80,
        "type": 1,
        "anonymity": "Low",
        "uptime": 0.24,
        "checked": "2016-12-04T17:01:40",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Indonesia",
          "nameRu": "Индонезия",
          "iso3166a2": "ID"
        }
      },
      {
        "ip": "108.171.249.138",
        "port": 80,
        "type": 1,
        "anonymity": "High",
        "uptime": 0.22,
        "checked": "2016-12-03T17:06:27",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "USA",
          "nameRu": "США",
          "iso3166a2": "US"
        }
      },
      {
        "ip": "111.68.99.57",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 8.48,
        "checked": "2016-12-03T16:48:30",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Pakistan",
          "nameRu": "Пакистан",
          "iso3166a2": "PK"
        }
      },
      {
        "ip": "46.218.85.101",
        "port": 3129,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 2.5,
        "checked": "2016-12-03T05:08:54",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "France",
          "nameRu": "Франция",
          "iso3166a2": "FR"
        }
      },
      {
        "ip": "124.88.67.81",
        "port": 843,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.24,
        "checked": "2016-12-03T04:57:59",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "103.28.225.180",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 5.16,
        "checked": "2016-12-03T04:45:59",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Indonesia",
          "nameRu": "Индонезия",
          "iso3166a2": "ID"
        }
      },
      {
        "ip": "183.61.236.55",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.34,
        "checked": "2016-12-03T04:40:11",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "50.30.152.130",
        "port": 8086,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 1.58,
        "checked": "2016-12-03T04:39:42",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "USA",
          "nameRu": "США",
          "iso3166a2": "US"
        }
      },
      {
        "ip": "88.149.221.35",
        "port": 80,
        "type": 1,
        "anonymity": "High",
        "uptime": 0.07,
        "checked": "2016-12-03T04:20:34",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Italy",
          "nameRu": "Италия",
          "iso3166a2": "IT"
        }
      },
      {
        "ip": "118.189.157.9",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 9.36,
        "checked": "2016-12-03T04:19:44",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "79.129.56.159",
        "port": 8080,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 7.55,
        "checked": "2016-12-03T04:09:37",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Greece",
          "nameRu": "Греция",
          "iso3166a2": "GR"
        }
      },
      {
        "ip": "125.253.122.110",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 1.29,
        "checked": "2016-12-03T04:08:35",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Vietnam",
          "nameRu": "Вьетнам",
          "iso3166a2": "VN"
        }
      },
      {
        "ip": "42.118.216.219",
        "port": 3128,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.19,
        "checked": "2016-12-02T17:14:38",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Vietnam",
          "nameRu": "Вьетнам",
          "iso3166a2": "VN"
        }
      },
      {
        "ip": "86.100.118.44",
        "port": 80,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 0.85,
        "checked": "2016-12-02T17:11:05",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Lithuania",
          "nameRu": "Литва",
          "iso3166a2": "LT"
        }
      },
      {
        "ip": "92.51.133.3",
        "port": 3128,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 0.33,
        "checked": "2016-12-02T17:04:23",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Germany",
          "nameRu": "Германия",
          "iso3166a2": "DE"
        }
      },
      {
        "ip": "60.250.81.118",
        "port": 80,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 12.49,
        "checked": "2016-12-02T17:01:35",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Taiwan",
          "nameRu": "Тайвань",
          "iso3166a2": "TW"
        }
      },
      {
        "ip": "124.88.67.54",
        "port": 843,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.2,
        "checked": "2016-12-02T16:57:28",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "124.88.67.20",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.23,
        "checked": "2016-12-02T16:55:18",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "107.151.152.212",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.19,
        "checked": "2016-12-02T16:53:59",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "USA",
          "nameRu": "США",
          "iso3166a2": "US"
        }
      },
      {
        "ip": "119.105.177.105",
        "port": 8118,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 4.33,
        "checked": "2016-12-02T16:52:08",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Japan",
          "nameRu": "Япония",
          "iso3166a2": "JP"
        }
      },
      {
        "ip": "93.64.156.3",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 12.26,
        "checked": "2016-12-02T16:50:16",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Italy",
          "nameRu": "Италия",
          "iso3166a2": "IT"
        }
      },
      {
        "ip": "107.191.61.167",
        "port": 81,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.23,
        "checked": "2016-12-02T16:49:11",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "USA",
          "nameRu": "США",
          "iso3166a2": "US"
        }
      },
      {
        "ip": "107.170.111.66",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.1,
        "checked": "2016-12-02T16:48:55",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "USA",
          "nameRu": "США",
          "iso3166a2": "US"
        }
      },
      {
        "ip": "66.162.122.25",
        "port": 8080,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 2.14,
        "checked": "2016-12-02T16:48:30",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "USA",
          "nameRu": "США",
          "iso3166a2": "US"
        }
      },
      {
        "ip": "87.244.181.185",
        "port": 8080,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 5.76,
        "checked": "2016-12-02T16:48:00",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Ukraine",
          "nameRu": "Украина",
          "iso3166a2": "UA"
        }
      },
      {
        "ip": "138.201.63.123",
        "port": 31288,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 7.14,
        "checked": "2016-12-02T16:45:40",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Germany",
          "nameRu": "Германия",
          "iso3166a2": "DE"
        }
      },
      {
        "ip": "202.117.10.65",
        "port": 1080,
        "type": 12,
        "anonymity": "HighKeepAlive",
        "uptime": 0.28,
        "checked": "2016-12-02T16:44:10",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "92.42.163.198",
        "port": 3128,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 3.75,
        "checked": "2016-12-02T16:44:06",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Russia",
          "nameRu": "Россия",
          "iso3166a2": "RU"
        }
      },
      {
        "ip": "184.172.104.35",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.15,
        "checked": "2016-12-02T16:43:49",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "USA",
          "nameRu": "США",
          "iso3166a2": "US"
        }
      },
      {
        "ip": "193.84.184.25",
        "port": 8080,
        "type": 2,
        "anonymity": "HighKeepAlive",
        "uptime": 1.98,
        "checked": "2016-12-02T16:35:13",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Latvia",
          "nameRu": "Латвия",
          "iso3166a2": "LV"
        }
      },
      {
        "ip": "89.250.207.195",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.04,
        "checked": "2016-12-02T16:27:39",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Poland",
          "nameRu": "Польша",
          "iso3166a2": "PL"
        }
      },
      {
        "ip": "124.133.230.254",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.14,
        "checked": "2016-12-02T16:22:21",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "107.151.136.194",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 0.18,
        "checked": "2016-12-02T16:10:38",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "USA",
          "nameRu": "США",
          "iso3166a2": "US"
        }
      },
      {
        "ip": "112.64.185.73",
        "port": 80,
        "type": 1,
        "anonymity": "High",
        "uptime": 0.24,
        "checked": "2016-12-02T04:26:51",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "223.19.212.121",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 1.01,
        "checked": "2016-12-02T04:09:45",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Honkong",
          "nameRu": "Гонконг",
          "iso3166a2": "HK"
        }
      },
      {
        "ip": "95.107.161.221",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 0.12,
        "checked": "2016-12-01T16:01:05",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Albania",
          "nameRu": "Албания",
          "iso3166a2": "AL"
        }
      },
      {
        "ip": "58.67.147.201",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 0.74,
        "checked": "2016-12-01T05:00:03",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "China",
          "nameRu": "Китай",
          "iso3166a2": "CN"
        }
      },
      {
        "ip": "200.27.114.228",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 0.52,
        "checked": "2016-12-01T04:42:49",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Chili",
          "nameRu": "Чили",
          "iso3166a2": "CL"
        }
      },
      {
        "ip": "89.108.165.187",
        "port": 8080,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 47.4,
        "checked": "2016-12-01T04:32:40",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Lebanon",
          "nameRu": "Ливан",
          "iso3166a2": "LB"
        }
      },
      {
        "ip": "217.23.90.10",
        "port": 8080,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 2.63,
        "checked": "2016-12-01T04:30:16",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Russia",
          "nameRu": "Россия",
          "iso3166a2": "RU"
        }
      },
      {
        "ip": "202.137.6.90",
        "port": 8080,
        "type": 1,
        "anonymity": "Low",
        "uptime": 8.27,
        "checked": "2016-12-01T04:29:25",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "Indonesia",
          "nameRu": "Индонезия",
          "iso3166a2": "ID"
        }
      },
      {
        "ip": "202.56.203.40",
        "port": 80,
        "type": 1,
        "anonymity": "HighKeepAlive",
        "uptime": 11.01,
        "checked": "2016-12-01T04:28:43",
        "available": "Yes",
        "free": "Yes",
        "country": {
          "nameEn": "India",
          "nameRu": "Индия",
          "iso3166a2": "IN"
        }
      }
    ]


#proxy_list = [{'http': ''}]
proxy_list = open('us-proxy.txt', 'r').read().split('\n')
print(proxy_list)


'''
main_page = 'http://rutor.info'

deque = {
    'http://rutor.info': False,
    'http://rutor.info/top': False,
    'http://rutor.info/categories': False,
    'http://rutor.info/browse/': False
}
'''
main_page = 'http://extratorrent.cc'

deque = {
    'http://extratorrent.cc': False,
}

while True:
    # print(deque)
    page = random.choice(list(deque.keys()))
    if not deque[page]:
        print(page)
        try:
            rnd_prox = random.choice(proxy_list)
            # proxies = {'http:' '{}:{}'.format(rnd_prox['ip'], rnd_prox['port'])}
            proxies = {'http:': ''}

            resp = r.get(page, headers=headers, proxies=proxies)
            if resp.status_code == 200:
                #print(resp.text)
                deque[page] = True
            else:
                print(resp.status_code)
            # links = rutor_to_torrent(resp.text)
            links = extratorrent_to_torrent(resp.text)

            for i in links:
                page_insert = main_page + i
                # print(page_insert)

                if page_insert not in deque:
                    deque[page_insert] = False

        except Exception as e:
            print(e)