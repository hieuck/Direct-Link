import re

def main():
    links = []
    input_source = input("Enter 'f' to read from a file or 't' to type the link (or press enter to quit): ")

    while input_source not in ["f", "F", "t", "T", ""]:
        print("Invalid input. Please try again.")
        input_source = input("Enter 'f' to read from a file or 't' to type the link (or press enter to quit): ")
    
    if input_source in ["f","F"]:
        try:
            with open("input.txt", "r") as f:
                links = f.readlines()
            links = [x.strip() for x in links]
        except:
            # Go to typing link mode
            input_source = "t"
            print("Could not find input.txt. Please enter the link instead.")
    
    if input_source in ["t", "T"]:
        while True:
            link = input("Enter the link (or press enter to quit): ")
            if link == "":
                break
            links.append(link)
    else:
        return

    new_links = []
    for link in links:
        new_link_o = new_links_ob = new_link_d = new_link_g = None
        if "onedrive.live.com" in link:
            if re.search(r"https://.*width=", link):
                new_link_o = re.sub(r"embed", "download", re.search(r"https://.*width=", link).group())
                new_link_o = new_link_o.rstrip("\" width=")
        elif "my.sharepoint.com" in link:
            if re.search(r"https://.*\?", link):
                new_links_ob = re.search(r"https://.*\?", link).group()
                new_links_ob = new_links_ob + "download=1"
        elif "www.dropbox.com" in link:
            new_link_d = link.replace("www.dropbox.com", "dl.dropboxusercontent.com")
        elif "drive.google.com" in link:
            google_drive_link = re.search(r"https://drive.google.com/file/d/(.*)/view", link)
            if google_drive_link:
                new_link_g = "https://drive.google.com/uc?export=download&id=" + google_drive_link.group(1)

        if new_link_o or new_links_ob or new_link_d or new_link_g:
            new_links.append(new_link_o or new_links_ob or new_link_d or new_link_g)
        else:
            print(f"{link} is not a link from OneDrive, OneDrive for Business, Dropbox, or Google Drive.")

    if new_links:
        print("\n".join(new_links))
        input("Press enter to write to output.txt and quit.")
        try:
            with open("output.txt", "w") as f:
                for l in new_links:
                    f.write(l + "\n")
        except:
            print("An error occurred while opening the file. Exiting.")
            exit()
    else:
        print("No links found.")

if __name__ == "__main__":
    main()
