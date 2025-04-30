
import os

# Configuration settings - EDIT THIS SECTION TO CHANGE PROGRAM BEHAVIOR
CONFIG = {
    # API Key for OpenAI
    'API_KEY': os.getenv('OPENAI_API_KEY', ''),
    
    # Model to use for stance detection
    'MODEL_NAME': 'gpt-4.1-mini', # Options: gpt4o, gpt-4o-mini, gpt-4.1, gpt-4.1-mini
    
    # Number of posts to process in each batch
    'BATCH_SIZE': 200,
    
    # Input dataset configuration
    'DATASET_PATH': 'cleaned_original_x_data_idTextUrl.csv',
    'DATASET_FORMAT': 'csv',  # Options: 'pickle', 'csv', 'excel', 'json'
    'TEXT_COLUMN': 'original_text',  # Column name containing the text to analyze
    
    # Output configuration
    'OUTPUT_PATH': '70k_UHC.csv',
    'OUTPUT_FORMAT': 'csv',  # Options: 'pickle', 'csv', 'excel', 'json'
    'BACKUP_DIR': '70k_UHC/',
    
    # Prompt configuration (must match a prompt name in prompt.py)
    'SYSTEM_PROMPT_NAME': 'STANCE_DETECTION_UHC',
    'TASK_PROMPT_NAME': 'UHC_PROMPT'
}