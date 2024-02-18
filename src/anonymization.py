from src.exception import AnnommazationException
from src.logger import logging
import os
import sys


from transformers import pipeline, BertTokenizer, BertForTokenClassification
import torch

try:
    logging.info("Loading BERT model and tokenizer...")
    # Load the BERT tokenizer and model for token classification
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertForTokenClassification.from_pretrained("bert-base-uncased", num_labels=18)
    model.eval()
    
    logging.info("Loaded BERT model and tokenizer.")
    
except Exception as e:
    raise AnnommazationException(e, sys)

def anonymize_text(text):
    try:
        logging.info("Anonymizing text...")
        
        # Tokenize the text
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

        with torch.no_grad():
            # Get the token-level predictions
            outputs = model(**inputs)
            
        logging.info("Anonymized text.")
        

        # Get the predicted labels
        predicted_labels = torch.argmax(outputs.logits, dim=2).squeeze().tolist()
        tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'].squeeze().tolist())

        anonymized_text = text
        
        logging.info("Replacing identified entities with asterisks...")
        
        # Replace identified entities with asterisks
        for token, label_id in zip(tokens, predicted_labels):
            label = model.config.id2label[label_id]
            if label != 'O':
                anonymized_text = anonymized_text.replace(token, '*' * len(token))

        return anonymized_text
    
    except Exception as e:
        raise AnnommazationException(e, sys)
