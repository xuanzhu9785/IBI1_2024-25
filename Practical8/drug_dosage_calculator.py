def calculator(weight, paracetamol):
    if weight<10 or weight>100:
        return False
    if paracetamol not in [120,250]:
        return False
    dose_mg=15*weight #mg
    volume_ml=(dose_mg*5)/paracetamol
    return volume_ml
print("Dose needed:", calculator(20, 120), "ml")