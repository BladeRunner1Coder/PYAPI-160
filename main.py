import sys
import requests
import json
import os
from settings import token


study_group_name = "PYAPI-160"

class YandexDisk:
    urlYD = "https://cloud-api.yandex.net"

    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"OAuth {self.token}"}

    def create_folder(self, folder_name):
        response = requests.put(self.urlYD + "/v1/disk/resources/" + f"?path=%2F{folder_name}", headers=self.headers)
        if response.status_code == 201:
            print(f"Folder {folder_name} was created successfully!")
        elif response.status_code == 409:
            print(f"Folder {folder_name} already exists!")
        else:
            print(f"Folder {folder_name} was not created: {response.status_code}")
            print(response.json()["message"])
            sys.exit(0)

    def upload_files_to_folder(self, folder_name):
        url_cat = "https://cataas.com/cat/says/"
        while True:
            file_name = input("Enter your text (0 for exit), but keep in mind that the" +
                              "\n"+ "entire file path must be strictly under 250 characters: ")
            if file_name == "0":
                print("Application closed successfully!")
                sys.exit(0)
            response = requests.get(url_cat + file_name)
            if response.status_code == 200:
                print("Request for a cat image file with text was successful!")
            else:
                print(f"Request for a cat image file with text was not successful: {response.status_code}")
                print(response.json()["message"])
                sys.exit(0)
            file_extension = response.headers["content-type"].split('/')[1]
            image_size = response.headers["content-length"]
            response2 = requests.get(
                self.urlYD + "/v1/disk/resources/upload" + f"?path=%2F{folder_name}%2F{file_name}.{file_extension}",
                headers=self.headers)
            if response2.status_code == 200:
                print(f"Link to upload file {file_name}.{file_extension} received successfully!")
            elif response2.status_code == 409:
                print(f"File {file_name}.{file_extension} already exists!")
                print("Enter another text!")
                continue
            else:
                print(f"Error: {response2.status_code}")
                print(response2.json()["message"])
                print("Enter another text!")
                sys.exit(0)
            path = response2.json()["href"]
            response3 = requests.put(path, response.content)
            if response3.status_code == 201:
                print(f"File {file_name}.{file_extension} uploaded successfully!")
            else:
                print(f"Loading error: {response3.status_code}")
                print(response3.json())
                print(response3.json()["message"])
                sys.exit(0)
            self.get_cat_file_info(file_name, file_extension, image_size)

    @staticmethod
    def get_cat_file_info(file_name, file_extension, image_size):
        data = {
            f"{file_name}.{file_extension}": image_size
        }
        file_exists = os.path.exists("image_size_data.json")
        if not file_exists:
            image_size_data = {}
            initial_data = {
                "Cat picture file name": "Size in bytes"
            }
            image_size_data.update(initial_data)
            image_size_data.update(data)
            with open("image_size_data.json", "w", encoding="utf-8") as file:
                json.dump(image_size_data, file, ensure_ascii=False, indent=4)
        else:
            with open("image_size_data.json", "r", encoding="utf-8") as file:
                image_size_data = json.load(file)
                image_size_data.update(data)
            with open("image_size_data.json", "w", encoding="utf-8") as file:
                json.dump(image_size_data, file, ensure_ascii=False, indent=4)


YD = YandexDisk(token)

YD.create_folder(study_group_name)

YD.upload_files_to_folder(study_group_name)
