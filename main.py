import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

imgs = ['https://avatars.mds.yandex.net/i?id=a62083e2fa0d5aab9afb5d1dd1eca83f5769eafd-9066083-images-thumbs&n=13']  # batch of images

results = model(imgs)

results.print()
results.show()
