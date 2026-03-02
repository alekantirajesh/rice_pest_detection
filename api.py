from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import io
import sys
from pathlib import Path
import torch
import torch.nn as nn
from torchvision import transforms, models

# Ensure project root is importable so we can import knowledge_base
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import knowledge_base

app = Flask(__name__)
CORS(app)


def load_model(path="final_15class_model.pth", device="cpu"):
    model = models.resnet50(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 15)

    # Resolve model path: check given path, then repo root
    p = Path(path)
    if not p.is_file():
        p = ROOT / path
    if not p.is_file():
        raise FileNotFoundError(f"Model file not found at {path} or {p}")

    ckpt = torch.load(str(p), map_location=device)
    if isinstance(ckpt, dict) and "model_state" in ckpt:
        state = ckpt["model_state"]
    elif isinstance(ckpt, dict) and any(k.startswith("module.") or k in model.state_dict() for k in ckpt.keys()):
        state = ckpt
    else:
        state = ckpt

    model.load_state_dict(state)
    model.eval()
    return model


MODEL = None


def init():
    global MODEL
    try:
        MODEL = load_model()
        print("Model loaded")
    except Exception as e:
        MODEL = None
        print("Failed to load model:", e)


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "no image provided"}), 400

    file = request.files["image"]
    img_bytes = file.read()
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    tensor = transform(img).unsqueeze(0)

    if MODEL is None:
        return jsonify({"error": "model not loaded"}), 500

    with torch.no_grad():
        out = MODEL(tensor)
        idx = int(torch.argmax(out, 1).item())
        probs = torch.softmax(out, 1)[0]
    
    # Debug logging
    print(f"Predictions: {out}")
    print(f"Argmax index: {idx}")
    print(f"Top 3 scores: {torch.topk(probs, 3)}")

    name = knowledge_base.CLASS_NAMES[idx]
    info = knowledge_base.pest_info.get(name, {})

    return jsonify({
        "index": idx,
        "name": name,
        "info": info
    })


if __name__ == "__main__":
    init()
    app.run(host="0.0.0.0", port=5005, debug=True)
