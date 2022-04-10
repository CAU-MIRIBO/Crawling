import torch
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration
from gensim.summarization.summarizer import summarize


class get_summarization:
    def __init__(self):
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained('digit82/kobart-summarization')
        self.model = BartForConditionalGeneration.from_pretrained('digit82/kobart-summarization')

    def summarization_KoBART(self, text):
        # print(text)
        raw_input_ids = self.tokenizer.encode(text)
        input_ids = [self.tokenizer.bos_token_id] + raw_input_ids + [self.tokenizer.eos_token_id]
        summary_ids = self.model.generate(torch.tensor([input_ids]), num_beams=4, max_length=512, eos_token_id=1)
        return self.tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)

    def summarization_newspaper(self, text):
        return summarize(text)