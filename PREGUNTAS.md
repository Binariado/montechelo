# Microservicios y Django: Conceptos y Respuestas

## Microservicios

### ¿Qué es la arquitectura de microservicios y cuáles son sus ventajas sobre una arquitectura monolítica?
La arquitectura de microservicios es un enfoque donde la aplicación se divide en servicios pequeños e independientes. Cada servicio está diseñado para cumplir una función específica y puede desarrollarse, desplegarse y escalarse de manera independiente. Estos servicios se comunican entre sí a través de APIs o mensajes.

**Ventajas sobre una arquitectura monolítica:**
1. Cada servicio puede escalarse según sus propias necesidades, sin afectar al resto del sistema.
2. Puedes usar diferentes tecnologías en cada microservicio dependiendo de lo que mejor se adapte a sus necesidades.
3. Si un servicio falla, no afecta directamente a los demás, lo que mejora la estabilidad del sistema.
4. Los cambios en un microservicio no requieren desplegar toda la aplicación, lo que facilita la iteración y la entrega continua.

---

### ¿Cómo gestionas la comunicación y la consistencia de datos entre microservicios?
- **Comunicación:** 
  - Para interacciones síncronas, usaría **APIs REST** o **gRPC**.
  - Para interacciones asíncronas o eventos, prefiero usar colas de mensajes como **RabbitMQ** o **Apache Kafka**.
  
- **Consistencia de datos:**
  - Uso **consistencia eventual** para mantener flexibilidad, aplicando patrones como **Saga** para coordinar transacciones distribuidas.
  - Si es necesaria la consistencia fuerte, podría usar bases de datos distribuidas con soporte transaccional o diseñar APIs que ofrezcan confirmación explícita de operaciones.

---

## Django

### ¿Cómo funciona el sistema de enrutamiento (URLs) en Django?
El sistema de enrutamiento de Django se basa en el archivo `urls.py`. Este archivo actúa como un mapa que asocia URLs con vistas específicas. Básicamente, defines rutas utilizando expresiones regulares o patrones de URL modernos, y las enlazas con vistas que procesan las solicitudes.

Un ejemplo básico:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.inicio, name='todo-list-create'),
    path('todos/<int:id>/', views.detalle, name='todo-detail'),
]
