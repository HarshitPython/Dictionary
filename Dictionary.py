import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
  # lower() means either you write in capital or in lower it will take only in lower
  w=w.lower()
  if w in data:
    return data[w]
  elif w.title() in data:
    return data[w.title()]
  elif w.upper() in data: #in case user enters words like USA or NATO
    return data[w.upper()]
  elif len(get_close_matches(w,data.keys())) >0:
    yn = input("Did you mean %s instead? Enter Y if yes, or N if no:"%get_close_matches(w,data.keys())[0])
    if yn =="Y":
      return data[get_close_matches(w,data.keys())[0]]
    elif yn =="N":
      return "The word does not exist.Please double check it."
    else:
      return "we did not understand your entry"
  else:
    return "The word does not exist.Please double check it."

word=input("Enter word: ")

output = translate(word)

if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)
