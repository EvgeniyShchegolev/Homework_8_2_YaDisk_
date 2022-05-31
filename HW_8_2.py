import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.headers = {"Authorization": f"OAuth {self.token}", "Content-Type": "application/json"}
        self.path_disk_files = 'https://cloud-api.yandex.net/v1/disk/resources'

    def _get_link_upload(self, file_path):
        name_file = file_path.split('\\')[-1]
        params = {"path": f"/{name_file}", "overwrite": "true"}
        response = requests.get(url=f"{self.path_disk_files}/upload", headers=self.headers, params=params)
        data = response.json()
        return data["href"]

    def upload(self, file_path: str):
        href_link = self._get_link_upload(file_path)
        res = requests.put(href_link, data=open(file_path, "rb"))
        res.raise_for_status()
        if res.status_code == 201:
            print('Success')


if __name__ == '__main__':
    API_TOKEN = ''
    path_to_file = os.path.join(os.getcwd(), 'test_file.txt')
    uploader = YaUploader(API_TOKEN)
    uploader.upload(path_to_file)
