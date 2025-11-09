from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from src.external_api.service import service
from src.external_api.models import CatFactModel, CatImageModel, CatCombinedModel

router = APIRouter(prefix="/external", tags=["External API"])

@router.get("/fact", response_model=CatFactModel)
def get_cat_fact():
    try:
        return service.get_cat_fact()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

@router.get("/image", response_model=CatImageModel)
def get_cat_image():
    try:
        return service.get_cat_image()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

@router.get("/cat", response_model=CatCombinedModel)
def get_cat_info():
    try:
        return service.get_cat_info()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

@router.get("/cat/html", response_class=HTMLResponse)
def get_cat_html():
    try:
        data = service.get_cat_info()
        html = f"""
        <!doctype html>
        <html>
          <head><meta charset="utf-8"><title>Random Cat</title></head>
          <body>
            <img src="{data.image_url}" alt="cat" style="max-width:600px;"/><p>{data.fact}</p>
          </body>
        </html>
        """
        return HTMLResponse(content=html, status_code=200)
    except Exception as e:
        return HTMLResponse(content=f"<h3>Error: {e}</h3>", status_code=500)
