# rasbObjectDetection
Applying an object detection model to Raspberry Pi
### Step 1: 
Install all dependencies onto raspberry Pi These are the configs for a Pi 4 Model B
```
pip3 install opencv-python
sudo apt-get install libcblas-dev
sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-testv
```
### Step 2:
 Make sure the google apt-keys are correctly added
```echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
```

### Step 3:
Update your pi again
```
sudo apt-get update
sudo apt-get install
```

### Step 4: 
Install the tensor flow lite runtime enviornment on the pi

```
sudo apt-get install python3-tflite-runtime
```
