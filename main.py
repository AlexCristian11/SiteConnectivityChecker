import urllib.request as urllib

input_url = input("Enter the URL to check: ")


def main(url):
    print("Checking the connectivity")

    response = urllib.urlopen(url)

    print("Connected successfully")
    print(f"Response code: {response.getcode()}")


main(input_url)