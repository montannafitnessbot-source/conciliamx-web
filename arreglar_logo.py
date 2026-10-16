with open("index.html", "r") as f:
    content = f.read()

# Reemplazar el div vacío del logo con la imagen
old = '<div class="logo-icon"></div>'
new = '<img src="logo.png" alt="ConciliaMx" style="width: 45px; height: 45px; border-radius: 50%; object-fit: cover;">'

if old in content:
    content = content.replace(old, new)
    print("✅ Logo reemplazado correctamente")
else:
    print("⚠️ No se encontró el div del logo, buscando alternativas...")
    # Buscar cualquier versión del logo-icon
    import re
    content = re.sub(r'<div class="logo-icon"[^>]*>.*?</div>', new, content, flags=re.DOTALL)
    print("✅ Logo reemplazado con regex")

with open("index.html", "w") as f:
    f.write(content)
