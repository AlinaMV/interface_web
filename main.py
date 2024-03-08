from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import uvicorn

# Create FastAPI instance
app = FastAPI()

# Mount static files directory for serving CSS, JS, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load Jinja2 templates for generating dynamic HTML content
templates = Jinja2Templates(directory="templates")

# Load English model
english_tokenizer = AutoTokenizer.from_pretrained("fekpghojezpoh/sarcasm_BART_v2")
english_model = AutoModelForSeq2SeqLM.from_pretrained("fekpghojezpoh/sarcasm_BART_v2")

# Load French model
french_tokenizer = AutoTokenizer.from_pretrained("fekpghojezpoh/sarcasm_BARThez_v3")
french_model = AutoModelForSeq2SeqLM.from_pretrained("fekpghojezpoh/sarcasm_BARThez_v3")

# Define route to serve home page
@app.get("/", response_class=HTMLResponse)
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define route to generate sarcastic text
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
        raise HTTPException(status_code=400, detail="Invalid language selected.")

    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    # Generate text using the model
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, do_sample=True)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Render generated text template with input text, generated text, and selected language
    return templates.TemplateResponse("generated_text.html", {"request": request, "input_text": input_text, "generated_text": generated_text, "language": language})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
