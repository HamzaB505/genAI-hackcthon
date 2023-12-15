import pandas as pd 
import os

# GenAI libraries needed
from deep_translator import GoogleTranslator
from transformers import pipeline
from keras_cv.models import StableDiffusion
from PIL import Image
from transformers import VitsModel, AutoTokenizer
import torch
from IPython.display import Audio
import scipy
from transformers import AutoTokenizer, AutoModelWithLMHead
import torch
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

class AImodels_loader():

    
    def load_translator(self, language: str='en'):
        self.translator_eng = GoogleTranslator(source='auto', target=language)


    def load_bart_summarizer(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    

    def load_text_to_image(self,
                           img_height: int=512,
                           img_width: int=512,
                           jit_compile: bool=True):

        self.text_to_image_model = StableDiffusion(img_height=img_height,
                        img_width=img_width,
                        jit_compile=jit_compile)
        
    def load_narrator_model(self):
        self.narration_model = VitsModel.from_pretrained("facebook/mms-tts-ara")
        self.narration_tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-ara")

    def load_arabic_summarizer(self):
        # device setup
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        m_name = "marefa-nlp/summarization-arabic-english-news"
        # model definition
        self.summarizer_tokenizer_ar = AutoTokenizer.from_pretrained(m_name)
        self.summarizer_model_ar = AutoModelWithLMHead.from_pretrained(m_name).to(device)








