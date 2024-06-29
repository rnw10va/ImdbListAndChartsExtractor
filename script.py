# -*- coding: utf-8 -*-
listLength=
webPage="""

"""
tempSplit=webPage.split("\"name\":\"")
for showOrMovie in tempSplit[1:listLength+1]:
    print(showOrMovie.split("\",\"description\":\"")[0])
