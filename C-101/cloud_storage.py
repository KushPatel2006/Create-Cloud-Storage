import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,"rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.A_5iENTftCP8whvxbTGjO4vYtpqSDpl5B7Yf0dO5cGV6oswIjwL-6b5bD_1z-PQXTEY6_MvDFBv0abR4pUk28Lj3nrhl6IUSKD3kyeHRFiOsB7e0pCfFhLjx2eBWncBTVA9bPRI"
    TransferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:-")
    file_to = input("Enter the full path to upload to dropbox:-")

    transferData.upload_file(file_from,file_to)
    print("File has been moved")

main()