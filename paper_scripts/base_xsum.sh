python run.py --output_name main --base_model_name gpt2-xl --mask_filling_model_name t5-3b --n_perturbation_list 1,10,100 --n_samples 500 --pct_words_masked 0.3 --span_length 2
python run.py --output_name main --base_model_name EleutherAI/gpt-neo-2.7B --mask_filling_model_name t5-3b --n_perturbation_list 1,10,100 --n_samples 500 --pct_words_masked 0.3 --span_length 2
python run.py --output_name main --base_model_name EleutherAI/gpt-j-6B --mask_filling_model_name t5-3b --n_perturbation_list 1,10,100 --n_samples 500 --pct_words_masked 0.3 --span_length 2
python run.py --output_name main --base_model_name facebook/opt-2.7b --mask_filling_model_name t5-3b --n_perturbation_list 1,10,100 --n_samples 500 --pct_words_masked 0.3 --span_length 2
#python run.py --output_name main --batch_size 20 --base_model_name EleutherAI/gpt-neox-20b --mask_filling_model_name t5-11b --n_perturbation_list 1,10,100 --n_samples 500 --pct_words_masked 0.3 --span_length 2
