import requests
import tarfile

source_url = "https://downloads.apache.org/tomcat/tomcat-10/v10.1.34/bin/apache-tomcat-10.1.34.tar.gz.asc"

file_path = "/home/ubuntu/apache-tomcat-10.1.34.tar.gz"
response = requests.get(source_url, stream = True)

with open(file_path, "wb") as file:
    file.write(response.content)

print(f"Tar file downloaded successfully:")

file = tarfile.open("/home/ubuntu/apache-tomcat-10.1.34.tar.gz")
file.extractall("/home/ubuntu/")
