from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load English model
english_tokenizer = AutoTokenizer.from_pretrained("fekpghojezpoh/sarcasm_BART_v2")
english_model = AutoModelForSeq2SeqLM.from_pretrained("fekpghojezpoh/sarcasm_BART_v2")

# Load French model
french_tokenizer = AutoTokenizer.from_pretrained("fekpghojezpoh/sarcasm_BARThez_v3")
french_model = AutoModelForSeq2SeqLM.from_pretrained("fekpghojezpoh/sarcasm_BARThez_v3")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_text", response_class=HTMLResponse)
async def generate_text(request: Request, input_text: str = Form(...), language: str = Form(...)):
    # Select model and tokenizer based on language
    if language == "Generate in English":
        tokenizer = english_tokenizer
        model = english_model
    elif language == "Générez en français":
        tokenizer = french_tokenizer
        model = french_model
    else:
        return "Invalid language selected."

    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text using the model
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, do_sample=True)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return templates.TemplateResponse("generated_text.html", {"request": request, "input_text": input_text, "generated_text": generated_text, "language": language})