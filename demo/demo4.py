# Simple Seq2Seq
import torch.nn as nn

class Seq2Seq(nn.module):
    def __init__(self, input_size, hidden_size=128):
        self.encoder = nn.RNN(input_size, hidden_size)
        self.decoder = nn.RNN(hidden_size, 32)

    def forward(self, input_seq):
        hidden = self.encoder(input_seq)
        outputs = self.decoder(hidden)

        return outputs