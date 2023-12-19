# Contextualized Embeddings Encode Monolingual and Cross-lingual Knowledge of Idiomaticity

### Installation:

* To run the experiments, install python3. Then, you need to install the following packages:

`
python -m pip install -r requirements.txt
`

---
### Running experiments:

You can find the code for each experiment in each sub-directory in the Source Code directory. 

* BERT
* RoBERTa
* mBERT
* RuBERT
* LAYERS
* Cross-lingual

---
### Datasets:
Pre-processed datasets for our experiments are available in Datasets directory. If you wish to go through the process of preparing them by yourself, use the follwoing scrip files:

##### VNC-Tokens dataset:

* The TEST portions of this dataset is available in the Datasets directory.

##### Russian Datasets:

* This dataset is in the Datasets directory but if you wish to construct desired dataset, you can get the russian dataset from (https://github.com/kaharodnik/Ru_idioms). We only use texts from Russian Wikipedia and a context of up to 300 characters to the left and right of the target expression. You can achive this by running following in the Russian Dataset Prepration directory:
 
`
python Wiki.py
`

##### Datasets for our experiments are ready by this step.

---
#### If you have any further questions, please do not hesitate to contact me.
