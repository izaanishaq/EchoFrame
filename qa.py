import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image

# Load BLIP-2 model and processor
processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-flan-t5-xl",
    device_map={"":"cpu"} 
)

device = "cpu" 

def generate_answer(image: Image.Image, question: str) -> str:
    if not image.mode == "RGB":
        image = image.convert("RGB")

    inputs = processor(image, question, return_tensors="pt").to(device, torch.float16)
    generated_ids = model.generate(**inputs)
    answer = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
    return answer
