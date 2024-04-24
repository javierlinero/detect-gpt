# DetectGPT: Prerequisites for Adroit Cluster

## Sign up for Adroit Access
Go to https://myadroit.princeton.edu/, and make an account with your netid.

## Create Visualization Node
Create a Desktop Visualization Node, this will give you access to an A100 GPU required for this project to train. From there open applications on the top left and go to `Programming -> Vscode`.

Open up a terminal and setup anaconda3
```
module load anaconda3/2024.2
conda init
python3 --version
```

Make sure you have a python version >= 3.9.6.

## Change Directories
You are provided with a 10GB and 100GB storage, you will need to use the 100GB to save your model. Access `run.py` and change

```
chmod +x /paper_scripts/example.sh
sh /paper_scripts/example.sh
```