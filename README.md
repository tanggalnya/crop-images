# Crop

## Prerequire
1. Use virtualenv and install dependencies needed
    ```sh
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

1. Copy config_sample.yaml to config.yaml and update value respectively

## Usage
It detected file mode from args width and height and only process image with same mode.

1. One file
    - Potrait
    ```python
    python crop.py -w 500 -h 692 -i sample_potrait.png
    ```
    - Landscape
    ```python
    python crop.py -w 800 -h 539 -i sample_landscape.jpeg
    ```

1. Bulk
    - Potrait
    ```python
    python crop.py -w 500 -h 692 -p "."
    ```
    - Landscape
    ```python
    python crop.py -w 800 -h 539 -p "."
    ```

New file will exist with suffix `_thumbnail`

### Links
- https://www.holisticseo.digital/python-seo/resize-image/
- https://www.tutorialspoint.com/python_pillow/python_pillow_creating_thumbnails.htm
