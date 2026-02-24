import os
import base64
import uuid
import aiofiles
from datetime import datetime
from typing import Optional
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GENERATED_DESIGNS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "generated_designs")

os.makedirs(GENERATED_DESIGNS_PATH, exist_ok=True)

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def build_jewelry_prompt(
    jewelry_type: str,
    color: str,
    shape: str,
    material: str,
    karat: str,
    gemstone_type: str,
    gemstone_color: Optional[str] = None
) -> str:
    gemstone_desc = ""
    if gemstone_type and gemstone_type.lower() != "none":
        gemstone_desc = f"adorned with a stunning {gemstone_type}"
        if gemstone_color:
            gemstone_desc += f" in {gemstone_color} color"
        gemstone_desc += ", "
    
    prompt = f"""Create a photorealistic image of an exquisite {jewelry_type.lower()} piece.
    
Design specifications:
- Material: Premium {material} ({karat})
- Primary color: {color}
- Shape/Style: {shape} design
- {gemstone_desc}beautifully set in the center

The jewelry should showcase:
- Exceptional craftsmanship with intricate detailing
- Professional studio lighting with soft reflections
- Elegant presentation suitable for a luxury jewelry catalog
- High polish finish highlighting the {material}'s natural luster
- Realistic proportions and textures

Style: High-end jewelry photography, luxury brand quality, magazine-worthy composition.
Background: Clean, subtle gradient or soft focus backdrop that enhances the jewelry's beauty."""

    return prompt

async def generate_jewelry_image(
    jewelry_type: str,
    color: str,
    shape: str,
    material: str,
    karat: str,
    gemstone_type: str,
    gemstone_color: Optional[str] = None
) -> Optional[dict]:
    if not GEMINI_API_KEY:
        return {"error": "GEMINI_API_KEY not configured", "image_path": None}
    
    try:
        prompt = build_jewelry_prompt(
            jewelry_type, color, shape, material, karat, gemstone_type, gemstone_color
        )
        
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        response = await model.generate_content_async(
            prompt,
            generation_config={
                "response_modalities": ["IMAGE", "TEXT"],
                "temperature": 0.7,
            }
        )
        
        image_data = None
        for part in response.parts:
            if hasattr(part, 'inline_data') and part.inline_data:
                image_data = part.inline_data.data
                break
        
        if not image_data:
            if hasattr(response, 'text'):
                return {"error": f"No image generated. Response: {response.text}", "image_path": None}
            return {"error": "No image data in response", "image_path": None}
        
        filename = f"{uuid.uuid4().hex}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        image_path = os.path.join(GENERATED_DESIGNS_PATH, filename)
        
        async with aiofiles.open(image_path, 'wb') as f:
            await f.write(base64.b64decode(image_data))
        
        relative_path = f"/static/generated_designs/{filename}"
        
        return {
            "error": None,
            "image_path": relative_path,
            "filename": filename
        }
        
    except Exception as e:
        return {"error": str(e), "image_path": None}