# Spam Email Classifier using NLP

## Overview

This project is a spam email classifier built using Natural Language Processing (NLP).
The goal is to automatically identify and filter out spam emails from your inbox. I created this NLP entirely from scratch utilising only two libraries (pandas and re). 

### Idea

I came up with this project while exploring ways to automate email management and improve productivity.
I liked the idea because it combines machine learning, NLP, and real-world utility.

### Workflow

1. **Data Collection**: Gathered a dataset of emails labeled as spam or not spam from kaggle.
2. **Preprocessing**: Cleaned and tokenised the text, removed stopwords, and user has choice to do lemmatization/stemming.
3. **Model Training**: Built and trained a classifier to distinguish spam from non-spam emails.
4. **Evaluation**: Tested the model on a separate dataset to measure accuracy and performance.
5. **Prediction**: Input new emails to classify them as spam or not spam.

---

## How to Run

### Requirements

* Python 3.11+
* `pandas`, `re` (or other NLP libraries as needed)

### Instructions

1. Clone the repository:

   ```bash
   git clone 'https://git.infotech.monash.edu/fit2107UG/2025s2/mdig0003/-/tree/412f5ed7605d7efafe1e767ae47934b2d47b7f09/Final-Project-Folder'
   ```

2. Navigate to the project folder:

   ```bash
   cd src
   ```
3. Install required packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the main script:

   ```bash
   python -m notebook
   ```

5. Explore the 'expirements.ipynb' with different inputs/outputs.

---

## Notes

* Make sure your dataset is in the `data/` folder.
* You can adjust preprocessing steps in `model.py` for better performance.
* If you have a new dataset, train the model first with model.train_model -> select preprocessing strategy (follow on screen instructions) and wait for it to complete running instructions.
