import requests
def main():
    url="https://jsonplaceholder.typicode.com/todos"

    resp = requests.get(url)
    data = resp.json()


    print(data[0])


    # python3.8 -m venv .venv

if __name__ == '__main__':
    main()