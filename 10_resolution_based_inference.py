# 10. Resolution-Based Inference for Medical Diagnosis

def resolve(c1, c2):
    for x in c1:
        opposite = '~' + x if not x.startswith('~') else x[1:]
        if opposite in c2:
            return (c1 | c2) - {x, opposite}
    return None

c1 = {'fever'}
c2 = {'~fever', 'flu'}

result = resolve(c1, c2)
print("Inferred diagnosis:", result)
