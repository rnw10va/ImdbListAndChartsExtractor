# -*- coding: utf-8 -*-
listLength=
webPage="""

"""
tempSplit=webPage.split("\"originalTitleText\":\"")
for showOrMovie in tempSplit[1:listLength+1]:
    print(showOrMovie.split("\",\"plot\":\"")[0])
