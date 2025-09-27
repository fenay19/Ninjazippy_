# Ninjazippy_

# NinjaZipPy

**NinjaZipPy** is a Python CLI utility for compressing and extracting `.7z` archives. It allows you to zip files or folders and unzip them into a desired location with simple commands.

---

## Sample Data and Workflow

1. **Sample Folder**
- The folder `sample_folder` contains several `.txt` files with sample content:
  - `gen_ai.txt` – essay on Generative AI  
  - `harry_potter.txt` – essay on Harry Potter  
  - `space_exploration.txt` – essay on space exploration  

2. **Zipping the Sample Folder**

ninjazippy zip my_archive.7z sample_folder

3. **Zipping Specific Files**

ninjazippy zip my_archive.7z file1.txt file2.txt

Creates an archive with only the specified files.

4. **Unzipping into a Specific Folder**

ninjazippy unzip my_archive.7z -d extracted


Extracts all files into the folder extracted.

This shows that my_archive.7z is converted into the extracted folder, preserving folder structure and file contents.

5. Features
Compress files or folders into .7z archives.

Extract .7z archives to any directory.

Works from the terminal on Unix/Linux and Windows.

Lightweight Python package using py7zr for 7zip compression.

usage example:
# Zip a folder
ninjazippy zip my_archive.7z sample_folder

# Unzip to current folder
ninjazippy unzip my_archive.7z

# Unzip to a specific folder
ninjazippy unzip my_archive.7z -d extracted
