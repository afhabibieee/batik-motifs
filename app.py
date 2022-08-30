import streamlit as st
import torch
from torchvision import models
import matplotlib.pyplot as plt
from PIL import Image
from process import predict

device = 'cuda' if torch.cuda.is_available() else 'cpu'

num_classes = 15
pretrained = models.efficientnet_b0(weights='IMAGENET1K_V1')

class MyEfficientNet(torch.nn.Module):
  def __init__(self, pretrained, num_classes=num_classes):
    super(MyEfficientNet, self).__init__()
    self.pretrained = pretrained
    self.classifier_layer = torch.nn.Sequential(
        torch.nn.Linear(1280 , 512),
        torch.nn.BatchNorm1d(512),  
        torch.nn.Dropout(0.7),
        torch.nn.Linear(512 , 256),
        torch.nn.Dropout(0.5),
        torch.nn.Linear(256 , num_classes)
    )
  def forward(self, x):
    x = self.pretrained.features(x)
    x = self.pretrained.avgpool(x)
    x = x.view(x.size(0), -1)
    x = self.pretrained.classifier[0](x)
    x = self.classifier_layer(x)
    return x

MODEL_PATH = 'model.pth'

model = torch.load(MODEL_PATH, map_location=torch.device(device))

st.title('Batik Motif Classification')

st.markdown(
    'This is a web application that can classify 15 kinds of batik motifs.'
)
st.markdown('---')

motif = st.markdown(
    f"<h1 style='text-align: center; color: red;'>Hmm, did you upload the picture?</h1>", 
    unsafe_allow_html=True
)

st.markdown('---')

img_file_buffer = st.file_uploader(
    "Upload an image", 
    type=[ "jpg", "jpeg",'png']
)

if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    #model = torch.jit.load(MODEL_PATH)
    batik_name = predict(model, image, device)

    #st.image(image)
    
    motif.write(
        f"<h1 style='text-align: center; color: green;'>{batik_name}</h1>", 
        unsafe_allow_html=True
    )

    p = plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('off')
    st.pyplot(p)