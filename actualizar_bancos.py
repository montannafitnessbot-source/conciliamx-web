with open("index.html") as f:
    content = f.read()

cambios = 0

old1 = "Envia el estado de cuenta de BBVA, Banorte, Santander, HSBC o Banamex directamente en el chat de Telegram."
new1 = "Envia tu estado de cuenta de BBVA directamente en el chat de Telegram. Mas bancos proximamente."
if old1 in content:
    content = content.replace(old1, new1); cambios += 1

old2 = "BBVA, Banorte, Santander, HSBC y Banamex. Estamos agregando mas bancos constantemente."
new2 = "Actualmente BBVA (unico soportado y probado). Estamos agregando mas bancos constantemente."
if old2 in content:
    content = content.replace(old2, new2); cambios += 1

with open("index.html", "w") as f:
    f.write(content)

print(f"✅ {cambios} textos actualizados en la web")
