import torch
import streamlit as st

@st.cache
def get_model():
    return torch.hub.load("WongKinYiu/yolov7","custom","./best.pt",trust_repo=True)


def predict(image):
    model = get_model()
    return model(image)


def get_output_image(prediction):
    return prediction.render()[0]

def get_animals(prediction):
    animals_map = {0: "cat", 1: "dog"}
    animals_classes = prediction.xyxy[0][:,-1].tolist()

    return [animals_map[int(animal_class)] for animal_class in animals_classes]

def get_probabilities(prediction):
    return list(map(lambda proba: round(proba, ndigits=2),prediction.xyxy[0][:,-2].tolist()))


def get_text_description(prediction):
    description = ""
    animals = get_animals(prediction)
    probabilities = get_probabilities(prediction)

    for i, (animal, probability) in enumerate(zip(animals, probabilities),1):
        description += f"{i}- {animal} with probability {probability}\n"
    return description