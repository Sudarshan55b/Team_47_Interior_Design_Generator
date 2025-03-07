from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import httpx

app = FastAPI(title="Interior Design Generator")

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

WEBUI_ENABLED = True
WEBUI_BASE_URL = "https://chat.ivislabs.in/api"
API_KEY = "sk-ecde4e770ce34426aabe0a9a5e620d91"  # Replace with actual API key
DEFAULT_MODEL = "gemma2:2b"

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_design")
async def generate_design(
    room_type: str = Form(...),
    style: str = Form(...),
    color_scheme: str = Form(...),
    furniture: str = Form(...)
):
    try:
        prompt = f"Generate a detailed room layout and decoration recommendations for a {style} {room_type} with a {color_scheme} color scheme. Include furniture like {furniture}."

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{WEBUI_BASE_URL}/chat/completions",
                headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                json={"model": DEFAULT_MODEL, "messages": [{"role": "user", "content": prompt}]},
                timeout=60.0
            )

        if response.status_code == 200:
            result = response.json()
            generated_text = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
            return JSONResponse(content={"design_recommendation":generated_text})

        raise HTTPException(status_code=500, detail="Failed to generate recommendations.")

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
