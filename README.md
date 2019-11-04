# Projects
Repo with my current projects

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/morganmcg1/Projects/master)
  <- Launch Binder or share the [Binder link](https://mybinder.org/v2/gh/morganmcg1/Projects/master)

### [RangerQH_v2](https://github.com/morganmcg1/Projects/blob/master/RangerQH%20to%20fastai2%20-%20working.ipynb)
- My rough attempt at porting @lessw2020's RangerQH optimizer to fastaiv2 with super simple MNIST net for testing
- @lessw2020 fastaiv1 implementation here: https://github.com/lessw2020/Ranger-Deep-Learning-Optimizer/blob/master/rangerqh.py

### [Stanford Cars](https://github.com/morganmcg1/Projects/tree/master/stanford-cars)
- Fine-grained image classification of different car models (Stanford-Cars dataset)
- The goal of this series of notebooks is to achieve **90%+** accuracy using fastai
- My current best is **93.29%** accuracy 

### [Feature Testing](https://github.com/morganmcg1/Projects/tree/master/feature-testing)
- RGB Transforms: Tested whether different types of RGB transforms could improve validatoin accuracy for image classification. Randomly zeroing out 1 channel had the best improvement. Prompted after discussion on the fastai formum here: https://forums.fast.ai/t/rgb-transformations-for-data-augmentation/36876/8
- Achieved 1% increase in accuracy over baseline on Stanford-Cars dataset 

### Resources
Hows to customise the Fastai DataBlock: https://medium.com/@wgilliam/finding-data-block-nirvana-a-journey-through-the-fastai-data-block-api-c38210537fe4
