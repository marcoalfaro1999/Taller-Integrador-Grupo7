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

# Que es LoRa?
LoRa, abreviatura de Long Range, es una tecnología de comunicación inalámbrica que permite la transmisión de datos a largas distancias con un consumo energético mínimo. Su funcionamiento se basa en una técnica de modulación llamada chirp spread spectrum, donde las señales varían de frecuencia durante el envío, lo que proporciona una gran inmunidad al ruido y permite mantener la estabilidad de la señal incluso en entornos con muchas interferencias.

Esta tecnología se ha convertido en una de las favoritas para sistemas que requieren comunicaciones eficientes, económicas y de largo alcance, sin necesidad de recurrir a redes celulares. LoRa es especialmente útil en aplicaciones que no demandan altas tasas de transferencia de datos, sino más bien confiabilidad y alcance, como sucede con sensores remotos o dispositivos distribuidos en zonas rurales o urbanas de difícil acceso.

Entre los casos de uso más destacados se encuentran los sistemas de monitoreo agrícola, donde sensores distribuidos por campos o invernaderos pueden reportar información sobre humedad, temperatura o estado del cultivo. También es clave en infraestructura de ciudades inteligentes, donde se requiere recolectar datos sobre niveles de contaminación, estado del tráfico, consumo de energía, o incluso la ubicación de contenedores de basura inteligentes.

A diferencia de tecnologías como WiFi o Bluetooth, LoRa puede alcanzar distancias de varios kilómetros sin perder estabilidad en la comunicación, lo que la hace perfecta para redes IoT de bajo consumo. Además, opera en bandas de frecuencia no licenciadas, lo cual facilita su implementación sin grandes costos regulatorios. En América Latina, por ejemplo, suele utilizarse la banda ISM de 900 MHz, específicamente el rango de 902 a 928 MHz en países como Costa Rica.

En cuanto al desarrollo de proyectos con esta tecnología, existen múltiples plataformas que permiten su integración. Una de las más utilizadas es el microcontrolador ESP32, compatible con módulos LoRa como el SX1276 o SX1278. El ESP32 no solo facilita la conexión inalámbrica mediante LoRa, sino que también incluye conectividad WiFi y Bluetooth, y puede configurarse para operar con diferentes velocidades de reloj, lo que le otorga una gran flexibilidad en aplicaciones tanto comerciales como experimentales.

Gracias a su bajo consumo energético, robustez y simplicidad de implementación, LoRa continúa posicionándose como una solución clave en redes distribuidas de sensores, automatización remota y otras aplicaciones de monitoreo que requieren confiabilidad y bajo mantenimiento.

# Procedimiento

Una vez descargado el firmware correspondiente al LoRa APRS Tracker, el siguiente paso es la configuración del entorno de desarrollo. Para ello, se utiliza PlatformIO, una extensión del editor Visual Studio Code, diseñada para facilitar el desarrollo de software embebido.

El proceso comienza iniciando un nuevo proyecto dentro de PlatformIO. En lugar de crear uno desde cero, se opta por la opción "Import Project", que permite cargar un proyecto ya existente. Durante este paso, es necesario seleccionar la placa de desarrollo específica por ejemplo ESP32 o STM32 en función de la placa a utilizar, así como la ruta del directorio donde se encuentra el firmware descargado.

Una vez importado el proyecto, PlatformIO configura automáticamente el entorno, incluyendo la plataforma objetivo, los entornos de compilación y las bibliotecas necesarias. Esto permite compilar y cargar el firmware directamente en la placa desde la misma interfaz, facilitando el flujo de trabajo para desarrolladores de sistemas embebidos.

Este procedimiento se ilustra en las siguientes imágenes, donde se detallan cada uno de los pasos mencionados, desde la importación hasta la selección del hardware y ubicación del proyecto.

## Entorno de desarroollo
Dentro del entorno de desarrollo del LoRa APRS Tracker, existen varios bloques de configuración clave que permiten personalizar el comportamiento del dispositivo según los requisitos del usuario y el entorno donde será desplegado. A continuación, se describen las secciones más relevantes del archivo de configuración:

-Bacon
Esta sección está dedicada a la identificación del dispositivo y al control de la transmisión de datos APRS.

Callsign: Define el nombre de identificación del nodo en la red APRS. Se compone de dos partes:

Prefijo: Generalmente, los primeros caracteres corresponden al indicativo nacional del país. En el caso de Costa Rica, se utiliza el prefijo "TI", seguido de letras o números que identifican el sistema o la zona donde opera el equipo. Por ejemplo, un "TI3" puede indicar que el dispositivo opera en la provincia de Cartago.

SSID: El sufijo numérico indica la función del dispositivo dentro de la red. Por ejemplo, un SSID de 0 usualmente representa un IGate o estación base, mientras que un 7 se asocia con trackers móviles o nodos transmisores.

Symbol: Corresponde al ícono visual que será mostrado en los mapas APRS para representar la posición del dispositivo. La elección del símbolo depende del tipo de estación (vehículo, base fija, persona, etc.).

Comment: Es un mensaje adicional que se envía junto con cada paquete de datos, útil para proporcionar información sobre el propósito del dispositivo, su ubicación o estado operativo.

SmartBeacon: Parámetros que controlan la lógica de transmisión adaptativa. Esta función ajusta automáticamente el intervalo de envío de paquetes dependiendo de la velocidad y dirección del dispositivo, optimizando el uso del canal de radio y reduciendo el tráfico innecesario.

-Display
showSymbol: Habilita la visualización del símbolo asociado al dispositivo en una pantalla local, si está disponible. Esta opción es útil para verificar en tiempo real el estado del nodo o para fines demostrativos.

-Notificación
ledTx: Activa un indicador luminoso (LED) que se enciende cada vez que se realiza una transmisión APRS. Esta función es útil para diagnóstico visual, indicando que el equipo está transmitiendo correctamente.

-LoRa
frequency: Define la frecuencia de operación del módulo LoRa. En cumplimiento con la normativa nacional de telecomunicaciones, este valor se ajusta comúnmente a 433.775 MHz en Costa Rica, dentro del rango permitido para aplicaciones de baja potencia.

power: Establece el nivel de potencia de salida en la transmisión LoRa. Ajustar este parámetro permite balancear el alcance de la señal y el consumo energético del dispositivo, algo esencial en implementaciones autónomas con alimentación limitada.

## Conexión

1-Abrir el archivo de configuración
Con el entorno ya preparado, accede al archivo principal de configuración del transmisor, el cual usualmente se encuentra dentro del directorio src o config. Este archivo contiene los parámetros clave para el funcionamiento del dispositivo.

2-Personalizar parámetros del dispositivo
Ajusta los valores de configuración de acuerdo con tus necesidades. Entre ellos, el callsign es uno de los más relevantes. En el ejemplo de referencia, se incluyen tres posibles identificadores para ilustrar diferentes formas de identificación dentro de la red APRS. Es importante que este parámetro sea único por dispositivo para evitar conflictos de red.

3-Seleccionar la placa de desarrollo adecuada
Asegúrate de que el tipo de hardware seleccionado sea compatible con tu dispositivo. En este caso, se debe elegir la opción "ttgo-t-beam-v1_2" en la configuración del entorno, ya que corresponde al modelo exacto de la placa utilizada. Esta configuración define aspectos como pines, controladores y librerías necesarias.

4-Ejecutar la verificación del código (Compilación)
Utiliza la opción de Build en PlatformIO para compilar el código. Esta acción revisa la sintaxis, enlaza las bibliotecas y genera los binarios necesarios. Si existen errores en la configuración o el código fuente, se mostrarán en la consola para su corrección.

5-Construir el proyecto
Una vez compilado correctamente, se procede a construir el proyecto. Este paso prepara el firmware final que será cargado en el microcontrolador. Si se encuentra conectado el dispositivo, también puede iniciarse el proceso de carga automática desde la misma interfaz.


6-Acceder al menú de PlatformIO
Una vez completada la compilación del proyecto, dirígete al menú lateral de PlatformIO dentro de Visual Studio Code. Este menú contiene todas las herramientas necesarias para gestionar, cargar y monitorear el dispositivo.

7-Cargar el sistema de archivos al dispositivo
En la sección correspondiente al entorno de la placa configurada, localiza la opción "Upload Filesystem Image". Esta función permite cargar al dispositivo todos los archivos necesarios que no forman parte del firmware directamente, como configuraciones adicionales, imágenes, registros o recursos estáticos. Esta operación es esencial para garantizar que el dispositivo tenga acceso a todos los elementos requeridos para su funcionamiento en campo.

Si el proceso fue exitoso el dispositivo procede a reiniciarse, posterormente inicia el trackeo y en su pantalla se logra observar el identificador además de otros datos reelevantes como la bateía restante.
![photo_5167904899558649634_y](https://github.com/user-attachments/assets/3d632971-ddec-40f9-8b66-885ba5e39170)

Finalmente se realiza la busqueda del modulo en la página web aprs.fi , de forma que se observa en dispositvo en el mapa, además de el trazo del recorrido realizado, en funcion del tiempo sellecionado en la página web.
![photo_5167904899558649633_y (1)](https://github.com/user-attachments/assets/ceba1da4-c4d5-4f52-b4ca-1d35ec8fd62d)
