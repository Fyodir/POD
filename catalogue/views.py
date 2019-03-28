from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from catalogue.models import *
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalogue.forms import UpdateProductInstanceStockForm, OrderForm
from django.contrib.auth.models import User


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_prod = ProductType.objects.all().count()
    num_instances = ProductInstance.objects.all().count()
    num_suppliers = Supplier.objects.count()

    # Orders/Requisitions
    num_req_incomplete = Requisition.objects.filter(requisition_status__exact='To Order').count()
    num_order_incomplete = Order.objects.filter(order_status__exact='Order Created').count()
    num_order_sent = Order.objects.filter(order_status__exact='Order Sent').count()
    num_order_preceived = Order.objects.filter(order_status__exact='Part Received').count()
    num_order_issue = Order.objects.filter(order_issue__exact='Yes').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_prod': num_prod,
        'num_instances': num_instances,
        'num_suppliers': num_suppliers,
        'num_req_incomplete': num_req_incomplete,
        'num_order_incomplete': num_order_incomplete,
        'num_order_sent': num_order_sent,
        'num_order_preceived': num_order_preceived,
        'num_order_issue': num_order_issue,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# Views to display list and detail pages

class ProductTypeView(LoginRequiredMixin, generic.ListView):
    model = ProductType
    paginate_by = 30

class ProductTypeDetailView(LoginRequiredMixin,generic.DetailView):
    model = ProductType
    paginate_by = 30

#######################################

class ProductInstanceListView(LoginRequiredMixin, generic.ListView):
    model = ProductInstance
    paginate_by = 30

class ProductInstanceDetailView(LoginRequiredMixin,generic.DetailView):
    model = ProductInstance
    paginate_by = 30

#######################################

class SupplierListView(LoginRequiredMixin, generic.ListView):
    model = Supplier
    paginate_by = 30

class SupplierDetailView(LoginRequiredMixin,generic.DetailView):
    model = Supplier
    paginate_by = 30

#######################################

class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    paginate_by = 30

class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    paginate_by = 30

#######################################

class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    paginate_by = 30

class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order
    paginate_by = 30

#######################################

class RequisitionListView(LoginRequiredMixin, generic.ListView):
    model = Requisition
    paginate_by = 30

class RequisitionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Requisition
    paginate_by = 30

#######################################

class StorageListView(LoginRequiredMixin, generic.ListView):
    model = Storage
    paginate_by = 30

class StorageDetailView(LoginRequiredMixin, generic.DetailView):
    model = Storage
    paginate_by = 30

#######################################

class TemperatureListView(LoginRequiredMixin, generic.ListView):
    model = Temperature
    paginate_by = 30

class TemperatureDetailView(LoginRequiredMixin, generic.DetailView):
    model = Temperature
    paginate_by = 30


# # Views to display user specific pages
#
# class OrdersCreatedByUserListView(LoginRequiredMixin,generic.ListView):
#     """Generic class-based view orders created by current user."""
#     model = Order
#     template_name ='catalogue/orders_created_list_user.html'
#     paginate_by = 30
#
#     def get_queryset(self):
#         return Order.objects.filter(orderer=self.request.user).order_by('date_created')


# Update stock of a product instance  (via product instance)
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
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    # If this is a GET (or any other method) create the default form.
    else:
        default_stock = productinstance.stock
        form = UpdateProductInstanceStockForm(initial={'stock_level': default_stock})

    context = {
        'form': form,
        'productinstance': productinstance,
    }
    return render(request, 'catalogue/productinstance_stock_update.html', context)

#######################################

class SupplierCreate(PermissionRequiredMixin, CreateView):
    model = Supplier
    fields = '__all__'
    permission_required = 'catalogue.can_create_new_supplier'


class SupplierUpdate(PermissionRequiredMixin, UpdateView):
    model = Supplier
    fields = '__all__'
    permission_required = 'catalogue.can_update_supplier'


class SupplierDelete(PermissionRequiredMixin, DeleteView):
    model = Supplier
    permission_required = 'catalogue.can_delete_supplier'
    success_url = reverse_lazy('supplier')

#######################################

class ProductTypeCreate(PermissionRequiredMixin, CreateView):
    model = ProductType
    fields = '__all__'
    permission_required = 'catalogue.can_create_new_product_type'

class ProductTypeUpdate(PermissionRequiredMixin, UpdateView):
    model = ProductType
    fields = '__all__'
    permission_required = 'catalogue.can_update_product_type'

class ProductTypeDelete(PermissionRequiredMixin, DeleteView):
    model = ProductType
    permission_required = 'catalogue.can_delete_product_type'
    success_url = reverse_lazy('producttype')

#######################################

class RequisitionCreate(PermissionRequiredMixin, CreateView):
    model = Requisition
    # fields = ['req_ref', 'date_sent', 'requisition_status', 'comments']
    fields = '__all__'
    permission_required = 'catalogue.can_create_new_requisition'

class RequisitionUpdate(PermissionRequiredMixin, UpdateView):
    model = Requisition
    # fields = ['req_ref', 'date_sent', 'requisition_status', 'comments']
    fields = '__all__'
    permission_required = 'catalogue.can_update_requisition'

class RequisitionDelete(PermissionRequiredMixin, DeleteView):
    model = Requisition
    permission_required = 'catalogue.can_delete_requisition'
    success_url = reverse_lazy('requisition')

#######################################

class OrderCreate(PermissionRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    permission_required = 'catalogue.can_create_new_order'
    success_url = reverse_lazy('order')
    # success_url = reverse_lazy('requisition-detail', args=[str(model.id)])

    def form_valid(self, form):
        order = form.save(commit=False)
        order.orderer = User.objects.get(username=self.request.user)
        order.save()
        return HttpResponseRedirect(self.success_url)

class OrderUpdate(PermissionRequiredMixin, UpdateView):
    model = Order
    # form_class = OrderForm
    fields=[
        'team',
        'requisition_id',
        'product_type',
        'quantity',
        'urgency',
        'order_issue',
        'order_status',
        'comments',
        'date_delivered',
        'qc_status',
        'lot_id',
        'expiry_date'
    ]
    permission_required = 'catalogue.can_update_order'

class OrderDelete(PermissionRequiredMixin, DeleteView):
    model = Order
    permission_required = 'catalogue.can_delete_order'
    success_url = reverse_lazy('order')

#######################################

class TeamCreate(PermissionRequiredMixin, CreateView):
    model = Team
    fields = '__all__'
    permission_required = 'catalogue.can_create_new_team'

class TeamUpdate(PermissionRequiredMixin, UpdateView):
    model = Team
    fields = '__all__'
    permission_required = 'catalogue.can_update_team'

class TeamDelete(PermissionRequiredMixin, DeleteView):
    model = Team
    permission_required = 'catalogue.can_delete_team'
    success_url = reverse_lazy('team')

#######################################

class StorageCreate(PermissionRequiredMixin, CreateView):
    model = Storage
    fields = '__all__'
    permission_required = 'catalogue.can_create_new_storage'

class StorageUpdate(PermissionRequiredMixin, UpdateView):
    model = Storage
    fields = '__all__'
    permission_required = 'catalogue.can_update_storage'

class StorageDelete(PermissionRequiredMixin, DeleteView):
    model = Storage
    permission_required = 'catalogue.can_delete_storage'
    success_url = reverse_lazy('storage')

#######################################

class TemperatureCreate(PermissionRequiredMixin, CreateView):
    model = Temperature
    fields = '__all__'
    permission_required = 'catalogue.can_create_new_temperature'

class TemperatureUpdate(PermissionRequiredMixin, UpdateView):
    model = Temperature
    fields = '__all__'
    permission_required = 'catalogue.can_update_temperature'

class TemperatureDelete(PermissionRequiredMixin, DeleteView):
    model = Temperature
    permission_required = 'catalogue.can_delete_temperature'
    success_url = reverse_lazy('index')

#######################################

class ProductInstanceCreate(PermissionRequiredMixin, CreateView):
    model = ProductInstance
    fields = ['product_type', 'team', 'storage', 'stock', 'minimum_stock']
    permission_required = 'catalogue.can_create_new_product_instance'

class ProductInstanceUpdate(PermissionRequiredMixin, UpdateView):
    model = ProductInstance
    fields = ['product_type', 'team', 'storage', 'stock', 'minimum_stock']
    permission_required = 'catalogue.can_update_product_instance'

class ProductInstanceDelete(PermissionRequiredMixin, DeleteView):
    model = ProductInstance
    permission_required = 'catalogue.can_delete_product_instance'
    success_url = reverse_lazy('productinstance')
