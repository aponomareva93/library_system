from django.test import TestCase
from django.core.urlresolvers import reverse
from readers.models import Reader


class TestLogout(TestCase):
    def test_logout(self):
        reader1 = Reader.objects.get_or_create(username="Reader1")[0]
        reader1.set_password('12345')
        reader1.save()
        self.client.login(username='Reader1', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertContains(response, 'Вы успешно покинули систему')
