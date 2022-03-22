# Grammatical Error Correction: Synthetic Dataset Generation

## Settings
  - Methods: 
    - Sentence Level: Percentage for the fraction of words modified
    - Word level: DirectNoise  
    - Character level: Synthetic Spelling Error (SSE)
      - 0.3% per character: deletion, insertion, replacement, or transposition of adjacent characters
  - Seed corpus: Wikipedia
  - Optimization setting: PRETRAIN
    - Peak with 30M samples for pre-training
