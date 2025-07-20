# DogFaceNet

This code is an implementation of a deep learning method for dog identification. It relies on the triplet loss defined in FaceNet paper and on novel deep learning techniques as ResNet networks.

Dog faces pictures were retrieved from the web and aligned using three handmade labels. We used VIA tool to label the images. The dataset is available here: [Zenodo](https://zenodo.org/records/12578449)

### Dataset

The complete dataset is now available on [Zenodo](https://zenodo.org/records/12578449).

### Run the recognition algorithm

To run the code you will need:
* python >= 3.6.4
* tensorflow == 1.12.0 (this constraint will be improved)
* numpy >= 1.14.0
* matplotlib >= 2.1.2
* scikit-image >= 0.13.1
* jupyter >= 1.0.0 (optional: only for dev)
* tqdm >= 4.23.4 (optional: only for dev)

Then run the following command from the root directory of the project:

    python dogfacenet/dogfacenet.py

To run properly the dataset has to be located in a data/dogfacenet folder or you will have to edit the config part of the dogfacenet.py file.

The above command will train a model and save it into output/model directory. It will also save its history in output/history.

### Content

As previously described, the stable version is in dogfacenet/dogfacenet.py. It contains:

* the online and offline training modules
* the model definition and training
* the model evaluation (still in development)

The dogfacenet-dev folder contains the developer version of the code. Model evaluation (verification, recognition, clustering, ROC curve, observation on the heatmap, ...) is in developer folder. It will be transfer in stable folder soon. The main dev version is in dogfacenet-dev/dogfacenet_v12-dev.ipynb jupyter notebook file.

The rest of the project contains:

* (data: the images of the project) not available right now...
* dogfacenet: stable version of the DogFaceNet project.
    * dogfacenet: dataset loading, model definiton and training
    * offline/online_training: function for triplet generation
* dogfacenet-dev: the main part, it contains the code on dog face verification and on face alignment (in dogfacenet/labelizer).
    * labelizer: contains the data-preprocessing function after labeling the images using VIA
        * copy_images: copies the images from the output folder of VIA to the input folder of DogFaceNet
        * transform_csv_to_clean_format: edits the output csv file from VIA to a adapted format
        * align_face: aligns copied faces using the edited csv file
    * dogfacenet-*dataset*: different tries on different dataset 
    * dogfacenet_v*version_number*: the different version of the code on dog pictures
    * triplet_preprocessing: triplets linked functions
        * triplets definition
        * triplets augmentation
        * hard triplets definition
* output:
    * (model: the trained models not available right now...)
    * history: the convergence curves

### References

This repository is based on the first implementation of the dogFaceNet, by [Guillaume Mougeot](https://github.com/GuillaumeMougeot), wich is provided by [this link](https://github.com/GuillaumeMougeot/DogFaceNet)
