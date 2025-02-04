import zipfile

# Define ZIP file path
zip_file_path = '/home/ubuntu/apache-tomcat-10.1.34.zip'
extract_path = '/home/ubuntu/'  # Destination folder

try:
    # Open and list contents of the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        print("Contents of the ZIP file:")
        print(zip_ref.namelist())  # List files inside ZIP

        # Extracting all files
        zip_ref.extractall(extract_path)
        print("Files extracted successfully to:", extract_path)

except zipfile.BadZipFile:
    print("Error: The file is not a valid ZIP archive.")
except FileNotFoundError:
    print("Error: ZIP file not found.")

