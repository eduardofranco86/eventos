from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request, "home.html")


from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def cadastro(request):
    print("Método da requisição", request.method)
    print("Dados passados pelo POST: ", request.POST)

    for key, value in request.POST.items():
        print(f"Chave: {key}, Valor: {value}")

    nome = request.POST.get("nome")  
    idade = request.POST.get("idade")
    cidade = request.POST.get("cidade")

    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)

    # http://127.0.0.1:8000/cadastro/?nome=Maria&idade=50&cidade=São+Paulo
    # path("cadastro/", cadastro, name="cadastro")
    # conda install curl 
    # curl "http://127.0.0.1:8000/cadastro/?nome=Maria&idade=50&cidade=São+Paulo"
    
    return HttpResponse("Página de cadastro de usuário")