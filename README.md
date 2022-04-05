# Grammatical Error Correction: Synthetic Dataset Generation
In this project I use raw Wikipedia articles to create a synthetic dataset for grammatical error correction. 

## Inspiration
Paper from Kiyono et al: An Empirical Study of Incorporating Pseudo Data
into Grammatical Error Correction, url:https://aclanthology.org/D19-1119/

Paper discusses three main methods: BACKTRANS (NOISY), BACKTRANS (SAMPLE) and DIRECTNOISE.
I will be using the DIRECTNOISE method and extrapolate the method from word level to character level. I will also incorporate other kind of data corruption, such as punctuation corruption and corruption based on the part-of-speech (POS) tag. By combining all these different methods I aim to create a synthetic dataset which has high quality uncorrupted sentences paired with realistically corrupted versions of them.

## Dataset
Dataset consists of 6078422 Wikipedia articles. All the articles are from the English version of Wikipedia. The data was scraped on the 1st of May 2020. I used the Huggingface "load_dataset" function to download the data. More on how to download the dataset can be found here: https://github.com/huggingface/datasets/tree/master/datasets/wikipedia

## Methods
All of the variables mentioned in this section can be tuned in src/settings.py file.

### Sentence Level
I did not want to corrupt all the sentences in the dataset to avoid training LMs to always correct the sentences, even if there are no mistakes. I used "sentence_percentage" variable to tune what percentage of the sentences get corrupted. 

The percentage of corrupted sentences can be adjusted from src/settings.py under caption "Sentence corrupt"

### Word Level
Word level corruptions included:
- Masking
- Deletion
- Insertion
- Swapping
- POS-tag corruption (more in the next section)

Proportions of word level corruptions can be adjusted from src/settings.py under caption "Word corrupt"

### POS Level
Corruptions based on the POS-tag include:
- Corrupting adjectives by adding or removing comparatives and superlatives
- Corrupting articles by mixing them randomly
- Corrupting nouns by pluralizing singular words and singularizing plural words
- Corrupting words by mixing tenses, person and number

Proportions of POS-corruptions can be adjusted from src/settings.py under caption "POS corrupt"

### Character Level [Synthetic Spelling Error (SSE)]
Character level corruptions included:
- Insertion
- Deletion
- Replacement
- Swapping

Proportions of character level corruptions can be adjusted from src/settings.py under caption "Character corrupt"

## How to Run
You only need to have Docker and docker-compose installed. You can install them from here: https://docs.docker.com/get-docker/

Then perform the following steps:
1. In the root of the project run the following command in terminal: ```docker-compose up```
2. In another terminal run the following command: ```docker exec -it gec_app bash```

You're good to go! You're now inside the container and can use BASH to navigate. Navigate to "src" directory and run the command ```python main.py```. This command will run the main script which will create the training and validation sets and upload them to "data" directory with the settings used for creating the datasets.