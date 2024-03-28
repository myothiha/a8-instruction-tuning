from flask import Flask, render_template, request
import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Load the saved model state dictionary
model_path = "./models/model.pt"
state_dict = torch.load(model_path)

# Initialize the model and load the saved state
model_name_or_path = "distilgpt2"
model = AutoModelForCausalLM.from_pretrained(model_name_or_path)
model.load_state_dict(state_dict)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

# Move the model to the appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/answer', methods=['POST'])
def answer():

    query = request.form.get('query')
    # answer = model({"question": question})

    input_ids = tokenizer.encode(query, return_tensors="pt").to(device)

    # Generate output
    output = model.generate(input_ids, max_length=256, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    # Decode and print the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return render_template('index.html', old_query = query, result = generated_text)


port_number = 8000

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_number)