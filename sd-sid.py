import urllib.request
from bs4 import BeautifulSoup
import time
import os

def specify_img_filetype(content):
    if content[:4] == b"\xff\xd8\xff\xdb" or content[:4] == b"\xff\xd8\xff\xe0" or content[:4] == b"\xff\xd8\xff\xee" or content[:4] == b"\xff\xd8\xff\xe1":
        return "jpg"
    elif content[:8] == b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a":
        return "png"
    elif content[:6] == b"\x47\x49\x46\x38\x37\x61" or content[:6] == b"\x47\x49\x46\x38\x39\x61":
        return "gif"
    elif content[:2] == b"\x42\x4d":
        return "bmp"
    else:
        return ""

def main():
    url = input("SpeakerDeck slide URL->")
    dir_name = input("Output directory name->")
    os.makedirs(dir_name, exist_ok=True)
    
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    slide_part = soup.find("div", class_="sd-player-slides js-sd-player-slides")
    if(slide_part):
        slide_divs = slide_part.findAll("div", class_="sd-player-slide js-sd-slide")
        slide_urls = [slide_div['data-url'] for slide_div in slide_divs]
        slide_total = len(slide_urls)

        file_number = 0
        for slide_url in slide_urls:
            slide_img = urllib.request.urlopen(slide_url).read()
            ext = specify_img_filetype(slide_img)
            with open("%s/%05d.%s" % (dir_name, file_number, ext), "wb") as img_file:
                img_file.write(slide_img)
            file_number += 1
            print("[+] saved %d/%d slides." % (file_number, slide_total))
            time.sleep(1)

        input("[+] All slides are saved. press enter to exit.")

if __name__ == "__main__":
    main()