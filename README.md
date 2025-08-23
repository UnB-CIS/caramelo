# DogFaceNet

This code is an implementation of a deep learning method for dog identification. It relies on the triplet loss defined in FaceNet paper and on novel deep learning techniques as ResNet networks.

Dog faces pictures were retrieved from the web and aligned using three handmade labels. The dataset is available here: [Zenodo](https://zenodo.org/records/12578449)

### Run the recognition algorithm

To create a virtual environment, run:

```bash
python -m venv venv
```

Then activate it:

On Linux/Mac:
```bash
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

After creating a virtual environment, the dependencies should be installed with:

```bash
pip install -r requirements.txt
```

Then run the following command from the root directory of the project:

```bash
python dogfacenet/dogfacenet.py
```

To run properly the dataset has to be located in a data/dogfacenet folder or you will have to edit the config part of the dogfacenet.py file.

The above command will train a model and save it into output/model directory. It will also save its history in output/history.

### Contents

This project is organized as follows:

```
dogs_recognition/
├── data/
├── doc/
├── dogfacenet/
│   ├── __init__.py
│   ├── dogfacenet.py
│   ├── offline_training.py
│   └── online_training.py
├── output/
│   ├── model/
│   └── history/
├── requirements.txt
└── README.md
```

The stable version of the DogFaceNet is located at the dogfacenet folder. The files are arranged as the following:

* dogfacenet: dataset loading, model definiton and training
* offline/online_training: function for triplet generation

The rest of the project contains:

* output:
    * model: the trained models
    * history: the convergence curves and training history

### References

This repository is based on the first implementation of the dogFaceNet, by [Guillaume Mougeot](https://github.com/GuillaumeMougeot), wich is provided by [this link](https://github.com/GuillaumeMougeot/DogFaceNet)
