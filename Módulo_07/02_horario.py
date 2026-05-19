from datetime import datetime

agora = datetime.now()

print("Data de hoje:", agora.strftime("%d/%m/%Y"))
print("Horário:", agora.strftime("%H:%M"))