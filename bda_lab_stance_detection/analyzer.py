import os
import time
import pandas as pd
from openai import OpenAI
from typing import Optional
from tqdm import tqdm
from config import CONFIG

class Analyzer:
    """A class for text analysis and stance annotation using OpenAI."""

    def __init__(self):
        self.client = OpenAI(api_key=CONFIG['API_KEY'])
        self._ensure_backup_dir()

    def _ensure_backup_dir(self):
        """Ensure backup directory exists."""
        os.makedirs(CONFIG['BACKUP_DIR'], exist_ok=True)

    def read_dataset(self, file_path: Optional[str] = None, file_format: Optional[str] = None) -> pd.DataFrame:
        """Read dataset from specified file format."""
        if file_path is None:
            file_path = CONFIG['DATASET_PATH']
        if file_format is None:
            file_format = CONFIG['DATASET_FORMAT']

        if file_format.lower() == 'pickle':
            df = pd.read_pickle(file_path)
        elif file_format.lower() == 'csv':
            df = pd.read_csv(file_path)
        elif file_format.lower() == 'excel':
            df = pd.read_excel(file_path)
        elif file_format.lower() == 'json':
            df = pd.read_json(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

        return df.reset_index(drop=True)

    def save_dataset(self, dataset: pd.DataFrame, batch_num: int, file_path: Optional[str] = None, file_format: Optional[str] = None):
        """Save dataset with timestamp and batch number."""
        if file_format is None:
            file_format = CONFIG['OUTPUT_FORMAT']
        if file_path is None:
            file_path = CONFIG['OUTPUT_PATH']

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"batch_{batch_num}_{timestamp}.{file_format}"
        full_path = os.path.join(CONFIG['BACKUP_DIR'], filename)

        if file_format.lower() == 'pickle':
            dataset.to_pickle(full_path)
        elif file_format.lower() == 'csv':
            dataset.to_csv(full_path, index=False)
        elif file_format.lower() == 'excel':
            dataset.to_excel(full_path, index=False)
        elif file_format.lower() == 'json':
            dataset.to_json(full_path, orient='records', lines=True)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

    def analyze_text(self, text: str, system_prompt: str, task_prompt: str) -> str:
        """Get LLM response for the provided text."""
        completion = self.client.chat.completions.create(
            model=CONFIG['MODEL_NAME'],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": task_prompt.format(text=text)}
            ]
        )
        return completion.choices[0].message.content

    def annotate_dataset(self, dataset: pd.DataFrame, text_column: str, stance_column: str, system_prompt: str, task_prompt: str):
        """Annotate entire dataset with stances using LLM and a progress bar."""
        for idx, row in tqdm(dataset.iterrows(), total=len(dataset), desc="Annotating dataset"):
            if pd.isna(row[stance_column]):
                text = row[text_column]
                stance = self.analyze_text(text, system_prompt, task_prompt)
                dataset.at[idx, stance_column] = stance

        return dataset
