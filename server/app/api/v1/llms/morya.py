import os
from flask import Flask, Blueprint, request, jsonify
from transformers import GPT2Tokenizer, GPT2LMHeadModel, GPT2Config

os.environ["TRANSFORMERS_USE_SAFETENSORS"] = "1"

app = Flask(__name__)

model_path = './distil_morya'
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
tokenizer.pad_token = tokenizer.eos_token
config = GPT2Config.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path, config=config, ignore_mismatched_sizes=True)

# Create a Flask Blueprint for generating text with a specific URL prefix
generate = Blueprint('generate', __name__, url_prefix='/morya-model')

# Define a route within the Blueprint for generating text, accepting only POST requests
@generate.route('/generate', methods=['POST'], strict_slashes=False)
def generate_text():
    """Distil GPT Model Generation"""
    # Get the JSON data from the request, forcing it if necessary
    data = request.get_json(force=True)
    # Retrieve the input text from the data, defaulting to an empty string if not found
    input_text = data.get('text', '')
    # Retrieve the maximum length for the generated text, if provided
    max_length = data.get('max_length')
    # Retrieve the maximum number of new tokens to generate, if provided
    max_new_tokens = data.get('max_new_tokens')

    # Validate the max_length parameter to ensure it's an integer, greater than 0 and less than or equal to 1024
    if not isinstance(max_length, int) or max_length <= 0 or max_length > 1024:
        return jsonify({'error': 'Invalid max_length parameter'}), 400

    # Encode the input text into format compatible with the model, including special tokens
    encoded_input = tokenizer.encode_plus(input_text,
                                          return_tensors='pt',
                                          add_special_tokens=True)

    # Extract the input_ids and attention_mask from the encoded input
    input_ids = encoded_input['input_ids']
    attention_mask = encoded_input['attention_mask']

    # Generate text from the model using the provided parameters and the encoded input
    output = model.generate(input_ids,
                            attention_mask=attention_mask,
                            max_length=max_length,
                            pad_token_id=tokenizer.eos_token_id,
                            do_sample=True,  # Enable sampling to introduce randomness in output
                            temperature=0.7,  # Adjusts randomness in sampling, lower is less random
                            top_k=50,  # Limits the sampling pool to the top k tokens
                            top_p=0.92,  # Applies nucleus sampling, keeping cumulative probability of top p tokens
                            no_repeat_ngram_size=2  # Prevents repeating 2-gram sequences to reduce repetition
                            )

    # Decode the generated text, skipping special tokens
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Return the generated text as JSON
    return jsonify({'generated_text': generated_text})

# Register the Blueprint with the Flask application
app.register_blueprint(generate)

# Run the Flask application in debug mode if this script is the main program
if __name__ == '__main__':
    app.run(debug=True)
