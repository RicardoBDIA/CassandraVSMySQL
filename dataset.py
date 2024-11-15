import csv
from faker import Faker
import random
from tqdm import tqdm

NUM_RECORDS = 1000000
OUTPUT_FILE = 'data.csv'

fake = Faker()
emails = set()

with open(OUTPUT_FILE, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "email", "age"])  # Header
    
    count = 0
    with tqdm(total=NUM_RECORDS, desc="Generando datos", unit="registros") as pbar:
        while count < NUM_RECORDS:
            email = fake.email()
            if email not in emails:  # Verifica si el email ya existe
                emails.add(email)
                writer.writerow([
                    fake.name(),
                    email,
                    random.randint(0, 99)
                ])
                count += 1
                pbar.update(1)  # Actualiza la barra de progreso

print(f'{NUM_RECORDS} registros únicos generados en el archivo {OUTPUT_FILE}.')
