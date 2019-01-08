# Standford Cars  - Image Classification

Image classification of the stanford-cars dataset leveraging the fastai v1. The goal is to try hit 90%+ accuracy, starting with a basic fastai image classification workflow and interating from there. My 90%+ goal is based on @sgugger's code implementing Adam for the Stanford Cars dataset, here: https://github.com/sgugger/Adam-experiments

This was all run on a Paperspace P4000 machine

## Potential Avenues of Investigation:

Implementation of:

- Stanford Cars SOTA 93.61% (Aug-18)  https://www.researchgate.net/publication/316027349_Deep_CNNs_With_Spatially_Weighted_Pooling_for_Fine-Grained_Car_Recognition
- @sgugger's adam experiments: https://github.com/sgugger/Adam-experiments

## NOTEBOOKS

**1. stanford_cars_benchmark.ipynb**

    - Benchmark model using basic fastai image classification workflow
    - 84.95% Accuracy
    
## Credits

- code to extract the labels and annotations from the .mat files: Devon Yates' code on Kaggle, thanks Devon! https://www.kaggle.com/criticalmassacre/inaccurate-labels-in-stanford-cars-data-set
