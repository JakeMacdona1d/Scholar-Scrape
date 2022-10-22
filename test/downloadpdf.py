import requests


def download_pdf(url, file_name, headers):

    # Send GET request
    response = requests.get(url, headers=headers)

    # Save the PDF
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(response.status_code)



if __name__ == "__main__":

    # Define HTTP Headers
    headers = {
        "User-Agent": "Chrome/51.0.2704.103",
    }

    # Define URL of an image
    url = "https://pyshark.com/wp-content/uploads/2022/05/merged_all_pages.pdf"

    # Define image file name
    file_name = "file1.pdf"

    # Download image
    download_pdf(url, file_name, headers)