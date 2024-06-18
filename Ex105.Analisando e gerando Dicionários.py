def notas(*n, sit=False):
    d = dict()
    d['Total'] = len(n)
    d['Maior'] = max(n)
    d['Menor'] = min(n)
    d['Média'] = sum(n)/len(n)
    if sit:
        if d['Média'] >= 7:
            d['Situação'] = 'APROVADO!'
        elif d['Média'] >= 5:
            d['Situação'] = 'RECUPERAÇÃO!'
        else:
            d['Situação'] = 'REPROVADO!'
    return d


resp = notas(2.6, 6, 8.5, sit=True)
print(resp)
