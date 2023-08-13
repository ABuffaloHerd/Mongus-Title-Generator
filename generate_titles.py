import markovify

title_count = input("How many titles? ")
try:
    title_count = int(title_count)
except ValueError:
    print("Invalid input.")
    exit()

# Train the model
with open("./video_titles.txt", "r", encoding="utf-8") as f:
    try:
        text = f.read()
    except UnicodeDecodeError:
        print("Bad unicode in file.")
        exit()

    text_model = markovify.NewlineText(text)

    # Generate titles
    for i in range(title_count):
        print(text_model.make_short_sentence(100))