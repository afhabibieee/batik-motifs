import torch
from torchvision import transforms as T

MEAN = [0.5205, 0.4397, 0.4213]
STD = [0.2361, 0.2329, 0.2218]

image_transform = T.Compose([
    T.Resize(224),
    T.ToTensor(),
    T.Normalize(MEAN, STD)
])

class_dec = {
    0:'Batik Sekar Jagad',
    1:'Batik Poleng',
    2:'Batik Pala',
    3:'Batik Tambal',
    4:'Batik Geblek Renteng',
    5:'Batik Parang',
    6:'Batik Megamendung',
    7:'Batik Dayak',
    8:'Batik Ikat Celup',
    9:'Batik Insang',
    10:'Batik Kawung',
    11:'Batik Bali',
    12:'Batik Betawi',
    13:'Batik Lasem',
    14:'Batik Cendrawasih'
}

def predict(model, image, device):
    
    image_tensor = image_transform(image)
    
    model.eval()
    with torch.no_grad():
        # adjust input dimensions
        image_tensor = image_tensor.unsqueeze(0).to(device)

        output = model(image_tensor)
        pred = torch.argmax(torch.nn.functional.softmax(output, dim=1)).cpu().item()

    return class_dec[pred]