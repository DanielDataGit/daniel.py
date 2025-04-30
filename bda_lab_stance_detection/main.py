import pandas as pd
from analyzer import Analyzer
from config import CONFIG
from prompt import SYSTEM_PROMPTS, TASK_PROMPTS

def main():
    analyzer = Analyzer()

    # Load dataset
    dataset = analyzer.read_dataset()

    model_col = f"{CONFIG['MODEL_NAME']}_stance"

    if model_col not in dataset.columns:
        dataset[model_col] = None

    text_column = CONFIG['TEXT_COLUMN']

    # Get prompts
    system_prompt = SYSTEM_PROMPTS[CONFIG['SYSTEM_PROMPT_NAME']]
    task_prompt = TASK_PROMPTS[CONFIG['TASK_PROMPT_NAME']]

    batch_size = CONFIG['BATCH_SIZE']
    total_batches = (len(dataset) + batch_size - 1) // batch_size

    for batch_num in range(total_batches):
        batch_start = batch_num * batch_size
        batch_end = min(batch_start + batch_size, len(dataset))

        batch_df = dataset.iloc[batch_start:batch_end].copy()

        # Annotate batch
        annotated_batch = analyzer.annotate_dataset(
            dataset=batch_df,
            text_column=text_column,
            stance_column=model_col,
            system_prompt=system_prompt,
            task_prompt=task_prompt
        )

        # Save intermediate batch results (backup)
        analyzer.save_dataset(annotated_batch, batch_num)
        dataset.iloc[batch_start:batch_end] = annotated_batch

    # Save the final annotated dataset
    analyzer.save_dataset(dataset, batch_num='final', file_path=CONFIG['OUTPUT_PATH'], file_format=CONFIG['OUTPUT_FORMAT'])
    print(f"Final annotated dataset saved to {CONFIG['OUTPUT_PATH']} in {CONFIG['OUTPUT_FORMAT']} format.")

if __name__ == "__main__":
    main()