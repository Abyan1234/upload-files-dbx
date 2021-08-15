import dropbox 
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to,local_path):
        
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            relative_path= os.path.relpath(local_path,file_from)
            dropbox_path= os.path.join(file_to,relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A2O83YjIi9qL9hwD5tM6Cw7NG0nOzjPMPCwXnZv4RAzjKK4kOnM0voI2-jkZ0AkSVrQR2R5gbnipwwtf6qKuuEYKTaV99-hNd0CyiWWqDbd3RKMjy5Dt4gbLHfeS7g7cFyPdo_E'
    transferData = TransferData(access_token)

    file_from =input("Enter the file name to transfer:- ")
    file_to =input("Enter the full path to upload to dropbox:- ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()