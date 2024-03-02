from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_text", response_class=HTMLResponse)
async def generate_text(request: Request, input_text: str):
    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    # Generate text using the model
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, do_sample=True)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return templates.TemplateResponse("generated_text.html", {"request": request, "input_text": input_text, "generated_text": generated_text})
