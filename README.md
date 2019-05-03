# Materials for the Introduction to Machine Learning Workshop


Links to Jupyter notebooks will be posted here by May 9th!

You have two options for running the Jupyter notebooks:


#### OPTION 1: run on Google Colab

All you need is a Google account and either Google Chrome or Firefox.  
See the FAQ if you would like to learn more about Google Colab:
https://research.google.com/colaboratory/faq.html

#### OPTION 2: run locally

Miniconda: download and install from https://conda.io/miniconda.html (choose the Python 3.6 version)  

Open Anaconda Prompt (Windows) or Terminal (Mac) and run the following:

`conda create -n rriML python=3`  

`source activate rriML`  

`conda install git`  

`conda install jupyter`  

`cd ~`  

`git clone https://www.github.com/amandakeasson/rriML`  

`cd rriML`  

`pip install -r requirements.txt` 

`python download_nilearn_data.py`

