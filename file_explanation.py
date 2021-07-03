import requests
from game_logic import incorrect_words


# TODO: TRY/CATCH BLOCKS IF THERE IS NO INTERNET CONNECTION
def explaining_words():
    for word in incorrect_words:
        url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/" + word
        headers = {"Accept": "application/json"}
        response = requests.request("GET", url, headers=headers)
        print(response.text)