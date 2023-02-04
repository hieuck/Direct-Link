import re

def main():
    links = []
    input_source = input("Enter 'f' to read from a file or press enter to type the link: ")
    if input_source == "f":
        with open("input.txt", "r") as f:
            links = f.readlines()
        links = [x.strip() for x in links]
    else:
        while True:
            link = input("Enter the link (or press enter to quit): ")
            if link == "":
                break
            links.append(link)

    new_links = []
    for link in links:
        if "onedrive.live.com" in link:
            new_link_o = ""
            if re.search(r"https://.*width=", link):
                new_link_o = re.sub(r"embed", "download", re.search(r"https://.*width=", link).group())
                new_link_o = new_link_o.rstrip("\" width=")
            new_links.append(new_link_o)
        elif "www.dropbox.com" in link:
            new_link_d = link.replace("www.dropbox.com", "dl.dropboxusercontent.com")
            new_links.append(new_link_d)
        elif "drive.google.com" in link:
            google_drive_link = re.search(r"https://drive.google.com/file/d/(.*)/view", link)
            if google_drive_link:
                new_link_g = "https://drive.google.com/uc?export=download&id=" + google_drive_link.group(1)
                new_links.append(new_link_g)

    with open("output.txt", "w") as f:
        for l in new_links:
            f.write(l + "\n")
    print("Done!")

if __name__ == "__main__":
    main()
