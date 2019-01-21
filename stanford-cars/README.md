# Standford Cars  - Image Classification

Image classification of the stanford-cars dataset leveraging the fastai v1. The goal is to **try hit 90%+ accuracy**, starting with a basic fastai image classification workflow and interating from there. My 90%+ goal is based on @sgugger's code implementing Adam for the Stanford Cars dataset, here: https://github.com/sgugger/Adam-experiments

This was all run on a Paperspace P4000 machine

## Potential Avenues of Investigation:
FORNAX - Great roundup in advances in 2018, some of which can be applied: https://github.com/kmkolasinski/deep-learning-notes/blob/master/seminars/2018-12-Improving-DL-with-tricks/Improving_deep_learning_models_with_bag_of_tricks.pdf

AMAZON - Bag of Tricks for Image Classification with Convolutional Neural Network: https://arxiv.org/pdf/1812.01187.pdf

#### Data Augmentation
- Train only on cropped images
- Use Mixup (https://docs.fast.ai/callbacks.mixup.html , https://forums.fast.ai/t/mixup-data-augmentation/22764/21, https://arxiv.org/abs/1710.09412)
- Use own stats (mean+std dev) from training set to normalize the images
- Use non-standard fastai image augmentations, including augmentations for this dataset can be found here: http://ee.sharif.edu/~shayan_f/fgcc/index.html 

#### Training Regimes
- Agressive LR for training all layers
- Adding Weight-Decay and tuning Dropout
- @sgugger's adam experiments: https://github.com/sgugger/Adam-experiments
- AdamW with 1-cycle: https://twitter.com/radekosmulski/status/1014964816337952770?s=12
- AdamW and other DL tricks: https://twitter.com/drsxr/status/1073208269907353602?s=12
- train with bn_freeze=true for unfrozen layers
- Shake-Shake Regularisation (mentioned in Fornax slides above)
- Knowledge Distillation (paper: https://arxiv.org/abs/1503.02531, https://forums.fast.ai/t/part-1-complete-collection-of-video-timelines/5504)

#### Architecture
- Try alternate resnet sizes (benchmark used resnet152

Implementation of:
- Stanford Cars SOTA 93.61% (Apr-18)  https://www.researchgate.net/publication/316027349_Deep_CNNs_With_Spatially_Weighted_Pooling_for_Fine-Grained_Car_Recognition


## Notebooks

**1_stanford_cars_basic.ipynb**

 - Benchmark model using basic fastai image classification workflow including the 1-cycle policy
 - 84.95% Accuracy
 
 **2_stanford_cars_lr_tuning.ipynb**

 - Tuning of the learning rate and differential learning rates, again using fastai's implementation of the 1-cycle policy
 - 88.19% Accuracy, up 3.2%
 
 **3_stanford_cars_cropped.ipynb**

 - Training the model using the cropped images, based on the bounding boxes provided
 - XX.XX% Accuracy, down 
 
 **4_stanford_cars_mixup.ipynb**

 - Tuning the model using the mixup protocol, blending input images to provide stronger regularisation
 - XX.XX% Accuracy, up X.X%
 
 
    
## Credits

- code to extract the labels and annotations from the .mat files: Devon Yates' code on Kaggle, thanks Devon! https://www.kaggle.com/criticalmassacre/inaccurate-labels-in-stanford-cars-data-set
