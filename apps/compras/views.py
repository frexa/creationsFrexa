from django.shortcuts import render, get_object_or_404
from django.urls import*
from django.contrib.auth.mixins import*
from django.http import*
from apps.compras.forms import*
from apps.compras.models import*
from django.views.generic import*
from django.views.generic.detail import*
from apps.compras.reportes.reportes_compras_semanales import ReporteComprasSemanales
# Create your views here.
def index(request):
	ingrediente = Ingrediente.objects.filter(status__iexact='D').count()
	numero_visitas = request.session.get('numero_visitas',0)
	request.session['numero_visitas'] = numero_visitas+1
	return render(request,'index.html', {'ingrediente':ingrediente,
										'numero_visitas':numero_visitas})

def reporte_compras_semanales(request):
	response = HttpResponse(content_type='aplication/pdf')
	response['Content-Disposition']='attachment;filename="comprassemanales.pdf"'
	report = ReporteComprasSemanales()
	response.write(report.run())
	return response

class RegistrarFecha(CreateView):
	"""docstring for RegistrarCompra"""
	model = FechaDeCompra
	template_name = 'CrearCompra.html'
	form_class = FechaDeCompraForm
	success_url = 'fecha'

	def get_context_data(self, **kwargs):
		context = super(RegistrarFecha,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.model_form(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			compra = form.save(commit=False)
			compra.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class ActualizarFecha(UpdateView):
	"""docstring for ActualizarCompra"""
	model = FechaDeCompra
	template_name = 'CrearCompra.html'
	form_class = FechaDeCompraForm
	success_url = 'fecha'

	def get_context_data(self, **kwargs):
		context = super(ActualizarFecha,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.model_form(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			compra = form.save(commit=False)
			compra.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))


class RegistrarLineaCompra(CreateView):
	"""docstring for RegistrarCompra"""
	model = LineaDeCompra
	template_name = 'CrearLineaDeCompra.html'
	form_class = LineaDeCompraForm
	success_url = 'compra'

	def get_context_data(self, **kwargs):
		context = super(RegistrarLineaCompra,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			lineacompra = form.save(commit=False)
			lineacompra.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class ActualizarLineaCompra(UpdateView):
	"""docstring for ActualizarLineaCompra"""
	model = LineaDeCompra
	template_name = 'CrearLineaDeCompra.html'
	form_class = LineaDeCompraForm
	success_url = 'compra'

	def get_context_data(self, **kwargs):
		context = super(ActualizarLineaCompra,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			lineacompra = form.save(commit=False)
			lineacompra.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class RegistrarIngrediente(CreateView):
	"""docstring for RegistrarCompra"""
	model = Ingrediente
	template_name = 'CrearIngrediente.html'
	form_class = IngredienteForm
	success_url = 'ingrediente'

	def get_context_data(self, **kwargs):
		context = super(RegistrarIngrediente,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			ingrediente = form.save(commit=False)
			ingrediente.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class ActualizarIngrediente(UpdateView):
	"""docstring for ActualizarIngrediente"""
	model = Ingrediente
	template_name = 'CrearIngrediente.html'
	form_class = IngredienteForm
	success_url = 'ingrediente'

	def get_context_data(self, **kwargs):
		context = super(ActualizarIngrediente,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			ingrediente = form.save(commit=False)
			ingrediente.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))


class EliminarFecha(DeleteView):
	"""docstring for Eliminar"""
	model = FechaDeCompra
	template_name = 'EliminarCompra'
	reverse_lazy('/')
class EliminarLineaCompra(DeleteView):
	"""docstring for Eliminar"""
	model = LineaDeCompra
	template_name = 'EliminarLinea'
	reverse_lazy('/')
class EliminarIngrediente(DeleteView):
	"""docstring for Eliminar"""
	model = Ingrediente
	template_name = 'EliminarIngrediente'
	reverse_lazy('/')

class ListarCompras(ListView):
	model = FechaDeCompra
	template_name = 'compras_diarias.html'

class DetallesCompra(SingleObjectMixin,ListView):
	template_name = 'detalles_compra.html'
	paginate_by = 5
	
	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset = FechaDeCompra.objects.all())
		return super(DetallesCompra,self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(DetallesCompra,self).get_context_data(**kwargs)
		context['fechadecompra'] = self.object
		return context

	def get_queryset(self):
		return self.object.lineadecompra_set.all()
