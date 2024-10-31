import csv
from faker import Faker
import random

NUM_RECORDS = 10
OUTPUT_FILE = 'data.csv'

fake = Faker()
emails = set()

with open(OUTPUT_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "email", "age"])  # Header
    
    count = 0
    while count < NUM_RECORDS:
        email = fake.email()
        if email not in emails:  # Verifica si el email ya existe
            emails.add(email)  # Añade el email al conjunto para evitar duplicados
            writer.writerow([
                fake.name(),
                email,
                random.randint(0, 99)
            ])
            count += 1

print(f'{NUM_RECORDS} registros únicos generados en el archivo {OUTPUT_FILE}.')