# LoRa_APRS_Tracker
## Grupo 7
Integrantes

- Ricardo Sanchez Calderón
- Marco Umaña Vallejos
- Marco Alfaro Bolaños



## Descripción
Este repositorio contiene el firmware para un rastreador y estación APRS utilizando placas basadas en ESP32 con módulos LoRa y GPS. Basado en el proyecto original de [Richonguzman / CA2RXU LoRa APRS Tracker/Station.
](https://github.com/richonguzman/LoRa_APRS_Tracker)

# Que es APRS?
El Sistema Automático de Reporte de Paquetes, conocido como APRS (Automatic Packet Reporting System), es una tecnología de comunicación digital en tiempo real, ampliamente utilizada por radioaficionados para compartir información útil como coordenadas GPS, datos meteorológicos, mensajes breves y señales de telemetría. Fue desarrollado en los años 80 por Bob Bruninga (WB4APR) y opera principalmente sobre redes de radio VHF y UHF, aunque también puede integrarse a través de Internet mediante servidores conocidos como APRS-IS.

Este sistema permite una comunicación bidireccional entre múltiples usuarios conectados a una misma red, facilitando el envío y la recepción continua de información considerada de interés para una comunidad local o una red más amplia. Cualquier dato relevante en el entorno, como la posición de un vehículo, condiciones del clima o parámetros de sensores, puede ser detectado por un dispositivo APRS y transmitido automáticamente.

Las transmisiones suelen realizarse en frecuencias compartidas, y la información se repite mediante estaciones de retransmisión para ampliar su cobertura. Además, los datos pueden ser introducidos en la red global mediante estaciones pasarela (IGate), que los suben a la infraestructura de APRS en Internet, haciéndolos accesibles a otros usuarios desde cualquier parte del mundo.

En cuanto a los protocolos utilizados, el más común es el AX.25, una versión adaptada del protocolo X.25 especialmente diseñado para la comunidad de radioaficionados. No obstante, dependiendo del propósito o aplicación específica, se pueden emplear otros protocolos de comunicación compatibles con APRS.

## Caracteristicas de APRS
- Transmisión de Datos en Tiempo Real: Permite enviar y recibir información sin necesidad de una conexión a Internet, usando radios y repetidores.

- Geolocalización: Puede transmitir la ubicación GPS de estaciones móviles o fijas.

- Mensajería Digital: Facilita la comunicación entre estaciones sin necesidad de una infraestructura celular o de Internet.

- Telemetría y Sensores: Se usa para monitorear variables ambientales como temperatura, humedad, presión y más.

- Infraestructura Mixta: Funciona tanto en radiofrecuencia (RF) como en Internet, con servidores que retransmiten los datos.

## Principales usos de APRS
Rastreo de vehículos y expediciones.

Monitoreo de estaciones meteorológicas.

Comunicación en emergencias y eventos.

Telemetría de sensores remotos.

## Funcionalidades Principales de la Placa LILYGO LoRa32

### Mensajería y Reportes Meteorológicos:
- Envío y recepción de mensajes mediante teclado I2C o teléfono..
- Solicitud de reportes meteorológicos y detección de rastreadores cercanos.
### Gestión de Energía y Pantalla:
- Ajuste de la frecuencia del procesador (240MHz a 80MHz) para reducir el consumo en un 20%.
- Pantalla OLED con datos de altitud, velocidad, rumbo y mensajes.
- Modos de ahorro de energía y ajuste de brillo.
### Conectividad y Notificaciones:
- Indicadores LED y notificaciones sonoras con zumbador YL44.
- Compatible con APRSDroid (Android) y APRS.fi (iPhone) para funciones TNC.
### Telemetría y Frecuencias:
- Transmisión de datos meteorológicos con sensor BME280
- Cambio entre tres frecuencias LoRa APRS globales.
- Compatible con hardware ESP32 y LoRa, incluyendo Heltec V3 y Lilygo TTGO T-Deck.
### Modos Adicionales:
- Función DigiRepeater para emergencias
- Detección automática de sensores meteorológicos.
- Apagado rápido en modelos T-Beams con triple pulsación.

### Modos y Funcionalidades Adicionales:
- Función DigiRepeater para asistencia en emergencias.
- Detección automática de sensores BME y BMP (BME280/BMP280/BME680).
- Posibilidad de apagar el rastreador con tres pulsaciones del botón central en modelos T-Beams.
