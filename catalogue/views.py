from django.shortcuts import render, get_object_or_404
from django.views import generic
from catalogue.models import Team, Supplier, ProductType, Temperature, Storage, ProductInstance, Order, Requisition
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_prod = ProductType.objects.all().count()
    num_instances = ProductInstance.objects.all().count()
    num_suppliers = Supplier.objects.count()

    # Requisitions
    num_req_incomplete = Requisition.objects.filter(requisition_status__exact='incomplete').count()
    num_req_awaiting = Requisition.objects.filter(requisition_status__exact='awaiting_auth').count()
    num_req_sent = Requisition.objects.filter(requisition_status__exact='sent').count()
    num_orders_no_req = Order.objects.filter(requisition_id__isnull=True).count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_prod': num_prod,
        'num_instances': num_instances,
        'num_req_incomplete': num_req_incomplete,
        'num_req_awaiting': num_req_awaiting,
        'num_req_sent': num_req_sent,
        'num_suppliers': num_suppliers,
        'num_visits': num_visits,
        'num_orders_no_req': num_orders_no_req,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# Views to display list and detail pages

class ProductTypeView(LoginRequiredMixin, generic.ListView):
    model = ProductType
    paginate_by = 25

class ProductTypeDetailView(LoginRequiredMixin,generic.DetailView):
    model = ProductType


class ProductInstanceListView(LoginRequiredMixin, generic.ListView):
    model = ProductInstance
    paginate_by = 25

class ProductInstanceDetailView(LoginRequiredMixin,generic.DetailView):
    model = ProductInstance


class SupplierListView(LoginRequiredMixin, generic.ListView):
    model = Supplier

class SupplierDetailView(LoginRequiredMixin,generic.DetailView):
    model = Supplier


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team

class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order

class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order


class RequisitionListView(LoginRequiredMixin, generic.ListView):
    model = Requisition

class RequisitionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Requisition


class StorageListView(LoginRequiredMixin, generic.ListView):
    model = Storage

class StorageDetailView(LoginRequiredMixin, generic.DetailView):
    model = Storage

# Views to display user specific pages

class OrdersCreatedByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view orders created by current user."""
    model = Order
    template_name ='catalogue/orders_created_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(orderer=self.request.user).order_by('date_created')

# Views for database manipulation forms

from catalogue.forms import UpdateProductInstanceStockForm

# Update stock of a product instance  (via product instance only)
def productinstance_stock_update(request, pk):
    productinstance = get_object_or_404(ProductInstance, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = UpdateProductInstanceStockForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model stock_level field)
            productinstance.stock = form.cleaned_data['stock_level']
            productinstance.save()
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('productinstance'))
    # If this is a GET (or any other method) create the default form.
    else:
        default_stock = 0
        form = UpdateProductInstanceStockForm(initial={'stock_level': default_stock})

    context = {
        'form': form,
        'productinstance': productinstance,
    }
    return render(request, 'catalogue/productinstance_stock_update.html', context)
