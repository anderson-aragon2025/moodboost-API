# MoodBoost API

Esta es una API creada en Flask que detecta el sentimiento de un texto y devuelve una emoción junto a una frase motivadora. Ideal para ser usada con herramientas como ToolJet o Postman.

## 📦 Características

- Análisis de sentimiento usando TextBlob.
- Clasificación: `muy alegre`, `alegre`, `neutro`, `triste`, `muy triste`.
- Devuelve una frase motivadora basada en el sentimiento detectado.

## 📥 Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta la API:

```bash
python app.py
```

## 🔍 Ejemplo de petición (POST)

**URL del endpoint**: `/analizar`  
**Método**: POST  
**Encabezado**: `Content-Type: application/json`  
**Body (JSON)**:

```json
{
  "texto": "Hoy me siento increíble, todo salió bien."
}
```

**Respuesta**:

```json
{
  "sentimiento": "muy alegre",
  "frase": "¡Sigue brillando! La alegría es contagiosa. ✨"
}
```

## 🧪 Pruebas rápidas

Puedes usar [Postman](https://www.postman.com/) o el panel de ToolJet para probar la API.
Solo asegúrate de enviar correctamente el `path` `/analizar` en tu túnel de Cloudflare.

## 🌐 Hosting con Cloudflare Tunnel

Recuerda que si estás usando Cloudflare Tunnels para exponer tu API, debes incluir **el path `/analizar`** en la URL.

Ejemplo:

```
https://mi-tunel.trycloudflare.com/analizar
```

## ✍ Autores

Desarrollado por Anderson Steven Aragón Cartagena.
Desarrollado por Rocío de los Angeles Henriquez Campos.
