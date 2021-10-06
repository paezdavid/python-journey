
import requests

word = input("Enter a word to look up its meaning: ")

response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)
json_response = response.json()

if response.status_code != 200:
    print("No definitions found")
else:
    for i in range(len(json_response[0]["meanings"])):
        # print(f"Part of Speech: ", json_response[0]["meanings"])
        print(
            {i + 1},
            f"PART OF SPEECH:",
            json_response[0]["meanings"][i]["partOfSpeech"],
            " - ",
            f"DEFINITION:",
            json_response[0]["meanings"][i]["definitions"][0]["definition"],
            " - ",
            f"EXAMPLE:",
            json_response[0]["meanings"][i]["definitions"][0]["example"]
        )
        

