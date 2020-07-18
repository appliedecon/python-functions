formulas = {
    'f1': {'i1':50, 'f2':50},
    'f2': {'i2':50, 'i3':40, 'f3':10},
    'f3': {'i3':10, 'i4':30, 'i5':30, 'i6':30}
}

def expand(formulas):

    from collections import defaultdict
    n_formulas = defaultdict(dict)

    for f in formulas.keys():
        new_formulas = []
        for ingr in formulas[f].keys():
            if ingr in formulas.keys():
                scalar = formulas[f][ingr] / 100
                new_formulas = list( {k:v*scalar for k,v in formulas[ingr].items()}.items() )
            else:
                n_formulas[f][ingr] = formulas[f][ingr]
        for item in new_formulas:
            n_formulas[f][item[0]] = n_formulas[f].get(item[0], 0) + item[1]
        
    return n_formulas

def full_expand(formulas):
    cont = True
    while cont:
        cont = False
        formulas = expand(formulas)
        for f in formulas.keys():
            for i in formulas[f].keys():
                if i in formulas.keys():
                    cont = True
    return formulas

print(full_expand(formulas))