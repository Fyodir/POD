from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from catalogue.models import *
import random

####################################################################

# class indexViewTest(TestCase):

####################################################################

class ProductTypeViewTest(TestCase):
    @classmethod
    def setUp(self):

        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        # Create 33 suppliers for pagination tests
        number_of_producttypes = 33
        for producttype_id in range(number_of_producttypes):
            ProductType.objects.create(
                name=f'Pippette Tips {producttype_id}',
                supplier= Supplier.objects.create(name='Illumina {producttype_id}'),
                description=f'blah blah blah here is a description.com {producttype_id}',
                product_EROS=f'56F7D8S76F76H {producttype_id}',
                price=34.00,
                lead_time=21,
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('producttype'))
        self.assertRedirects(response, '/accounts/login/?next=/catalogue/producttype/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('producttype'))
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'catalogue/producttype_list.html')

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/catalogue/producttype/')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('producttype'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('producttype'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/producttype_list.html')

    def test_pagination_is_thirty(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('producttype'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['producttype_list']) == 30)

    def test_lists_all_product_types(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('producttype')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['producttype_list']) == 3)

####################################################################

# class ProductTypeDetailViewTest(TestCase):

####################################################################

# class ProductInstanceListViewTest(TestCase):  #ISSUE WITH THE "stock_updater" FIELD BEING PULLED FROM THE "auth.user" MODEL
#     @classmethod
#     def setUp(self):
#
#         # Create two users
#         test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
#         test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
#         test_user1.save()
#         test_user2.save()
#
#         # Create 33 productinstance for pagination tests
#         number_of_productinstances = 33
#         for productinstance_id in range(number_of_productinstances):
#             ProductInstance.objects.create(
#                 product_type=ProductType.objects.create(name='Test Product', price=34.00),
#                 id=f'90ec5d20-13a2-481e-8e76-ed3675bfce40',
#                 team= Team.objects.create(name='Lab Team Alpha {productinstance_id}'),
#                 storage= Storage.objects.create(name='Freezer Beta {productinstance_id}'),
#                 stock=12,
#                 minimum_stock=20,
#                 stock_updater= User.objects.create(username='testuser1', password='1X<ISRUkw+tuK'),
#                 date_updated=f'2019-01-01',
#             )
#
#     def test_redirect_if_not_logged_in(self):
#         response = self.client.get(reverse('productinstance'))
#         self.assertRedirects(response, '/accounts/login/?next=/catalogue/productinstance/')
#
#     def test_logged_in_uses_correct_template(self):
#         login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get(reverse('productinstance'))
#         # Check our user is logged in
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         # Check that we got a response "success"
#         self.assertEqual(response.status_code, 200)
#         # Check we used correct template
#         self.assertTemplateUsed(response, 'catalogue/productinstance_list.html')
#
#     def test_view_url_exists_at_desired_location(self):
#         login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get('/catalogue/productinstance/')
#         # Check our user is logged in
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         # Check that we got a response "success"
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_url_accessible_by_name(self):
#         login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get(reverse('productinstance'))
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get(reverse('productinstance'))
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'catalogue/productinstance_list.html')
#
#     def test_pagination_is_thirty(self):
#         login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get(reverse('productinstance'))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         self.assertTrue('is_paginated' in response.context)
#         self.assertTrue(response.context['is_paginated'] == True)
#         self.assertTrue(len(response.context['productinstance_list']) == 30)
#
#     def test_lists_all_product_types(self):
#         login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         # Get second page and confirm it has (exactly) remaining 3 items
#         response = self.client.get(reverse('productinstance')+'?page=2')
#         self.assertEqual(response.status_code, 200)
#         self.assertTrue('is_paginated' in response.context)
#         self.assertTrue(response.context['is_paginated'] == True)
#         self.assertTrue(len(response.context['productinstance_list']) == 3)

####################################################################

# class ProductInstanceDetailViewTest(TestCase):

####################################################################

class SupplierListViewTest(TestCase):
    @classmethod
    def setUp(self):

        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        # Create 33 producttypes for pagination tests
        number_of_suppliers = 33
        for supplier_id in range(number_of_suppliers):
            Supplier.objects.create(
                name=f'Christian {supplier_id}',
                phone=f'0987654321234567 {supplier_id}',
                email=f'Christian@test.com {supplier_id}',
                address=f'123 blah blah street {supplier_id}',
                comments=f'Here is a comment {supplier_id}',
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

####################################################################

# class SupplierDetailViewTest(TestCase):

####################################################################

class TeamListViewTest(TestCase):
    @classmethod
    def setUp(self):

        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        # Create 33 teams for pagination tests
        number_of_teams = 33
        for team_id in range(number_of_teams):
            Team.objects.create(
                name=f'Laboratory Team Alpha {team_id}',
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('team'))
        self.assertRedirects(response, '/accounts/login/?next=/catalogue/team/')


    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('team'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'catalogue/team_list.html')

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/catalogue/team/')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('team'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('team'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/team_list.html')

    def test_pagination_is_thirty(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('team'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['team_list']) == 30)

    def test_lists_all_product_types(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('team')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['team_list']) == 3)

####################################################################

# class TeamDetailViewTest(TestCase):

####################################################################

# class OrderListViewTest(TestCase):            #ISSUE WITH THE "orderer" FIELD BEING PULLED FROM THE "auth.user" MODEL

####################################################################

# class OrderDetailViewTest(TestCase):

####################################################################

class RequisitionListViewTest(TestCase):
    @classmethod
    def setUp(self):

        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        # Create 33 teams for pagination tests
        number_of_requisitions = 33
        for requisition_id in range(number_of_requisitions):
            creation_date = timezone.now() - datetime.timedelta(days=-7)
            Requisition.objects.create(
                req_ref=f'J5H6G7F8DSD7F6GH5-{requisition_id}',
                date_created=creation_date,
                date_sent=timezone.now(),
                requisition_status=f'To Order',
                comments='Here is some comments for the requisition ({requisition_id})',
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('requisition'))
        self.assertRedirects(response, '/accounts/login/?next=/catalogue/requisition/')


    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('requisition'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'catalogue/requisition_list.html')

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/catalogue/requisition/')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('requisition'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('requisition'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/requisition_list.html')

    def test_pagination_is_thirty(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('requisition'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['requisition_list']) == 30)

    def test_lists_all_requisitions(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('requisition')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['requisition_list']) == 3)

####################################################################

# class RequisitionDetailViewTest(TestCase):

####################################################################

class StorageListViewTest(TestCase):
    @classmethod
    def setUp(self):

        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        # Create 33 storage locations for pagination tests
        number_of_storage_locations = 33
        for storage_id in range(number_of_storage_locations):
            Storage.objects.create(
                name=f'Death Star Ice Cream Freezer',
                location=f'Death Star, room 66',
                temp_range=Temperature.objects.create(name='Hoth {producttype_id}', minimum=-100, maximum=-20),
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('storage'))
        self.assertRedirects(response, '/accounts/login/?next=/catalogue/storage/')


    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('storage'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'catalogue/storage_list.html')

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/catalogue/storage/')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('storage'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('storage'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/storage_list.html')

    def test_pagination_is_thirty(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('storage'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['storage_list']) == 30)

    def test_lists_all_storage_locations(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('storage')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['storage_list']) == 3)

####################################################################

# class StorageDetailViewTest(TestCase):

####################################################################

class TemperatureListViewTest(TestCase):
    @classmethod
    def setUp(self):

        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        # Create 33 storage locations for pagination tests
        number_of_temp_ranges = 33
        for temp_range_id in range(number_of_temp_ranges):
            minimum_temp = random.randint(-101,101)
            maximum_temp = minimum_temp + random.randint(1,21)
            Temperature.objects.create(
                name=f'Death Star Ice Cream Freezer',
                minimum=minimum_temp,
                maximum=maximum_temp,
            )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('temperature'))
        self.assertRedirects(response, '/accounts/login/?next=/catalogue/temperature/')


    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('temperature'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'catalogue/temperature_list.html')

    def test_view_url_exists_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/catalogue/temperature/')
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('temperature'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('temperature'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/temperature_list.html')

    def test_pagination_is_thirty(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('temperature'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['temperature_list']) == 30)

    def test_lists_all_temp_ranges(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('temperature')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['temperature_list']) == 3)

####################################################################

# class TemperatureDetailView(TestCase):

###############################################################################

# class productinstance_stock_updateTest(TestCase):

###############################################################################

# class SupplierCreateViewTest(TestCase):

####################################################################

# class SupplierUpdateViewTest(TestCase):

####################################################################

# class SupplierDeleteViewTest(TestCase):

####################################################################

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

####################################################################

# class ProductTypeUpdateViewTest(TestCase):

####################################################################

# class ProductTypeDeleteViewTest(TestCase):

####################################################################

# class RequisitionCreateViewTest(TestCase):

####################################################################

# class RequisitionUpdateViewTest(TestCase):

####################################################################

# class RequisitionDeleteViewTest(TestCase):

####################################################################

# class OrderCreateViewTest(TestCase):

####################################################################

# class OrderUpdateViewTest(TestCase):

####################################################################

# class OrderDeleteViewTest(TestCase):

####################################################################

# class TeamCreateViewTest(TestCase):

####################################################################

# class TeamUpdateViewTest(TestCase):

####################################################################

# class TeamDeleteViewTest(TestCase):

####################################################################

# class StorageCreateViewTest(TestCase):

####################################################################

# class StorageUpdateViewTest(TestCase):

####################################################################

# class StorageDeleteViewTest(TestCase):

####################################################################

# class TemperatureCreateViewTest(TestCase):

####################################################################

# class TemperatureUpdateViewTest(TestCase):

####################################################################

# class TemperatureDeleteViewTest(TestCase):

####################################################################

# class ProductInstanceCreateViewTest(TestCase):

####################################################################

# class ProductInstanceUpdateViewTest(TestCase):

####################################################################

# class ProductInstanceDeleteViewTest(TestCase):
