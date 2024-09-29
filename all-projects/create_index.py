import os



# This program generates index.html automatically by scanning the subfolders in the 'projects' folder.
# The program checks for 'name.txt', reads and displays the name of the project from 'name.txt' and creates a button
# that points to index.html.



projects_dir = "projects"
print("Listing subfolders names in 'projects' directory...")
subfolders_names = [name for name in os.listdir(projects_dir) if os.path.isdir(os.path.join(projects_dir, name))]
print("Sorting subfolders names...")
subfolders_names.sort()
print("Generating paths to subfolders from subfolders names...")
subfolders_paths = []
for name in subfolders_names:
    subfolders_paths.append(os.path.join(projects_dir, name))

print("Creating index.html file...")
with open("index.html", 'w') as html_file:
    print("Writing to index.html...")
    html_file.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Archives - CodeRapids</title>
    <meta name="description" content="Download my archived content for FREE!">
    <link rel="stylesheet" href="../color-palette.css">
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="assets/main_icon.png" type="image/x-icon">
</head>
<body>
    <div class="header">
        <p class="title">Archives</p>
        <a href="../index.html">
            <button class='home-btn'>Back to Home</button>
        </a>
    </div>
    <div class='download-items'>
''')

    i = 0
    for path in subfolders_paths:
        html_file.write('''

        <div class='download-item'>
''')
        path_to_svg_file = os.path.join(subfolders_paths[i], "img.svg")
        if os.path.isfile(path_to_svg_file):
            html_file.write(f'''
            <img data-src="{path_to_svg_file}" alt="Icon." class="item-img">
''')
            print(f"Added the icon element for '{subfolders_names[i]}'.")
        else:
            print(f"Unable to find img.svg for '{subfolders_names[i]}'. Searching for img.png instead...")
            path_to_png_file = os.path.join(subfolders_paths[i], "img.png")
            if os.path.isfile(path_to_png_file):
                html_file.write(f'            <img data-src="{path_to_png_file}" alt="Thumbnail." class="item-img">\n')
                print("img.png file have been added.")
            else:
                print("img.svg and img.png not found.")
                html_file.write(f'            <img data-src="assets/no_image.png" alt="No image available." class="item-img">\n')
        project_name = "Name Unavailable"
        try:
            with open(os.path.join(subfolders_paths[i], "name.txt"), 'r') as name_file:
                project_name = name_file.read()
            print(f"Name for '{subfolders_names[i]}' has been successfully read.")
        except:
            project_name = "Name Unavailable"
            print(f"Unable to find name.txt for '{subfolders_paths[i]}'.")
        html_file.write(f'''
            <a href="{os.path.join(path, "file.zip")}" class="item-a" download>{project_name}</a>
        </div>
''')
        i += 1
    html_file.write("    </div>\n")
    print("All projects have been listed. Adding a reference to script.js...")
    html_file.write('    <script src="script.js"></script>\n')
    print("Closing the body and html tags...")
    html_file.write("</body>\n")
    html_file.write("</html>\n")
print("'index.html' has been successfully created and written.")
    