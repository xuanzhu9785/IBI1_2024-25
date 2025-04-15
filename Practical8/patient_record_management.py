class patients:
    def __init__(individual, name, age, date_of_latest_admission, medical_history):
        individual.name = name
        individual.age = age
        individual.date_of_latest_admission = date_of_latest_admission
        individual.medical_history = medical_history

    def print_record(individual):
        print(f"{individual.name}, Age: {individual.age}, Admitted: {individual.date_of_latest_admission}, History: {individual.medical_history}")
patient1 = patients("Xuanzhu Chen", 18, "2025-04-08", "cold")
patient1.print_record()