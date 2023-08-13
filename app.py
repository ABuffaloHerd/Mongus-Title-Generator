import gradio as gr
import markovify

with open("./video_titles.txt", "r", encoding="utf-8") as f:
    try:
        text = f.read()
    except UnicodeDecodeError:
        print("Bad unicode in file.")
        exit()

text_model = markovify.NewlineText(text)

def generate(count: int):
    return '\n'.join([text_model.make_short_sentence(100) for i in range(int(count))])

gr.Interface(
    generate,
    gr.inputs.Number(default=1, label="Number of titles"),
    gr.outputs.Textbox(label="Titles")
).launch()