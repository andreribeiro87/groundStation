# Andre Ribeiro <andrepedroribeiro@ua.pt>
# Duarte Cruz <?>


import random
import string


"""This module contains a function that generates a random message string containing various random values.\n To simulate a message from rocket"""


def generate_random_message():
    """

        Use the random library\n
        Use String library\n
        Don't forgot to\n
        ```python
        import string
        import random
        ```\n
        Use like this:\n
        ```python
        import modules.randomData
        generate_random_message()
        ```
    +    Generates a random message string containing various random values.
    +    Returns:
    +        str: A string in the format "id,idExperiencia,nome,descricao,Tick,ax_raw,ay_raw,az_raw,ax_cook,ay_cook,az_cook,euler_x,euler_y,euler_z,alt_raw,alt_cook,latitude,longitude,drogue,main,state,avg_acc,Delta,idData_id\\\\n"
    Made by: \n
        André Ribeiro <andreribeiro@ua.pt>\n
        Duarte Cruz <?>\n
        \n"""

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
    return f"{id},{idExperiencia},{nome},{descricao},{Tick},{ax_raw},{ay_raw},{az_raw},{ax_cook},{ay_cook},{az_cook},{euler_x},{euler_y},{euler_z},{alt_raw},{alt_cook},{latitude},{longitude},{drogue},{main},{state},{avg_acc},{Delta},{idData_id}\n"
