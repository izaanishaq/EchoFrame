import torch
from transformers import Blip2Processor, Blip2ForConditionalGeneration # Removed BitsAndBytesConfig
from PIL import Image

# Load BLIP-2 model and processor
# quant_config = BitsAndBytesConfig(load_in_8bit=True) # Removed for CPU-only
processor = Blip2Processor.from_pretrained("Salesforce/blip2-flan-t5-xl")
model = Blip2ForConditionalGeneration.from_pretrained(
    "Salesforce/blip2-flan-t5-xl",
    # quantization_config=quant_config, # Removed for CPU-only
    device_map={"":"cpu"} # Explicitly set to CPU
)

device = "cpu" # This is correctly set

def generate_answer(image: Image.Image, question: str) -> str:
    if not image.mode == "RGB":
        image = image.convert("RGB")

    # Consider changing torch.float16 to torch.float32 if you encounter issues or poor performance on CPU
    inputs = processor(image, question, return_tensors="pt").to(device, torch.float16)
    generated_ids = model.generate(**inputs)
    answer = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
    return answer
