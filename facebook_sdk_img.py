#!/usr/bin/python3
# -*- coding: utf-8 -*-

import facebook
import urllib.request

graph = facebook.GraphAPI("EAADoYtPTzfoBABzTAZCcbG1axEE1SZBZAcStNx1nE2cJjD2VGSqyvJdIhwPlgxYZAQdKEG0mZAlk5bZBmONX4vtRT2KiASiPFfDhZA2AEVkaQbxVNOGPsph6Va3TGPeCqCEHO46xFinmMW6GQ0EXYczq7JZBfQrjtEw4yozDYpttDQZDZD")
resp = graph.get_object("267880096651225_1266304763475415/attachments")

num = 0
for entry in resp["data"][0]["subattachments"]["data"]:
    img_url = entry["media"]["image"]["src"]
    num += 1
    print(img_url)
    urllib.request.urlretrieve(img_url, "./image" + "{0:03d}".format(num) + ".jpg")
print("画像を保存しました。")
