# Deep Learning classification tasks using 2D MRI data
A series of workbooks and scripts detailing various science projects.

The first notebook we have in here is the `Matplotlib Raincloud Plots.ipynb` which is a notebook showing some of the visualization methods we can use to display how the same variables appear at different sites in large international studies.

The second notebook `Multisite DTI harmonization.ipynb` shows a method, ComBat-GAM harmonization, and how it can be used to correct for some of the site-effects that exist in large multi-site studies. ComBat-GAM is able to reduce some of the variance in data that might be associated with factors we are not interested in, while at the same time retaining biological variance of interest.

The `SwimViT.ipynb` notebook demonstrates a vision transformer which is able to detect Alzheimer's disease from a 2D MRI image. It was trained on ImageNet-1k at resolution 224x224. The Swim Transformer is different from a traditional vision transformer in that it incorporates a hierarchical shifted windowing scheme which provides greater efficiency by limiting self-attention computation to non-overlapping local windows.

The `VisionTransformer.ipynb` notebook demonstrates a vanilla vision transformer which is able to detech Alzheimer's disease from a 2D MRI image, pretrained on ImageNet-21k (14 million images, 21,843 classes) at resolution 224x224.

The `midAxes_extraction.py` script is a tool that we can use to extract 2D niftis or 2D pngs from a 3D brain image, by finding the mid-point along each axis. This can be useful for machine learning tasks where we require a 2D image for some process.
