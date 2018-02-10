#!/usr/bin/python3
# -*- coding: utf-8 -*-

import facebook
import urllib.request

graph = facebook.GraphAPI("EAADoYtPTzfoBABzTAZCcbG1axEE1SZBZAcStNx1nE2cJjD2VGSqyvJdIhwPlgxYZAQdKEG0mZAlk5bZBmONX4vtRT2KiASiPFfDhZA2AEVkaQbxVNOGPsph6Va3TGPeCqCEHO46xFinmMW6GQ0EXYczq7JZBfQrjtEw4yozDYpttDQZDZD")
resp = graph.get_object("267880096651225/?fields=videos{source}")

num = 0
for entry in resp["videos"]["data"]:
    vid_url = entry["source"]
    num += 1
    print(vid_url)
    urllib.request.urlretrieve(vid_url, "./video" + "{0:03d}".format(num) + ".mp4")
print("動画を保存しました")
