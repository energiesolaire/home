from django.shortcuts import render, redirect, HttpResponse
from .models import Cliente, Leitura

def faturamento_medicao_lancar(request):
	if request.POST:
		id_cliente = request.POST.get("id_cliente")
		cliente = Cliente.objects.get(id_cliente=id_cliente)
		data = request.POST.get("data")
		leitura = request.POST.get("leitura")
		nova_leitura = Leitura(cliente = cliente, data = data, leitura = leitura)
		nova_leitura.save()
		html = "Salvo os seguintes dados:<BR>"
		html = html + "Identificador: " + cliente.id_cliente.__str__() + "<BR>"
		html = html + "Nome: " + cliente.nome + " " + cliente.sobrenome + "<BR>"
		html = html + "Data: " + nova_leitura.data.__str__() + "<BR>"
		html = html + "Leitura: " + nova_leitura.leitura.__str__() + "<BR>"
			
		return HttpResponse(html)
	else:
		return render(request, "faturamento/lanca_fatura.html")



