from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from applications.core.models import Doctor
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from applications.security.components.mixin_crud import PermissionMixin, DeleteViewMixin  # Asegúrate de que existan

class DoctorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Doctor
    template_name = 'core/doctor/list.html'
    context_object_name = 'doctores'
    paginate_by = 10
    permission_required = 'core.view_doctor'

    def get_queryset(self):
        q = self.request.GET.get("q", "")
        return Doctor.objects.filter(activo=True, nombres__icontains=q).order_by('apellidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Lista de Doctores"
        context['q'] = self.request.GET.get("q", "")
        return context


class DoctorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Doctor
    fields = '__all__'  # Reemplaza si quieres campos específicos
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')
    permission_required = 'core.add_doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nuevo Doctor"
        return context


class DoctorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Doctor
    fields = '__all__'
    template_name = 'core/doctor/form.html'
    success_url = reverse_lazy('core:doctor_list')
    permission_required = 'core.change_doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Doctor"
        return context


class DoctorDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Doctor
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:doctor_list')
    permission_required = 'core.delete_doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grabar'] = 'Eliminar Doctor'
        context['description'] = f"¿Desea eliminar al doctor '{self.object.nombre_completo}'?"
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        nombre = self.object.nombre_completo
        response = super().form_valid(form)
        messages.success(self.request, f"Doctor '{nombre}' eliminado con éxito.")
        return response
