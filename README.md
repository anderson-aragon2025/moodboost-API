# MoodBoost API

MoodBoost API es una API desarrollada en **Flask** que analiza el sentimiento de un texto y devuelve una emoción junto con una **frase motivadora**. Ideal para integraciones con **ToolJet**, **Postman** o cualquier aplicación que consuma APIs REST.

## 📦 Características
- 🔹 Análisis de sentimiento usando **TextBlob**.
- 🔹 Clasificación en 3 estados: `alegre`, `neutro`, `triste`.
- 🔹 Devuelve una frase motivadora personalizada según la emoción.
- 🔹 Compatible con **Cloudflare Tunnel** para exponer tu API a internet de forma segura.

## 🛠️ Herramientas necesarias

| Herramienta             | Uso principal |
|-------------------------|---------------|
| **Python 3.9+**         | Ejecutar la API Flask |
| **Pip**                 | Instalar dependencias del proyecto |
| **Flask y Flask-CORS**  | Framework para la API y soporte CORS |
| **TextBlob**            | Análisis de sentimientos |
| **Postman**             | Probar la API con solicitudes HTTP |
| **ToolJet**             | Integración visual para mostrar los resultados |
| **Cloudflare Tunnel (cloudflared)** | Exponer la API local a internet de forma segura |

## 📥 Instalación

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias:

```cmd
pip install -r requirements.txt
```

3. Ejecuta la API:

```
python app.py
```

Por defecto, la API se ejecutará en:
```
http://127.0.0.1:5000
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
  "sentimiento": "alegre",
  "frase": "¡Sigue brillando! La alegría es contagiosa. ✨"
}
```

## 🧪 Pruebas con Postman

1. Abre Postman y crea una nueva solicitud POST.
   
2. URL de ejemplo en local:
   http://127.0.0.1:5000/analizar
   
3. En la pestaña Body, selecciona raw → JSON e ingresa:
   {
     "texto": "Hoy me siento feliz"
   }

4. Haz clic en Send y verás la emoción detectada y la frase motivadora.

## 🌐 Subir la API a la nube con Cloudflare Tunnel

1. Instala cloudflared desde:
https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation

2. Ejecuta un túnel hacia tu API local:
   cloudflared tunnel --url http://127.0.0.1:5000

3. Obtendrás una URL pública como:
   https://mi-tunel.trycloudflare.com
   
4. Tu endpoint ahora será accesible desde cualquier lugar:
   https://mi-tunel.trycloudflare.com/analizar

## 🖥️ Pruebas con ToolJet

1. Crea una nueva aplicación en ToolJet.

2. Agrega un REST API Query con la siguiente configuración:

   -URL: https://mi-tunel.trycloudflare.com/analizar (proporcionada por cloudflare)

   -Método: POST

  - Encabezado o header: Content-Type: application/json

  - Body (Click en raw para evitar errores):

    {
      "texto": "{{ textInput1.value }}" (Variable que toma el valor colocado en un textInput)
    }

3. Vincula la respuesta a un Text Widget para mostrar {{ query1.data.sentimiento }} y {{ query1.data.frase_motivadora }}.

## ✍ Autores

Desarrollado por Anderson Steven Aragón Cartagena.
y Rocío de los Angeles Henriquez Campos.
