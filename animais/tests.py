from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Animal, Raca, TipoAnimal


class ListarAnimaisTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        tipo = TipoAnimal.objects.create(nome='Cachorro')
        cls.raca = Raca.objects.create(nome='Labrador', tipo_animal=tipo)
        outra_raca = Raca.objects.create(nome='Poodle', tipo_animal=tipo)
        Animal.objects.create(
            nome='Bidu',
            sexo='M',
            cor='Caramelo',
            raca=cls.raca,
            dataNascimento=date(2020, 1, 1),
        )
        Animal.objects.create(
            nome='Luna',
            sexo='F',
            cor='Branca',
            raca=outra_raca,
            dataNascimento=date(2021, 1, 1),
        )

    def test_lista_animais_e_exibida(self):
        response = self.client.get(reverse('animais:listaranimais'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bidu')
        self.assertContains(response, 'Luna')

    def test_exibe_foto_quando_animal_tem_imagem(self):
        Animal.objects.filter(nome='Bidu').update(
            foto='animais/fotos/bidu.png'
        )

        response = self.client.get(reverse('animais:listaranimais'))

        self.assertContains(
            response,
            '<img src="/media/animais/fotos/bidu.png" alt="Foto de Bidu"',
            html=False,
        )

    def test_filtra_por_nome(self):
        response = self.client.get(
            reverse('animais:listaranimais'), {'nome': 'bid'}
        )

        self.assertContains(response, 'Bidu')
        self.assertNotContains(response, 'Luna')

    def test_filtra_por_raca(self):
        response = self.client.get(
            reverse('animais:listaranimais'), {'raca': self.raca.pk}
        )

        self.assertContains(response, 'Bidu')
        self.assertNotContains(response, 'Luna')
