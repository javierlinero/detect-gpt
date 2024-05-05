import os
import json
import pandas as pd

# This is what allows for us to get the best AUROC score for DetectGPT
def best_auroc_score(directory):
    best_score = 0
    for file in os.listdir(directory):
        if file.startswith("perturbation_") and file.endswith(".json"):
            best_score = max(best_score, auroc_score(os.path.join(directory, file)))
    return best_score

def auroc_score(file_path, key="roc_auc"):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get("metrics", {}).get(key, 0)
    except FileNotFoundError:
        return 0

def model_info1(args_file):
    try:
        with open(args_file, 'r') as f:
            data = json.load(f)
            return data.get("base_model_name", "Unknown Model")
    except FileNotFoundError:
        return "Unknown Model"

def process_dataset(dataset_path):
    models = [os.path.join(dataset_path, model) for model in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, model))]
    scores = []

    for model in models:
        model_name = model_info1(os.path.join(model, "args.json"))
        model_scores = {
            "Model": model_name,
            "log p(x)": auroc_score(os.path.join(model, "likelihood_threshold_results.json")),
            "Entropy": auroc_score(os.path.join(model, "entropy_threshold_results.json")),
            "LogRank": auroc_score(os.path.join(model, "logrank_threshold_results.json")),
            "Rank": auroc_score(os.path.join(model, "rank_threshold_results.json")),
            "DetectGPT": best_auroc_score(model)
        }
        scores.append(model_scores)
    
    return scores

def make_table1(data_root):
    datasets = ["xsum", "squad", "writingprompts"]
    results_dfs = {}

    for dataset in datasets:
        df = pd.DataFrame(process_dataset(os.path.join(data_root, dataset)))
        avg_row = df.mean(numeric_only=True) # append the mean to another row
        avg_row['Model'] = 'Average'
        avg_df = pd.DataFrame([avg_row], columns=df.columns)
        df = pd.concat([df, avg_df], ignore_index=True)
        results_dfs[dataset] = df

    return results_dfs


def model_info2(args_file):
    try:
        with open(args_file, 'r+') as f:
            data = json.load(f)
            data['openai_key'] = None  # Set 'openai_key' to None
            f.seek(0)  # reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()  # remove remaining part of old data
            return data.get("openai_model", "Unknown Model"), data.get("dataset", "Unknown Dataset")
    except FileNotFoundError:
        return "Unknown Model", "Unknown Dataset"

def process_model(model_path):
    scores = []
    for dataset_dir in os.listdir(model_path):
        dataset_path = os.path.join(model_path, dataset_dir)
        if os.path.isdir(dataset_path):
            args_file = os.path.join(dataset_path, "args.json")
            model_name, dataset_name = model_info2(args_file)
            detect_gpt_score = best_auroc_score(dataset_path)
            roberta_large_score = auroc_score(os.path.join(dataset_path, "roberta-large-openai-detector_results.json"))
            roberta_base_score = auroc_score(os.path.join(dataset_path, "roberta-base-openai-detector_results.json"))
            
            scores.append({
                "Model": model_name,
                "Dataset": dataset_name,
                "DetectGPT": detect_gpt_score,
                "Roberta-Large": roberta_large_score,
                "Roberta-Base": roberta_base_score
            })
    return scores

def make_table2(data_root):
    models = [os.path.join(data_root, model) for model in os.listdir(data_root) if os.path.isdir(os.path.join(data_root, model))]
    all_scores = []

    for model in models:
        all_scores.extend(process_model(model))
    
    full_df = pd.DataFrame(all_scores)
    
    for model in full_df['Model'].unique():
        model_df = full_df[full_df['Model'] == model]
        print(f"Results for model: {model}\n", model_df, "\n")

def main():
    data_root = "data/table1"
    results_tables = make_table1(data_root)

    # print for every dataset
    for dataset, df in results_tables.items():
        print(f"Results for {dataset.upper()}:\n", df, "\n")

    data_root = "data/table2"
    make_table2(data_root)

if __name__ == "__main__":
    main()