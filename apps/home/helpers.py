import datetime

def generate_serial_number():
    today = datetime.date.today()
    if today.month != generate_serial_number.last_month:
        print('change ok')
        generate_serial_number.counter = 1
        generate_serial_number.last_month = today.month
    serial_number = f"CLT{today.strftime('%Y%m')}-{generate_serial_number.counter:05}"
    generate_serial_number.counter += 1
    return serial_number

generate_serial_number.counter = 2  # Initialiser la variable de compteur
generate_serial_number.last_month = 4  # Initialiser la dernière date
