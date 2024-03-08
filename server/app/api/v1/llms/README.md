# Morya-92M: A Vanguard in Foundational Models

## Overview

Developed by Jason Quist and Angela Ayivi, Morya-92M is a foundational model marking a significant leap in generative AI. With an 92 million parameter architecture, it sets new standards for machine learning efficacy and computational ingenuity. Originally designed for content creation, Morya-92M's capabilities extend far beyond, showcasing versatility in natural language processing (NLP) tasks. This project embodies the culmination of 4 months of dedicated research, experimentation, and leveraging GPT-2's dataset through advanced transfer learning strategies.

## Features

- **Robust Foundational Knowledge:** Built on GPT-2's extensive dataset, ensuring a comprehensive understanding of a wide array of textual data.
- **Architectural Ingenuity:** Utilizes transformer models and advanced attention mechanisms, optimizing for superior text generation and understanding.
- **State-of-the-Art Training:** Employs cutting-edge GPU infrastructure and distributed training techniques, refining the model's extensive parameter architecture.
- **Versatile Capabilities:** Demonstrates unparalleled proficiency in a range of linguistic tasks, standing out as a transformative force in AI.

## Installation

To get started with Morya-92M, ensure you have Python 3.11+ installed. Then, follow these steps to set up your environment:

1. Clone the MoryaAI repository:

```bash
git clone <repository-link>
cd Morya-92M
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

This will install packages like `h5py`, `typing-extensions`, `wheel`, `transformers`, `torch`, and `tqdm` among others.

## Running Morya-92M

### Local Deployment

To run Morya-92M locally, follow these steps:

1. Navigate to the project directory.
2. Activate your virtual environment.
3. Run the `morya.py` script to start the Flask server:

```bash
python morya.py
```

4. In a separate terminal, use `post.py` to send requests to your model:

```bash
python post.py
```

### Fine-tuning Morya-92M

Morya-92M offers facilities for further fine-tuning. Here's a step-by-step guide to fine-tuning on Kaggle:

1. Create a Kaggle account and verify your phone number for full feature access.
2. Upload the `foundational-model-morya-92m.ipynb` notebook to your Kaggle workspace.
3. Upload the `custom_conversation_dataset.json` as a dataset to your Kaggle input.
4. Configure the session to use a GPU for training, preferably a P100 for optimal performance.
5. Start the training session and monitor progress through Kaggle's logs interface.

For detailed instructions, please refer to the [Kaggle Fine-tuning Guide](#).

## Democratizing AI

Morya-92M is committed to democratizing AI, making advanced AI technologies accessible and usable across various domains. By providing a Flask endpoint and planning a release on Hugging Face, Morya-92M invites collaboration and exploration, empowering developers and researchers to leverage its capabilities for innovative applications.

## Disclaimer

Morya-92M, while a significant advancement in AI research, is primarily an experiment. It inherits certain biases from its training dataset and is designed as a predictive model with fine-tuning for conversational assistance. It represents a step towards creating more targeted and impactful AI solutions.

## Collaboration

We encourage collaboration within the AI community to further enhance and explore the capabilities of Morya-92M. Your contributions can help pave the way for new frontiers in AI research and application.

## Acknowledgements

Special thanks to Kaggle, Angela, Adu (for the extra GPU Clusters) and ALX for bringing me to a high point where I can achieve the impossible.
