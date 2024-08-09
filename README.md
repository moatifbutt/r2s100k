# R2S100K: Road-Region Segmentation Dataset For Semi-Supervised Autonomous Driving in the Wild [Accepted in IJCV 2024]
[Muhammad Atif Butt](https://scholar.google.com/citations?user=vf7PeaoAAAAJ&hl=en), [Hassan Ali](https://scholar.google.com/citations?user=MhiaZiQAAAAJ&hl=en), [Adnan Qayyum](https://scholar.google.com/citations?user=keWNlTIAAAAJ&hl=en),  [Waqas Sultani](https://scholar.google.com/citations?user=SqcjV8EAAAAJ&hl=en), [Ala Al-Fuqaha](https://scholar.google.com/citations?user=IKnfU2kAAAAJ&hl=en), and [Junaid Qadir](https://scholar.google.com/citations?user=EdPPQToAAAAJ&hl=en)

[[arXiv](https://arxiv.org/abs/2308.06393)] [[Project](https://r2s100k.github.io/)]


![teaser](assets/Dataset-Images-extended.jpg)
***TL;DB*** Examples of our dataset images covering a wide array of roadways, varying across different lighting and weather conditions. Instead of considering the whole paved road region as one class, we distinguish safe asphalt road region and its associated atypical classes found on unstructured roads such as distress, wet surface, gravel, boggy, vegetation misc., crag-stone, road grime, drainage grate, earthen, water puddle, misc., speed breakers, and concrete road patches.

# Installations (for local execution with PyTorch)
## Prerequisites
1. Windows
2. Anaconda Python
3. PyTorch (https://pytorch.org/get-started/locally/)
4. Albumentations (https://pypi.org/project/albumentations/), (pip install albumentations)
5. Tensorboard (https://pypi.org/project/tensorboard/), (pip install tensorboard)
6. TensorboardX (https://pypi.org/project/tensorboardX/), (pip install tensorboardX)

## Dataset 
We present a large-scale R2S100K dataset to train and evaluate supervised/semi-supervised methods in challenging road scenarios. You can send an email at 'matifbutt@outlook.com' to get access to our R2S100K dataset. Our labeled dataset contains over 14000 images with 14 diverse road region classes, which are enlisted below along with their definition.

![image](https://github.com/user-attachments/assets/fcae628b-2111-43a9-8c98-822f4b14fec2)

## Training
![teaser](assets/pipeline-1_.jpg)

***TL;DB*** Our Efficient Data Sampling (EDS) based self-training framework. Firstly, raw data samples are clustered based on similarity in road classes among image encodings — generated by an encoder. Then, a small subset is uniformly formed from all clusters for annotation to train the teacher model. After training, pseudo-labels of the unlabeled set are generated using the
teacher model, and the student model is trained on real and pseudo-labeled sets to achieve better generalization.

### Training Teacher Model
- Train the teacher model on the our labeled R2S100K dataset. Before starting training, place the downloaded dataset folders (train, train_labels, test, test_labels, val, and val_labels) in the data directory. After completion, verify the root paths and other configurations in 'config.py'.

```
python train.py --resume-training no
```

### Generating Psuedo-labels
- After training teacher model, pseudo-labels can be generated using following script. We will release our unlabeled data soon.

```
generate_pseudo_labels.ipynb
```

- Psuedo-labeled data can then be integrated with real-labeled data as terms the original data directory structure.

### Training Student Model
- After completion of pseudo-labeling, verify the root paths and other configurations in 'config.py'. Also, model can be changed in 'model.py'.

```
python train.py --resume-training no
```

## For Testing 

### Test the model on the image 

-  Use this python script to apply pixel level segmentation on any image of your choice.
```
python test_road_detection.py --model-path <path to saved checkpoint/weight file> --input <path to vid>.
```
example: python test.py --model-path model.pth --input abc.jpg

### Test the model on the video 

-  Use this python script to apply pixel level segmentation on any videos of your choice.
```
python test_vid.py --input <path to vid> --model-path <path to saved checkpoint/weight file>.
```
example: python test_vid.py --input <path_of_video>.mp4 --model-path model.pth

### Citation
```
@article{butt2023r2s100k,
  title={R2S100K: Road-Region Segmentation Dataset For Semi-Supervised Autonomous Driving in the Wild},
  author={Butt, Muhammad Atif and Ali, Hassan and Qayyum, Adnan and Sultani, Waqas and Al-Fuqaha, Ala and Qadir, Junaid},
  journal={arXiv preprint arXiv:2308.06393},
  year={2023}
}
```
