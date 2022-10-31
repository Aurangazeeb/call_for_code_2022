import argparse


import torch.cuda
from transformers import AutoTokenizer, pipeline
from transformers import AutoModelForTokenClassification
MODEL_SAVE_DIR = 'footprint_model'

def predict(tasks):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_SAVE_DIR, local_files_only=True)
    loaded_model = AutoModelForTokenClassification.from_pretrained(pretrained_model_name_or_path=MODEL_SAVE_DIR,
                                                                   local_files_only=True)

    loaded_model = pipeline('ner', loaded_model, tokenizer=tokenizer, aggregation_strategy='simple',
                            device='cuda:0' if torch.cuda.is_available() else 'cpu')
    return loaded_model(tasks)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("tasks")
    args = parser.parse_args()
    mytasks = args.tasks


    preds = predict(mytasks.split(','))

    print("Here are the predictions : ",preds)
