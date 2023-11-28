import socket
import time
import random
import string

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("localhost", 12345))


def generate_random_message():
    # id,idExperiencia,nome,descricao,Tick,ax_raw,ay_raw,az_raw,ax_cook,ay_cook,az_cook,euler_x,euler_y,euler_z,alt_raw,alt_cook,latitude,longitude,drogue,main,state,avg_acc,Delta,idData_id
    id = random.randint(1, 100)
    idExperiencia = random.randint(1, 100)
    nome = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
    descricao = "".join(random.choices(string.ascii_uppercase + string.digits, k=5))
    Tick = random.randint(1, 100)
    ax_raw = random.uniform(-1, 1)
    ay_raw = random.uniform(-1, 1)
    az_raw = random.uniform(-1, 1)
    ax_cook = random.uniform(-1, 1)
    ay_cook = random.uniform(-1, 1)
    az_cook = random.uniform(-1, 1)
    euler_x = random.uniform(-1, 1)
    euler_y = random.uniform(-1, 1)
    euler_z = random.uniform(-1, 1)
    alt_raw = random.uniform(-1, 1)
    alt_cook = random.uniform(-1, 1)
    latitude = random.uniform(-1, 1)
    longitude = random.uniform(-1, 1)
    drogue = random.randint(1, 100)
    main = random.randint(1, 100)
    state = random.randint(1, 100)
    avg_acc = random.uniform(-1, 1)
    Delta = random.uniform(-1, 1)
    idData_id = random.randint(1, 100)
    return f"{id},{idExperiencia},{nome},{descricao},{Tick},{ax_raw},{ay_raw},{az_raw},{ax_cook},{ay_cook},{az_cook},{euler_x},{euler_y},{euler_z},{alt_raw},{alt_cook},{latitude},{longitude},{drogue},{main},{state},{avg_acc},{Delta},{idData_id}"


if __name__ == "__main__":
    while True:
        message = generate_random_message()
        socket.send(message.encode("utf-8"))
        # print(f"Sent: {message}")
        time.sleep(0.05)
