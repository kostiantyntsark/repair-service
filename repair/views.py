from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, Device, RepairOrder
from .forms import DeviceForm, RepairOrderForm


def service_list(request):
    services = Service.objects.all()
    return render(request, 'repair/service_list.html', {'services': services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'repair/service_detail.html', {'service': service})


def contacts(request):
    return render(request, 'repair/contacts.html')


@login_required
def device_list(request):
    devices = Device.objects.filter(owner=request.user)
    return render(request, 'repair/device_list.html', {'devices': devices})


@login_required
def device_create(request):
    form = DeviceForm(request.POST or None)
    if form.is_valid():
        device = form.save(commit=False)
        device.owner = request.user
        device.save()
        return redirect('device_list')
    return render(request, 'repair/device_form.html', {'form': form})


@login_required
def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk, owner=request.user)
    if request.method == 'POST':
        device.delete()
        return redirect('device_list')
    return render(request, 'repair/device_confirm_delete.html', {'device': device})



@login_required
def order_list(request):
    orders = RepairOrder.objects.filter(device__owner=request.user)
    return render(request, 'repair/order_list.html', {'orders': orders})


@login_required
def order_create(request):
    form = RepairOrderForm(request.POST or None)
    form.fields['device'].queryset = Device.objects.filter(owner=request.user)
    if form.is_valid():
        form.save()
        return redirect('order_list')
    return render(request, 'repair/order_form.html', {'form': form})


@login_required
def order_detail(request, pk):
    order = get_object_or_404(RepairOrder, pk=pk, device__owner=request.user)
    return render(request, 'repair/order_detail.html', {'order': order})