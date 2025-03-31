from fakepinterest import database, app
from fakepinterest.models import Usuario, Foto


with app.app_context():
    database.create_all()

# gerar chave secreta para colocar no config no arquivo __init__
# import secrets
#
# print(secrets.token_hex(16))