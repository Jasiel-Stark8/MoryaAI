from flask import Flask, Blueprint, request, jsonify
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = Flask(__name__)

model_path = './distilgpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
# Set pad_token
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained(model_path)

generate = Blueprint('generate', __name__, url_prefix='/morya-model')

@generate.route('/generate', methods=['POST'], strict_slashes=False)
def generate_text():
    """Distil GPT Model Generation"""
    data = request.get_json(force=True)  # force=True to ensure JSON format
    input_text = data.get('text', '')
    max_length = data.get('max_length')  # Default to a reasonable value if not provided
    max_new_tokens = data.get('max_new_tokens')  # Default to generating up to 100 new tokens

    # Validate max_length
    if not isinstance(max_length, int) or max_length <= 0 or max_length > 1024:
        return jsonify({'error': 'Invalid max_length parameter'}), 400

    encoded_input = tokenizer.encode_plus(input_text,
                                          return_tensors='pt',
                                          add_special_tokens=True)

    input_ids = encoded_input['input_ids']
    attention_mask = encoded_input['attention_mask']

    output = model.generate(input_ids,
                            attention_mask=attention_mask,
                            max_length=max_length,
                            pad_token_id=tokenizer.eos_token_id,
                            # Added below to stop model repitition
                            do_sample=True,
                            temperature=0.7,
                            top_k=50,
                            top_p=0.92,
                            no_repeat_ngram_size=2
                            )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({'generated_text': generated_text})

app.register_blueprint(generate)

if __name__ == '__main__':
    app.run(debug=True)
