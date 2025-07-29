# 🧠 MoodBoost API

Una API simple desarrollada en Python y Flask que detecta el sentimiento de un texto (alegre, triste o neutro) y responde con una frase motivadora. Ideal para proyectos con interfaces visuales como ToolJet.

---

## 🚀 Tecnologías utilizadas

- Python 3.10+
- Flask
- TextBlob (para análisis de sentimientos)
- Flask-CORS (para permitir solicitudes desde frontends externos)
- Cloudflare Tunnel (para exponer la API pública sin servidor propio)
- ToolJet (interfaz gráfica de consumo de la API)

---

## 📂 Estructura del proyecto

```
moodboost-api/
├── app.py                # Código principal de la API
├── requirements.txt      # Paquetes necesarios
├── README.md             # Documentación
└── .env (opcional)       # Variables de entorno
```

---

## ⚙️ Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/moodboost-api.git
cd moodboost-api
```

2. Crea un entorno virtual (opcional):
```bash
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta la API localmente:
```bash
python app.py
```

---

## 🌐 Endpoint disponible

### `POST /analizar`

Envía un texto y recibe:

- El **sentimiento** detectado (`alegre`, `triste`, `neutro`, `muy alegre`, `muy triste`)
- Una **frase motivadora** basada en ese sentimiento

#### 🧾 Cuerpo de la solicitud (JSON):
```json
{
  "texto": "Hoy me siento muy feliz y agradecido."
}
```

#### 📥 Respuesta esperada:
```json
{
  "sentimiento": "muy alegre",
  "frase": "¡Tu alegría es contagiosa! "La felicidad no es algo hecho. Proviene de tus propias acciones." - Dalai Lama"
}
```

---

## 🧪 Pruebas rápidas con Postman

Puedes probar fácilmente tu API con [Postman](https://www.postman.com/):

1. Abre Postman y crea una nueva **solicitud POST**
2. URL: `https://TU-SUBDOMINIO.trycloudflare.com/analizar`
3. En la pestaña **Body**, selecciona `raw` y elige `JSON`
4. Envía el siguiente JSON:
```json
{
  "texto": "Estoy cansado y sin motivación."
}
```
5. Haz clic en **Send** y verás el sentimiento y frase motivadora.

---

## 🌐 Importante para uso con Cloudflare Tunnel

Para que Cloudflare Tunnel funcione correctamente con tu API, debes incluir explícitamente el **path `/analizar`** en tus solicitudes desde herramientas como ToolJet o Postman.

- ✅ Correcto: `https://TU-SUBDOMINIO.trycloudflare.com/analizar`
- ❌ Incorrecto: `https://TU-SUBDOMINIO.trycloudflare.com`

Si omites el path, Cloudflare no redirigirá correctamente la solicitud a tu API Flask.

---

## 🧳 Variables de entorno (opcional)

Puedes usar un archivo `.env` si deseas mover tus configuraciones fuera del código.

Ejemplo:

```bash
PORT=5000
DEBUG=True
```

## 👨‍💻 Autores

Anderson Steven Aragón Cartagena – [MoodBoost API]
Rocío de los Angeles Henriquez Campos – [MoodBoost API]
