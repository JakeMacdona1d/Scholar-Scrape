import requests


def download_pdf(url, file_name, dir, headers):

    # Send GET request
    response = requests.get(url, headers=headers)

    # Save the PDF
    if response.status_code == 200:
        with open(dir + '/' +file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)


def savePdf(url,dir):
    # Define HTTP Headers
    headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }

    # Define image file name
    file_name = "file1.pdf"

    # Download image
    download_pdf(url, file_name, dir, headers)

savePdf