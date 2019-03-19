from django.test import TestCase
from django.urls import reverse

from catalogue.models import *

class SupplierListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_suppliers = 13

        for supplier_id in range(number_of_suppliers):
            Supplier.objects.create(
                name=f'Christian {supplier_id}',
                phone=f'014938746578 {supplier_id}',
                email=f'Christian@test.co.uk {supplier_id}',
                agent=f'Benedict {supplier_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalogue/supplier/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('supplier'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('supplier'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/supplier_list.html')

    def test_pagination_is_thirty(self):
        response = self.client.get(reverse('supplier'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['supplier_list']) == 30)

    def test_lists_all_suppliers(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('supplier')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['author_list']) == 3)
