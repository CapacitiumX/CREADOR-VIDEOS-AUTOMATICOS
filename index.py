<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CAPACITIUMX V329 - WEB ÉLITE</title>
    
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css">
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>

    <style>
        body { background-color: #050505; color: #00ff00; font-family: 'Arial', sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: auto; text-align: center; }
        .header { border-bottom: 2px solid #111; padding-bottom: 20px; margin-bottom: 20px; }
        input, button { padding: 10px; font-size: 16px; border-radius: 5px; border: none; }
        input { width: 300px; }
        button { background-color: #7c3aed; color: white; cursor: pointer; font-weight: bold; }
        button:hover { background-color: #6d28d9; }
        #gallery { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; margin-top: 30px; }
        .card { background: #111; padding: 10px; border: 1px solid #333; border-radius: 8px; }
        img { width: 100%; border-radius: 5px; height: 150px; object-fit: cover; }
        .status { color: #d97706; margin: 10px; font-weight: bold; }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>🚀 CAPACITIUMX V329 - WEB INTERFACE</h1>
        <p>Buscador de recursos para automatización de YouTube</p>
        <input type="text" id="tema" placeholder="Introduce el tema (ej: Monterrey)...">
        <button id="search-btn" py-click="buscar_fotos">TRAER FOTOS ✨</button>
    </div>

    <div id="status-label" class="status">Listo para buscar...</div>
    <div id="gallery"></div>
</div>

<py-script>
import js
from pyodide.http import pyfetch
import asyncio
import re

async def buscar_fotos(event):
    status = js.document.getElementById("status-label")
    gallery = js.document.getElementById("gallery")
    tema = js.document.getElementById("tema").value
    
    if not tema:
        js.alert("¡Escribe un tema primero!")
        return

    status.innerHTML = f"⌛ Buscando 30 fotos de: {tema}..."
    gallery.innerHTML = "" # Limpiar galería

    # Simulamos el motor de búsqueda de Bing que tenías en Python
    # Nota: En Web, las peticiones directas a Bing pueden dar error de CORS,
    # por lo que PyScript usa el fetch del navegador.
    search_url = f"https://www.bing.com/images/search?q={tema.replace(' ', '+')}"
    
    try:
        response = await pyfetch(url=search_url, method="GET")
        if response.status == 200:
            html = await response.string()
            # Expresión regular para extraer links de imágenes del HTML de Bing
            links = re.findall(r'murl&quot;:&quot;(.*?)&quot;', html)
            
            exitos = 0
            for link in links[:30]:
                # Crear el elemento en el DOM (la tarjeta de la foto)
                card = js.document.createElement("div")
                card.className = "card"
                
                img = js.document.createElement("img")
                img.src = link
                
                card.appendChild(img)
                gallery.appendChild(card)
                exitos += 1
            
            status.innerHTML = f"✅ ¡Éxito! Se cargaron {exitos} imágenes."
        else:
            status.innerHTML = "❌ Error al conectar con el buscador."
    except Exception as e:
        status.innerHTML = f"❌ Error de red o CORS: {str(e)}"
        print(f"Error: {e}")

</py-script>

</body>
</html>
