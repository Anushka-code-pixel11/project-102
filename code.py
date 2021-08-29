#im creating how to upload files from your pc to dropbox with code because it makes our task much easier
#and we dont have to do all the step 

import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    #you can enter your own access token here to check if its working
    access_token = "sl.A3cqHI-HCBowKhXMKBMAT_um3wzYkJCW7TF6PU03LOiNfy-Yv8szcMA_lOKmI60NqwWu5eTKVpuDSx15PXsbfj0ODsgysl4s3qgMXe__bfqukVWb9aezIxCOcCsVC1w3MKkOZgQ"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path :  ")
    file_to = input("Enter the path to upload to dropbox : ")

    transferData.upload_file(file_from, file_to)
    print("File Has Been Moved")

if __name__ == '__main__':
    main()
