# Experiments

In this folder, important files connected to the conducted experiments can be found. 

Each subdirectory contains a short description of the experiment, progress file(s) that contain the training progress (loss, MSE, VLB, steps, samples, ...) and scripts that were used for training and sampling (i.e. contain the experiment specific parameter settings used).

Here is an overview over the conducted BraTS-experiments and their hyperparameter settings (bs = batch size, lr = learning rate).

<br> 

**1-Channel-Models:**
1. Experiment [bs=1, steps=100K, ~5 epochs, w/o BraTS loader, GeForce RTX 3060 Ti]
2. Experiment [bs=1, steps=230K, ~10 epochs, w/ BraTS loader, GeForce RTX 3060 Ti]

<br> 

**2-Channel-Models (T1CE incl. Segmentation):**
1. Experiment [bs=1, steps=250K, ~10 epochs, GeForce RTX 3060 Ti]
2. Experiment [bs=6, steps=160K, ~40 epochs, GeForce RTX 3090]
3. Experiment [bs=6, steps=220K, ~65 epochs, GeForce RTX 3090, decreased lr]
4. Experiment [bs=128 (microbatching), steps=60K, ~327 epochs, GeForce RTX 3090]

<br> 

**5-Channel-Model:**
1. Experiment [bs=128 (microbatching), steps=45K, ~247 epochs, GeForce RTX 3090]
