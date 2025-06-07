from translate import Translator

print("Welcome to David's translator bot")
print("Type: translate 'hello' to French ")
print("Type 'quit' to exit")





while True:
    userInput = input("You: ")
    if userInput == "quit":
        print("Goodbye")
        break


    if userInput.lower().startswith("translate '") and "' to" in userInput.lower():
        try: 
            word = userInput.split("'")[1]

            language = userInput.split("to ")[-1].lower().strip()
            

            translator = Translator(to_lang=language)


            translation = translator.translate(word)

            print("Translation ", word, "in ", language.title(), "is ", translation)
        except Exception as e:
            print("Error ",e)