from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def operacao_matematica(request):
    if request.method == "POST":
        try:
            data = json.loads(requests.body)
            var1 = data.get('var1', None)
            var2 = data.get('var2', None)
            operacao = data.get('operacao', None)

            if var1 is not None and var2 is not None and operacao is not None:
                resultado = realiza_operacao(var1, var2, operacao)
                response_data = {'resultado': resultado}
                return JsonResponse(response_data)
            else:
                response_data = {'error': 'Variavel (var1, var2 ou operacao) não foi fornecida na requisição'}
                return JsonResponse(response_data, status=400)
        except Json.JSONDecodeError:
            response_data = {'error': 'Erro na requisição JSON'}
            return JsonResponse(response_data, status=400)
    else:
        response_data = {'error': 'Esta API aceita apenas requisições POST'}
        return JsonResponse(response_data, status=405)


def realiza_operacao(var1, var2, operacao):
    if operacao == 'soma':
        return var1 + var2
    elif operacao == 'subtracao':
        return var1 - var2
    elif operacao == 'multiplicacao':
        return var1 * var2
    elif operacao == 'divisao':
        if var1 != 0:
            return var1 / var2
        else:
            return 'Erro: divisao por zero'
    else:
        return 'Operação não suportada'
