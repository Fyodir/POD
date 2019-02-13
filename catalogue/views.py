from django.shortcuts import render
from django.views import generic
from catalogue.models import Team, Supplier, ProductType, Temperature, Storage, ProductInstance, Order, Requisition
from django.contrib.auth.mixins import LoginRequiredMixin

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
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class ProductTypeView(generic.ListView):
    model = ProductType
    paginate_by = 25
    # template_name = '/producttype.html'

class ProductTypeDetailView(LoginRequiredMixin,generic.DetailView):
    model = ProductType

class SupplierListView(generic.ListView):
    model = Supplier

class SupplierDetailView(LoginRequiredMixin,generic.DetailView):
    model = Supplier

# def supplier_detail_view(request, primary_key):
#     try:
#         supplier = Supplier.objects.get(pk=primary_key)
#     except Supplier.DoesNotExist:
#         raise Http404('Supplier does not exist')
#
#     return render(request, 'catalogue/supplier_detail.html', context={'supplier': supplier})

class TeamListView(generic.ListView):
    model = Team

class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team

class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order

class OrdersCreatedByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view orders created by current user."""
    model = Order
    template_name ='catalog/orders_created_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(orderer=self.request.user).order_by('date_created')

class RequisitionListView(LoginRequiredMixin, generic.ListView):
    model = Requisition

class RequisitionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Requisition
