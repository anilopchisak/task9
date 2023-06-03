from django.test import TestCase, Client
from django.urls import reverse
from core import factories

class WorkerTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.depart = factories.Department()
        self.position = factories.Position()
        self.worker = factories.Worker(position=self.position, depart=self.depart)


    def test_list_data(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(reverse('core:worker_detail'), kwargs={'pk':self.worker.pk})
        self.assertEqual(response.status_code, 200)

    def test_update(self):
        data = {
            'name': 'test',
            'surname': 'test2',
            'depart': self.depart,
            'position': self.position,
            'phone': '0000000000',
            'email': 'test@mail.com',
            'kpi': '0'
        }
        response = self.client.post(path=reverse('core:worker_update'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        data = {
            'name': 'test',
            'surname': 'test2',
            'depart': self.depart,
            'position': self.position,
            'phone': '0000000000',
            'email': 'test@mail.com',
            'kpi': '0'
        }
        response = self.client.post(path=reverse('core:worker_create'), data=data, follow=True)
        self.assertEqual(response.status_code, 200)