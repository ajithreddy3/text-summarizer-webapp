from fastapi import FastAPI , Request
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration
import re
import torch
from fastapi.templating import Jinja2Templates #UI Part
from fastapi.responses import HTMLResponse #UI Part
from fastapi.staticfiles import StaticFiles #UI Part

app = FastAPI(title = "Text Summarizer app" , description = "This is a text summarizer app built using FastAPI and T5 model" , version = "1.0")
app.mount("/static", StaticFiles(directory="."), name="static")
model = T5ForConditionalGeneration.from_pretrained(r"C:\Users\rohit reddy\Installation\Transformer\saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained(r"C:\Users\rohit reddy\Installation\Transformer\saved_summary_model")
if torch.backends.mps.is_available():
    device = torch.device("mps")

elif torch.cuda.is_available():
    device = torch.device("cuda")

else:
    device = torch.device("cpu")

model = model.to(device)
templates = Jinja2Templates(directory=".")
class DialogueInput(BaseModel):
    dialogue: str   #UI Part

def clean_data(text):
    text = re.sub(r"\r\n" , " " , text)
    text = re.sub(r"\s+" , " " , text)
    text = re.sub(r"<.*?>" , " " , text)
    text = text.strip().lower()
    return text

def summarize_dialogue(text):
    text = clean_data(text)
    inputs = tokenizer(text , padding = "max_length" , max_length = 500 , truncation = True , return_tensors="pt").to(device)

    model.to(device)
    target = model.generate(inputs , max_length = 150 , num_beams = 4 , early_stopping=True)
    summary = tokenizer.decode(target[0], skip_special_tokens=True)
    
    return summary

def summarize_dialogue(text : str)-> str :
    text = clean_data(text)
    inputs = tokenizer(text , padding = "max_length" , max_length = 500 , truncation = True , return_tensors="pt").to(device)

    model.to(device)
    target = model.generate(input_ids = inputs["input_ids"] , attention_mask = inputs["attention_mask"] , max_length = 150 , num_beams = 4 , early_stopping=True)
    summary = tokenizer.decode(target[0], skip_special_tokens=True)
    
    return summary
@app.get("/" , response_class=HTMLResponse) #UI Part
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="Index.html")
@app.post("/summarize")
async def summarize(dialogue_input: DialogueInput):
    dialogue = dialogue_input.dialogue
    summary = summarize_dialogue(dialogue)
    return {"summary": summary}
