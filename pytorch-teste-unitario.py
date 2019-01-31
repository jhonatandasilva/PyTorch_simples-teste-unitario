from __future__ import print_function
import unittest

import torch 


def criar_tensor(linhas,colunas):
    tensor = torch.zeros(linhas,colunas)
    return tensor

class PyTorchTeste(unittest.TestCase):
    """ Criando um caso de teste para PyTorch """
    def teste_criar_tensor(self):
        tensor = criar_tensor(2,2)
        tensor_esperado = torch.zeros(2,2)
        tensor_ok = torch.equal(tensor,tensor_esperado)
        self.assertEqual(tensor_ok,True)