meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            "ROFl": "odpowiedź na żart",
            "SHEESH": "lekka dezaprobat",
            "CREEPY":  "straszny, złowieszczy",
            "AGGRO": "stać się agresywnym/zły",
            }


word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")



if word in meme_dict.keys():
    print("słówo", word)
    print("znaczenie:", meme_dict[word])
else:
    print("error")
    print(" takiego słowa nie ma")
 
