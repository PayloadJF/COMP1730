## install
To run this code,we need to install and run jupyter notebook first
<br>
``
pip install jupyter
``
<br>
``
cd ./
``
<br>
``
jupyter notebook
``

## app_ids.ipynb
This file use steam official api to get all application's id and store them in app_id.json

## Get_Reviews.ipynb
This file create a web scrawler to collect reviews <br>
Each game's reivews are stored in the ./Reivew folder, and file is named after application id <br>/
## kernel_function_for_SVM.py
py file stored 3 different kernel function of SVM, suitbale for different dataset

## main.ipynb
It is the main file of this project, containing the data process code, Naive Bayes and Support Vector Machine mode <br>

## How to run BERT
Because of the size limitation of wattle submission, we do need to download BERT pre-trained language model from [Google BERT](https://storage.googleapis.com/bert_models/2019_05_30/wwm_uncased_L-24_H-1024_A-16.zip), unzip it, put the files in the ./Bert/bert/BERT_BASE_DIR/
<br>
Because we have implement the 'mytask_sentiment' function in BERT files, only run below code can get the training result

python run_classifier.py  -task_name=mytask_sentiment <br>
                          -do_train=false          <br>
                          -do_eval=true         <br>
                          -data_dir=data    <br>
                          -vocab_file=BERT_BASE_DIR/vocab.txt       <br>
                          -bert_config_file=BERT_BASE_DIR/bert_config.json      <br>
                          -init_checkpoint=BERT_BASE_DIR/bert_model.ckpt      <br>
                          -max_seq_length=128           <br>
                          -train_batch_size=32          <br>
                          -learning_rate=2e-5           <br>
                          -num_train_epochs=3.0         <br>
                          -output_dir=/mytask_output          <br>


