# SoftEng_image_model

## Object Detection with YOLOv5

Проект реализует детекцию объектов на изображениях с помощью модели [YOLOv5](https://github.com/ultralytics/yolov5) на базе PyTorch Hub.  
Модель предсказывает координаты объектов, их классы и уверенность.

---

## 🚀 Возможности
- Детекция объектов на изображениях и URL-ссылках.
- Поддержка пакетной обработки (batch) изображений.
- Вывод результатов на экран и визуализация с рамками (bounding boxes).
- Использование предобученной модели `yolov5s`.

---

## 📦 Установка

1. Клонируем репозиторий (если есть) и переходим в папку:
```bash
git clone https://github.com/Alwaline/SoftEng_image_model.git
cd SoftEng_image_model
````

2. Устанавливаем зависимости (рекомендуется использовать виртуальное окружение):

```bash
pip install -r requirements.txt
```

---

## ▶️ Запуск

Пример скрипта `main.py`:

```python
import torch

# Загружаем модель
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Список изображений
imgs = ['https://avatars.mds.yandex.net/i?id=a62083e2fa0d5aab9afb5d1dd1eca83f5769eafd-9066083-images-thumbs&n=13']

# Детекция объектов
results = model(imgs)

# Вывод результатов
results.print()
results.show()
```

---

## 📑 Пример вывода

```
image 1/1: 640x640 1 person, 1 cell phone
Speed: 20ms pre-process, 30ms inference, 5ms NMS
```

На изображении будут визуально показаны bounding boxes для обнаруженных объектов.

---

## 🛠 Стек технологий

* Python 3.9+
* PyTorch
* YOLOv5
* Matplotlib (для визуализации результатов)

---

## 📌 TODO

* Поддержка видео и потокового детектирования.
* Сохранение изображений с рамками на диск.
* Интеграция с веб-приложением для онлайн детекции.


