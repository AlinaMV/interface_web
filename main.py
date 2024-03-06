from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from transformers import GPT2LMHeadModel, GPT2Tokenizer
############################
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="fekpghojezpoh/sarcasm_BARThez")
########################################################################

app = FastAPI()

# Mount the "static" directory to serve static files (CSS, JS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


############################ TEST
# Load pre-trained GPT-2 model and tokenizer
#model_name = "gpt2"
#tokenizer = GPT2Tokenizer.from_pretrained(model_name)
#model = GPT2LMHeadModel.from_pretrained(model_name)
############################


############################
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("fekpghojezpoh/sarcasm_BARThez_v3")
model = AutoModelForSeq2SeqLM.from_pretrained("fekpghojezpoh/sarcasm_BARThez_v3")
########################################################################

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_text", response_class=HTMLResponse)
async def generate_text(request: Request, input_text: str = Form(...)):
    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    # Generate text using the model
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, do_sample=True)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return templates.TemplateResponse("generated_text.html", {"request": request, "input_text": input_text, "generated_text": generated_text})
