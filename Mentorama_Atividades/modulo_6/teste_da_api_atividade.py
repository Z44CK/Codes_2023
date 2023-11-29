from django.test import TestCase
from django.urls import reverse
import json


class operacaomatematicadaAPI(TestCase):
    def test_matematico_operacao_soma(self):
        data = {'var1': 5, 'var2': 8, 'operacao': 'soma'}
        response = self.client.post(reverse('operacao-matematica'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['resultado'], 13)

    def test_matematico_operacao_subtracao(self):
        data = {'var1': 12, 'var2': 6, 'operacao': 'subtracao'}
        response = self.client.post(reverse('operacao-matematica'), json.dumps(data), content_type='appliacation/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['resultado'], 6)

    def test_matematico_operacao_multiplicacao(self):
        data = {'var1': 3, 'vaar2': 15, 'operacao:': 'multiplicacao'}
        response = self.client.post(reverse('operacao-matematica'), json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['resultado'], 45)

    def test_matematico_operacao_divisao(self):
        data = {'var1': 6.2, 'var2': 5, 'operacao': 'divisao'}
        response = self.client.post(reverse('operacao-matematica'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.json()['resultado'], 1.24)
