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
cd MoryaAI/server
```
2. Create and Activate a virtual environment.

2. Install required packages:

```bash
pip install -r requirements.txt
```

This will install packages like, `transformers`, `torch`, and `tqdm` among others.

## Running Morya-92M

### Local Deployment

To run Morya-92M locally, follow these steps:

1. Activate your virtual environment.
2. Navigate to the project directory `MoryaAI/server/app/api/v1/llms`
3. Run the `morya.py` script to start the Flask server:

```bash
python3 morya.py
```

4. In a separate terminal, use `post.py` to send requests to your model:
It accepts commandline arguments

```bash
python post.py Hello How Are You?
```

## Further Fine-tuning Instructions for Morya-83M

To enhance Morya-83M's capabilities or adapt it to new datasets, follow these detailed instructions for fine-tuning the model on Kaggle:

### Setting Up Your Environment on Kaggle

1. **Create a Kaggle Account:** If you haven't already, create a Kaggle account by visiting [Kaggle](https://www.kaggle.com) and signing up. This will be your gateway to accessing a vast array of datasets and GPU resources for your fine-tuning needs.

2. **Verify Your Phone Number:** Navigate to your account settings and verify your phone number. This step is crucial as it unlocks all features on Kaggle, including internet access and access to accelerator GPUs and TPUs, which are essential for training AI models.

3. **Prepare Your Notebook:**
   - Click on **Code** in the left navigation menu on Kaggle.
   - Click on **New Notebook**.
   - In the notebook settings, ensure you've selected a GPU as your accelerator to utilize Kaggle's free GPU resources.

4. **Upload Your Notebook:**
   - Click on **File** in the top-left corner of the Kaggle notebook interface.
   - Select **Upload Notebook**.
   - Choose and upload the `foundational-model-morya-92m.ipynb` file from your local machine.

5. **Add Your Dataset:**
   - On the right-hand side of the notebook interface, click on **Add Data**.
   - Then, select **Upload** and drag the content from the `morya-92m` folder into the designated drop area. This will add your custom dataset to the Kaggle notebook for use during fine-tuning.

### Fine-tuning Process

1. **Configure Session Options:**
   - Still in the Kaggle notebook interface, find the **Settings** panel on the right.
   - Scroll down and toggle the **Internet** option to ON. This allows your notebook to download the necessary weights and dependencies for the fine-tuning process.

2. **Select Your GPU:**
   - In the **Settings** panel, under **Accelerator**, select a GPU. For this fine-tuning process, it's recommended to use the **P100 GPU** for its balance between cost and performance. This setup has been optimized for approximately 6 hours of training on a GPU.

3. **Start Fine-tuning:**
   - Once your environment is set up, you're ready to start the fine-tuning process. Click on **Save Version** at the top right of your notebook. This will save your current notebook setup and start the fine-tuning process in the background.
   - You can name your version anything you like, for example, `first_run`. Under **Save and Run All**, this ensures that your notebook runs from start to finish without manual intervention.

### Monitoring and Retrieving Your Model

1. **Monitoring:**
   - Kaggle will notify you when your instance is ready and running. A link will appear at the bottom left of your screen, which you can click to view the logs and monitor the training progress.

2. **Retrieving Your Fine-tuned Model:**
   - Upon completion of the training, navigate to the **Outputs** tab in your notebook. Here, you should find the `pytorch_model.bin` file.
   - Download this file and replace the existing `pytorch_model.bin` file in your cloned project directory with the newly fine-tuned version.

### Final Steps

1. **Set Up Your Local Environment:**
   - Navigate back to the root of your cloned project directory.
   - Create and activate a virtual environment, then install the required dependencies as specified in your project's `requirements.txt` file.

2. **Running Your Model:**
   - Run `morya.py` in one terminal to start the Flask server.
   - In another terminal, run `post.py` to send requests to your model. You can edit the text in `post.py` to any message you wish to process through Morya-83M.

Congratulations! You've successfully fine-tuned Morya-83M. Explore its enhanced capabilities and integrate it into your applications as needed.

## Democratizing AI

Morya-92M is committed to democratizing AI, making advanced AI technologies accessible and usable across various domains. By providing a Flask endpoint and planning a release on Hugging Face, Morya-92M invites collaboration and exploration, empowering developers and researchers to leverage its capabilities for innovative applications.

## Disclaimer

Morya-92M, while a significant advancement in AI research, is primarily an experiment. It inherits certain biases from its training dataset and is designed as a predictive model with fine-tuning for conversational assistance. It represents a step towards creating more targeted and impactful AI solutions.

## Collaboration

We encourage collaboration within the AI community to further enhance and explore the capabilities of Morya-92M. Your contributions can help pave the way for new frontiers in AI research and application.

## Acknowledgements

Special thanks to Kaggle, Angela, Adu (for the extra GPU Clusters) and ALX for bringing me to a high point where I can achieve the impossible.
