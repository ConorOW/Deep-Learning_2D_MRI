# Deep Learning classification tasks using 2D MRI data
A series of workbooks and scripts detailing various science projects.

The `midAxes_extraction.py` script is a tool that we can use to extract 2D niftis or 2D pngs from a 3D brain image, by finding the mid-point along each axis. This can be useful for machine learning tasks such as those in this repo where we require a 2D images.

The `SwimViT.ipynb` notebook demonstrates a vision transformer which is able to detect Alzheimer's disease from a 2D MRI image. It was trained on ImageNet-1k at resolution 224x224. The Swim Transformer is different from a traditional vision transformer in that it incorporates a hierarchical shifted windowing scheme which provides greater efficiency by limiting self-attention computation to non-overlapping local windows.

The `VisionTransformer.ipynb` notebook demonstrates a vanilla vision transformer which is able to detech Alzheimer's disease from a 2D MRI image, pretrained on ImageNet-21k (14 million images, 21,843 classes) at resolution 224x224.
