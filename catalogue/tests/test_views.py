from django.test import TestCase
from django.urls import reverse

from catalogue.models import *

class SupplierrListViewTest(TestCase):
    @classmethod
    def setUp(self):

        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        # Create 33 suppliers for pagination tests
        number_of_suppliers = 33
        for supplier_id in range(number_of_suppliers):
            Supplier.objects.create(
                name=f'Christian {supplier_id}',
                phone=f'0987654321234567 {supplier_id}',
                email=f'Christian@test.com {supplier_id}',
                agent=f'Surname {supplier_id}',
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('supplier'))
        self.assertRedirects(response, '/accounts/login/?next=/catalogue/supplier/')


    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('supplier'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'catalogue/supplier_list.html')

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/catalogue/supplier/')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('supplier'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('supplier'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/supplier_list.html')

    def test_pagination_is_thirty(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('supplier'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['supplier_list']) == 30)

    def test_lists_all_suppliers(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('supplier')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['supplier_list']) == 3)




import uuid

from django.contrib.auth.models import Permission # Required to grant the permission needed to set a book as returned.

class ProductTypeCreateViewTest(TestCase):
    def setUp(self):
        # Create a user
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        # Adds product type creation priviledge only to test_user2
        permission = Permission.objects.get(name='Able to Create New Product Type')
        test_user2.user_permissions.add(permission)
        test_user2.save()

        # Create a product type
        test_supplier = Supplier.objects.create(name='Illumina')
        test_product_type = ProductType.objects.create(
            name='Fiffle Valve',
            supplier=test_supplier,
            description='My product summary',
            product_EROS='ABCDEFG',
            price=2346,
            lead_time=14,
        )

        # # Create genre as a post-step
        # genre_objects_for_book = Genre.objects.all()
        # test_book.genre.set(genre_objects_for_book) # Direct assignment of many-to-many types not allowed.
        # test_book.save()

        # Create a BookInstance object for test_user1
        # return_date = datetime.date.today() + datetime.timedelta(days=5)
        # self.test_bookinstance1 = BookInstance.objects.create(
        #     book=test_book,
        #     imprint='Unlikely Imprint, 2016',
        #     due_back=return_date,
        #     borrower=test_user1,
        #     status='o',
        # )
        #
        # # Create a BookInstance object for test_user2
        # return_date = datetime.date.today() + datetime.timedelta(days=5)
        # self.test_bookinstance2 = BookInstance.objects.create(
        #     book=test_book,
        #     imprint='Unlikely Imprint, 2016',
        #     due_back=return_date,
        #     borrower=test_user2,
        #     status='o',
        # )
