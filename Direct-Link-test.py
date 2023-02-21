import re

# Main Function
def main():
    links = []                                              # Initialize a list to store the links
    input_source = input("Enter 'f' to read from a file or 't' to type the link (or press enter to quit): ")   # Prompt the user for an input source

    while input_source not in ["f", "F", "t", "T", ""]:     # Check if an valid input has been received
        print("Invalid input. Please try again.")
        input_source = input("Enter 'f' to read from a file or 't' to type the link (or press enter to quit): ")   # Prompt the user for another input source

    if input_source in ["f","F"]:                        # Handle reading from a file
        try:
            with open("input.txt", "r") as f:             # Attempt to open the file
                links = f.readlines()                      # Store each line of the file into our list
            links = [x.strip() for x in links]            # Remove whitespaces and newline characters
        except:                                           # In case of exception
            # Go to typing link mode
            input_source = "t"
            print("Could not find input.txt. Please enter the link instead.")
    
    if input_source in ["t", "T"]:                        # Handle manually entering links
        while True:
            link = input("Enter the link (or press enter to quit): ")    # Request for each link
            if link == "":                                              # Break on empty link
                break
            links.append(link)                                          # Append valid link to our list
    else:
        return                                                         # Quit program

    new_links = []                                                     # Initialize a list to store the processed links
    for link in links:
        new_link_o = new_links_ob = new_link_d = new_link_g = None      # Initialize variables to store the processed versions
        if "onedrive.live.com" in link:
            if re.search(r"https://.*width=", link):                    # Check for OneDrive links
                new_link_o = re.sub(r"embed", "download", re.search(r"https://.*width=", link).group())   # Process the link
                new_link_o = new_link_o.rstrip("\" width=")                                                # Remove additional trailing text
        elif "my.sharepoint.com" in link:
            if re.search(r"https://.*\?", link):                        # Check for OneDrive for Business links
                new_links_ob = re.search(r"https://.*\?", link).group()  # Process the link
                new_links_ob = new_links_ob + "download=1"               # Append "download=1" to the end of the URL
        elif "www.dropbox.com" in link:
            new_link_d = link.replace("www.dropbox.com", "dl.dropboxusercontent.com")   # Process Dropbox links
        elif "drive.google.com" in link:
            google_drive_link = re.search(r"https://drive.google.com/file/d/(.*)/view", link)    # Try searching for Google Drive links
            if google_drive_link:
                new_link_g = "https://drive.google.com/uc?export=download&id=" + google_drive_link.group(1) # Process the link

        if new_link_o or new_links_ob or new_link_d or new_link_g:
            new_links.append(new_link_o or new_links_ob or new_link_d or new_link_g)   # Append the new link, if one exists
        else:
            print(f"{link} is not a link from OneDrive, OneDrive for Business, Dropbox, or Google Drive.")

    if new_links:                                           # If new links were found
        print("\n".join(new_links))                         # Print the new links
        input("Press enter to write to output.txt and quit.")
        try:
            with open("output.txt", "w") as f:              # Attempt to open output.txt for writing
                for l in new_links:                         # Iterate through all the new links
                    f.write(l + "\n")
        except:
            print("An error occurred while opening the file. Exiting.")
            exit()
    else:
        print("No links found.")

if __name__ == "__main__":
    main()
