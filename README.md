# NLP Assignment 8 (AIT - DSAI)

- [Student Information](#student-information)
- [Task 1 - Dataset](#task-1---dataset)
- [Task 2 - Training](#Task-2---training)
- [Task 3 - Web Application Development](#task-3---web-application-development)

## Student Information
 - Name: Myo Thiha
 - ID: st123783

## Task 1 - Dataset
 - I used https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json as training data and https://huggingface.co/datasets/tatsu-lab/alpaca_eval for the evaluation.

## Task 2 - Training
The language model underwent training through the Supervised Fine-Tuning (SFT) method, utilizing the Trainer class from the Hugging Face Transformers library. Additionally, the Alpaca dataset was integrated into the pre-existing code structure for the training process.

## Task 3 - Web Application Development

### How to run?

How to run: go inside the app folder using terminal and run `python app.py`. Note that your python environment must contains the dependencies: flask, peft 0.7.1, trl 0.7.4, transformer 4.36.2.
 - Then, the application can be accessed on http://localhost:8000
 - You will directly land on the "Home" page.

### How to run?

Input - Type your query or prompt in the text box.
Output - the model will generate something related to your prompt.