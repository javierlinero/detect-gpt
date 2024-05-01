# fixed this legacy version into the updated v1.25 of openai api
python run.py --output_name openai --batch_size 5 --openai_model davinci-002  --mask_filling_model_name t5-3b --n_perturbation_list 1,10,75 --n_samples 150 --pct_words_masked 0.3 --span_length 2 --do_top_p --top_p 0.9 --mask_top_p 0.95 --dataset pubmed
python run.py --output_name openai --batch_size 5 --openai_model davinci-002  --mask_filling_model_name t5-3b --n_perturbation_list 1,10,75 --n_samples 150 --pct_words_masked 0.3 --span_length 2 --do_top_p --top_p 0.9 --mask_top_p 0.95 --dataset writing
python run.py --output_name openai --batch_size 5 --openai_model davinci-002  --mask_filling_model_name t5-3b --n_perturbation_list 1,10,75 --n_samples 150 --pct_words_masked 0.3 --span_length 2 --do_top_p --top_p 0.9 --mask_top_p 0.95

# Our ablations to the project include gpt3.5turbo & gpt4turbo (chat-conversational models)
python run.py --output_name openai --batch_size 5 --openai_model gpt-3.5-turbo-0125  --mask_filling_model_name t5-3b --n_perturbation_list 1,10,75 --n_samples 150 --pct_words_masked 0.3 --span_length 2 --do_top_p --top_p 0.9 --mask_top_p 0.95 --dataset pubmed
python run.py --output_name openai --batch_size 5 --openai_model gpt-3.5-turbo-0125  --mask_filling_model_name t5-3b --n_perturbation_list 1,10,75 --n_samples 150 --pct_words_masked 0.3 --span_length 2 --do_top_p --top_p 0.9 --mask_top_p 0.95 --dataset writing
python run.py --output_name openai --batch_size 5 --openai_model gpt-3.5-turbo-0125  --mask_filling_model_name t5-3b --n_perturbation_list 1,10,75 --n_samples 150 --pct_words_masked 0.3 --span_length 2 --do_top_p --top_p 0.9 --mask_top_p 0.95

python run.py --output_name openai --batch_size 5 --openai_model gpt-4-turbo  --mask_filling_model_name t5-3b --n_perturbation_list 1,10,75 --n_samples 150 --pct_words_masked 0.3 --span_length 2 --do_top_p --top_p 0.9 --mask_top_p 0.95 --dataset pubmed
python run.py --output_name openai --batch_size 5 --openai_model gpt-4-turbo  --mask_filling_model_name t5-3b --n_perturbation_list 1,10,75 --n_samples 150 --pct_words_masked 0.3 --span_length 2 --do_top_p --top_p 0.9 --mask_top_p 0.95 --dataset writing
python run.py --output_name openai --batch_size 5 --openai_model gpt-4-turbo  --mask_filling_model_name t5-3b --n_perturbation_list 1,10,75 --n_samples 150 --pct_words_masked 0.3 --span_length 2 --do_top_p --top_p 0.9 --mask_top_p 0.95

