from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
import json

app = FastAPI()

# Counter to keep track of the ID
counter = 0

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html","r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/upload")
async def upload_image(image_url: str = Form(...), image_name: str = Form(...)):
    global counter  # Access the counter variable
    try:
        # Load existing data from JSON file
        try:
            with open("uploaded_images.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        # Increment the counter for the new ID
        counter += 1

        # Add new image data with incremented ID to existing data
        data[counter] = {"name": image_name, "URL": image_url}

        # Save updated data to JSON file
        with open("uploaded_images.json", "w") as f:
            json.dump(data, f, indent=4)

        return JSONResponse(content={"message": "Image link uploaded successfully", "id": counter})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
