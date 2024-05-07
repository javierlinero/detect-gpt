# DetectGPT
In this project, we reproduce and extend upon DetectGPT’s findings using newer models like GPT-3.5 Turbo and GPT-4 Turbo, evaluating DetectGPT’s classification accuracy against supervised RoBERTa models.

## Instructions

First, install the Python dependencies:

    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

Secondly, we've modified the default scripts that our Adroit system can handle, these can be found in the 'base_' sh scripts in `paper_scripts/` folder. 

Likewise if you would like to run any of the writing prompt experiments you need to download it from [here](https://www.kaggle.com/datasets/ratthachat/writing-prompts). Save the data into a directory `data/writingPrompts`. 

We also have this setup where you need to insert an `openai_key` as either the parameter or in a `.env` file when running the scripts. 

Be very mindful of the pricing among the different models. 

Finally, you must modify where the intermediate and final results will be located. These have been designed specifically for the Adroit file system; if you are a princeton student change the netid section to reach the appropriate folder and visit [prerequisites](paper_scripts/README.md), otherwise set it up as so: 

** Intermediate results can be saved in `tmp_results/`. If your experiment completes successfully, the results will be moved into the `results/` directory.**
