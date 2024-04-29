import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
file_id_master_list = []
file_title_master_list = []
file_name_master_list = []
file_type_master_list = []
file_category_master_list = []

def remove_space_title_case(input_string):
    return ' '.join(input_string.split()).title()


def getGDriveTitle(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title= soup.findAll('title')[0].text
        return title
    except:
        return Exception
        "Error occured"

def getFileID(url):
    url_parts = url.split("/")
    if len(url_parts) < 6:
        return "Error"
    return url_parts[5]

def getFileNameAndExtension(gDriveTitle):
    gDriveTitle = gDriveTitle.replace(" - Google Drive", "")
    file_info = gDriveTitle.split(".")
    return remove_space_title_case(file_info[0]), file_info[1]

def getFileTitle(gdrive_file_name):
    if ("(" in gdrive_file_name) and ('Sipara' not in gdrive_file_name):
        gdrive_file_name = gdrive_file_name.split("(")[0]
        return remove_space_title_case(gdrive_file_name)
    else:
        return remove_space_title_case(gdrive_file_name)

def getAllDetails(url):
    gdrive_file_id = getFileID(url)
    gdrive_title = getGDriveTitle(url)
    gdrive_file_name, gdrive_file_extension = getFileNameAndExtension(gdrive_title)
    gdrive_file_title = getFileTitle(gdrive_file_name)
    data_object = {
        "file_id": gdrive_file_id,
        "file_title": gdrive_file_title,
        "file_name": gdrive_file_name,
        }
    if gdrive_file_extension == 'mp3':
        data_object['file_type'] = 'Audio'
    elif gdrive_file_extension == 'pdf':
        data_object['file_type'] = 'PDF'
    else:
        data_object['file_type'] = f'Unknown {gdrive_file_extension}'
    return data_object

# link = 'https://drive.google.com/file/d/1p9EREjGKyJf3-wM6dwqAzMVAbHegii3i/view?usp=sharing'
# print(getAllDetails(link))

# directory_paths = ['./text_files/Audio/','./text_files/PDF/']
# for directory_path in directory_paths:
#     text_file_names = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
#     text_file_names.sort()
#     for text_file_name in text_file_names:
#         text_file_path = f'{directory_path}{text_file_name}'
#         file_text = open(text_file_path,"r")
#         text_file_data = file_text.read()
#         text_file_data_list = text_file_data.split(", ")
#         file_text.close()
#         for urls in text_file_data_list:
#             try:
#                 file_info = getAllDetails(urls)
#                 file_id_master_list.append(file_info['file_id'])
#                 file_title_master_list.append(file_info['file_title'])
#                 file_name_master_list.append(file_info['file_name'])
#                 file_type_master_list.append(file_info['file_type'])
#                 file_category_master_list.append(text_file_name)
#                 print(file_info)
#             except:
#                 print("** Error **")
#                 print(f"some error occured, url: {urls}, text_file_name: {text_file_name}")
#                 print("** Error **")

#         dict = {
#         "file_id_master_list":file_id_master_list,
#         "file_title_master_list":file_title_master_list,
#         "file_name_master_list":file_name_master_list,
#         "file_type_master_list":file_type_master_list,
#         "file_category_master_list":file_category_master_list,
#         }
#         df = pd.DataFrame(dict)
#         df.to_csv("Master_data.csv")
#         print(f"fininshed processing file {text_file_path}")
