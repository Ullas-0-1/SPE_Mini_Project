# app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.calculator import sqrt, factorial, ln, power



# Create FastAPI instance -main application
app = FastAPI()

# Configure template and static folder
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Route for the homepage
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    """Handles GET request to show calculator form."""
    return templates.TemplateResponse("index.html", {"request": request, "result": None, "error": None})

# Route for handling form submission
@app.post("/", response_class=HTMLResponse)
async def calculate(
    request: Request,
    operation: str = Form(...),
    number1: float = Form(...),
    number2: float = Form(0)  # default to 0 for operations that don't need it
):
    """Handles POST request to perform calculations."""
    result = None
    error = None

    try:
        if operation == "sqrt":
            result = sqrt(number1)
        elif operation == "factorial":
            result = factorial(number1)
        elif operation == "ln":
            result = ln(number1)
        elif operation == "power":
            result = power(number1, number2)
        else:
            error = "Invalid operation selected."
    except Exception as e:
        error = str(e)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result,
        "error": error
    })



