# Proyecto Flask - Nathaly Vizcaíno

Una aplicación web simple desarrollada en Flask con integración completa de Docker, CI/CD y pruebas automatizadas.

## 📋 Descripción

Este proyecto es una aplicación web básica construida con Flask que incluye:
- API REST simple con endpoint de saludo
- Función utilitaria para operaciones matemáticas
- Containerización con Docker
- Pipeline de CI/CD con GitHub Actions
- Pruebas automatizadas con pytest
- Despliegue automatizado con Docker Swarm

## 🚀 Características

- **Framework**: Flask 3.0.0
- **Lenguaje**: Python 3.9
- **Containerización**: Docker
- **Orquestación**: Docker Swarm
- **CI/CD**: GitHub Actions
- **Testing**: pytest 8.1.1
- **Automatización**: Makefile

## 📁 Estructura del Proyecto

```
nathaly.vizcaino/
├── .github/
│   └── workflows/
│       └── ci.yaml          # Pipeline de CI/CD
├── app.py                   # Aplicación principal Flask
├── test_app.py             # Pruebas unitarias
├── requirements.txt        # Dependencias Python
├── Dockerfile             # Configuración Docker
├── makefile              # Comandos automatizados
├── stack.yml            # Configuración Docker Swarm
└── README.md           # Documentación del proyecto
```

## 🛠️ Instalación y Configuración

### Prerrequisitos

- Python 3.9+
- Docker
- Docker Compose (opcional)
- Git

### Instalación Local

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd nathaly.vizcaino
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

La aplicación estará disponible en `http://localhost:5000`

## 🐳 Docker

### Construcción de la imagen

```bash
# Usando Makefile
make build

# O manualmente
docker build -t nathaly:1.0.1 .
```

### Ejecutar contenedor

```bash
docker run -p 5000:5000 nathaly:1.0.1
```

### Despliegue con Docker Swarm

```bash
# Desplegar stack
make deploy

# Remover stack
make rm
```

## 🧪 Pruebas

### Ejecutar pruebas localmente

```bash
pytest
```

### Ejecutar pruebas con cobertura

```bash
pytest --cov=app
```

## 🔄 CI/CD Pipeline

El proyecto incluye un pipeline automatizado de GitHub Actions que se ejecuta en cada push a la rama `vizcaino`:

### Pasos del Pipeline:
1. **Checkout del código**
2. **Configuración de Python 3.9**
3. **Instalación de dependencias**
4. **Ejecución de pruebas con pytest**

### Configuración del Pipeline

El archivo `.github/workflows/ci.yaml` contiene la configuración completa del pipeline.

## 📡 API Endpoints

### GET /
- **Descripción**: Endpoint de saludo
- **Respuesta**: `"Hola, Mundo!"`
- **Código de estado**: `200`

**Ejemplo de uso:**
```bash
curl http://localhost:5000/
```

**Respuesta:**
```
Hola, Mundo!
```

## 🔧 Funciones Utilitarias

### sumar(a, b)
Función que suma dos números.

**Parámetros:**
- `a` (int/float): Primer número
- `b` (int/float): Segundo número

**Retorna:**
- `int/float`: Suma de a + b

## 📝 Comandos Makefile

El proyecto incluye un Makefile con comandos útiles:

```bash
# Construir imagen Docker
make build

# Desplegar aplicación
make deploy

# Remover despliegue
make rm
```

## 🚀 Despliegue

### Desarrollo
```bash
python app.py
```

### Producción con Docker
```bash
make build
make deploy
```

### Variables de Entorno

La aplicación utiliza las siguientes configuraciones:
- **Host**: `0.0.0.0`
- **Puerto**: `5000`

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📋 Roadmap

- [ ] Agregar más endpoints REST
- [ ] Implementar base de datos
- [ ] Agregar autenticación
- [ ] Mejorar cobertura de pruebas
- [ ] Implementar logging
- [ ] Agregar documentación API con Swagger

## 🐛 Solución de Problemas

### Error: Puerto 5000 en uso
```bash
# Encontrar proceso usando el puerto
lsof -i :5000  # En Linux/Mac
netstat -ano | findstr :5000  # En Windows

# Matar el proceso
kill -9 <PID>
```

### Error: Docker no encontrado
Asegúrate de tener Docker instalado y ejecutándose:
```bash
docker --version
docker info
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

**Nathaly Vizcaíno**

## 📞 Soporte

Si tienes alguna pregunta o problema, por favor abre un issue en el repositorio.

---

⭐ ¡No olvides dar una estrella al proyecto si te fue útil!