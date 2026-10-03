### Application uploads cat images from https://cataas.com/ with your own text to your Yandex Disk (https://360.yandex.ru/disk/), and also creates a JSON file with names and sizes of the uploaded cat images.

#### Application needs an OAuth token from https://yandex.ru/dev/disk/poligon/
#### This token should be placed in the variable "token" in module "settings.py" (as shown by the module "settings.example.py".

#### A folder for these cat images on your Yandex Disk is created by the application. The folder name is contained in the global variable "study_group_name".

#### The command "YD = YandexDisk(token)" creates an object "YD" of the "YandexDisk" class (with a "token" parameter), which allows you to use its methods.

#### The method "YD.create_folder(study_group_name)" creates a folder with a name "study_group_name".

#### The method "upload_files_to_folder(self, folder_name)" is a loop that asks you to enter a text (that will be attached to a random cat image) or a number 0 (to exit the loop). The cat image file with your text in it is uploaded to the aforementioned folder in your Yandex Disk. The file name (without its extension) is the text that you entered. If a name of a new file will match exactly (including its extension) a name of a file already existing in this folder of your Yandex Drive, the program will ask you to enter another text.

#### The method "upload_files_to_folder(self, folder_name)" calls a static method "get_cat_file_info(file_name, file_extension, image_size)", which is responsible for creating and modifying a JSON file with names and sizes of the files uploaded to the aforementioned folder in your Yandex Disk. The parameters of this static method are all the "String" type. The name of JSON file is "image_size_data.json"

#### Application informs you about successful (or not) execution of all important steps.
