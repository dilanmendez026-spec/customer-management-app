# 📊 Customer Management Application

Una aplicación web moderna para gestionar clientes de la empresa, desarrollada con Flask y SQLAlchemy.

## 🎯 Características

- ✅ Crear nuevos clientes
- ✅ Editar información de clientes existentes
- ✅ Consultar datos de clientes
- ✅ Eliminar clientes
- ✅ Interfaz web responsiva y moderna
- ✅ API REST completa
- ✅ Workflows automatizados en GitHub Actions

## 🛠️ Tecnologías

- **Backend**: Python 3.9+
- **Framework**: Flask 2.3.3
- **ORM**: SQLAlchemy 3.0.5
- **Base de Datos**: SQLite (por defecto)
- **Frontend**: HTML5, CSS3, JavaScript Vanilla

## 📋 Requisitos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Git

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/dilanmendez026-spec/customer-management-app.git
cd customer-management-app
```

### 2. Crear un entorno virtual

```bash
python -m venv venv

# En Windows
venv\\Scripts\\activate

# En macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

El archivo `.env` ya está configurado por defecto:

```env
FLASK_ENV=development
FLASK_APP=app.py
DATABASE_URL=sqlite:///customers.db
```

### 5. Ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 📚 Uso de la API

### Endpoints disponibles

#### 1. Obtener todos los clientes

```bash
GET /api/customers
```

**Respuesta:**
```json
[
  {
    "id": 1,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "phone": "123456789",
    "address": "Calle Principal 123",
    "created_at": "2024-01-01T10:00:00",
    "updated_at": "2024-01-01T10:00:00"
  }
]
```

#### 2. Obtener un cliente específico

```bash
GET /api/customers/<id>
```

#### 3. Crear un nuevo cliente

```bash
POST /api/customers
Content-Type: application/json

{
  "name": "María García",
  "email": "maria@example.com",
  "phone": "987654321",
  "address": "Avenida Secundaria 456"
}
```

#### 4. Actualizar un cliente

```bash
PUT /api/customers/<id>
Content-Type: application/json

{
  "name": "María García Updated",
  "email": "maria.updated@example.com",
  "phone": "987654321",
  "address": "Avenida Nueva 789"
}
```

#### 5. Eliminar un cliente

```bash
DELETE /api/customers/<id>
```

#### 6. Verificar estado de la aplicación

```bash
GET /health
```

## 🔄 Workflows de GitHub Actions

La aplicación incluye los siguientes workflows automatizados:

### 1. Crear Nuevo Cliente
Disparado cuando se abre un issue con la etiqueta `crear-cliente`

### 2. Modificar Cliente Existente
Disparado cuando se abre un issue con la etiqueta `modificar-cliente`

### 3. Consultar Cliente
Disparado cuando se abre un issue con la etiqueta `consultar-cliente`

### 4. Solicitud de Nueva Función
Disparado cuando se abre un issue con la etiqueta `solicitud-funcion`

### 5. Solicitud de Mejora
Disparado cuando se abre un issue con la etiqueta `mejora`

### 6. Cambio de Código
Disparado cuando se abre o actualiza un Pull Request

## 👥 Roles y Permisos (DevOps Methodology)

### Administrador del Sistema
- Control total sobre el repositorio
- Gestión de permisos
- Despliegue a producción

### Desarrollador Senior
- Revisión de código
- Aprobación de pull requests
- Gestión de releases

### Desarrollador
- Crear branches y commits
- Abrir pull requests
- Resolver issues

### QA/Tester
- Crear issues de bugs
- Revisar funcionalidad
- Generar reportes

### DevOps
- Gestión de infraestructura
- Despliegue automatizado
- Monitoreo

## 📂 Estructura del Proyecto

```
customer-management-app/
├── app.py                 # Aplicación principal
├── requirements.txt       # Dependencias
├── .env                   # Variables de entorno
├── .gitignore            # Archivos a ignorar
├── templates/
│   └── index.html        # Interfaz web
├── .github/
│   └── workflows/        # Workflows de GitHub Actions
│       ├── create-customer.yml
│       ├── modify-customer.yml
│       ├── query-customer.yml
│       ├── feature-request.yml
│       ├── improvement-request.yml
│       └── code-change.yml
└── README.md             # Este archivo
```

## 🧪 Testing

Para ejecutar los tests:

```bash
pytest tests/ -v
```

## 🐛 Solución de Problemas

### El puerto 5000 ya está en uso

```bash
# Cambiar el puerto en app.py o usar:
python app.py --port 8000
```

### Error de conexión a base de datos

Asegúrate de que el archivo `customers.db` tenga permisos de escritura.

## 📝 Versionado

Para mantener un historial limpio de versiones:

```bash
# Ver historial
git log --oneline

# Crear tag para versión estable
git tag -a v1.0.0 -m "Versión 1.0.0 - Estable"

# Ver todas las versiones
git tag
```

## 🚨 Recuperación de Fallos

Si necesitas volver a una versión anterior:

```bash
# Ver commit específico
git log --oneline

# Volver a un commit anterior
git checkout <commit-hash>

# O crear una rama desde un commit anterior
git checkout -b restore-branch <commit-hash>
```

## 📞 Soporte

Para reportar bugs o solicitar funciones, abre un issue en el repositorio.

## 📄 Licencia

Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para más detalles.

## 👨‍💻 Autor

Desarrollado por el equipo de desarrollo.

---

**Última actualización**: 2024-01-01
