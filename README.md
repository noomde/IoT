# IoT

1) Project Links



Live Dashboard URL: [Link to deployed frontend, e.g. Vercel/Netlify/Cumulus]

Wokwi Simulation URL: https://wokwi.com/projects/463269245300540417


Backend/Database URL: [Link to deployed backend stack, if applicable]

Repository URL: [Link to your source code]

2) Project Overview

Briefly describe:

What your project does.
Which hardware/sensors you simulated.
What the dashboard allows the user to monitor/control.

3) Architecture and Data Flow

Explain how data moves through your system:

Wokwi device -> MQTT broker -> processing layer/database -> dashboard.
Dashboard -> MQTT command topic -> device action.

Use the placeholder below and replace it with your own architecture screenshot or diagram:

[Insert architecture diagram or screenshot here]


Your diagram must explicitly label the communication protocols used between components (for example MQTT, WebSocket, HTTP/HTTPS).
Example Mermaid diagram (you can copy and adapt):

flowchart TD
  A[Wokwi Device] -->|MQTT publish: sensor data| B[MQTT Broker]
  B -->|sensor data| C[Backend Service]
  C --> D[(Database)]
  C -->|REST API| E[Web Dashboard]
  E <-->|WebSocket, realtid| C
  E -->|send command| C
  C -->|MQTT publish: command| B
  B -->|control message| A


4) Database Strategy

Document:


Database chosen: (for example InfluxDB, MongoDB, TimescaleDB)

Data model: measurement/collection/table structure

Time-series considerations: retention, indexing, query strategy, aggregation, etc.

5) MQTT Topics and Payload Documentation

List all topics used and provide example payloads. This should be precise enough to serve as integration documentation for your device and dashboard communication.
6) Reflection

Answer the following:

Which frontend technologies did you choose, and why?
How does handling real-time MQTT data over WebSockets differ from a standard REST API workflow?
What was the most challenging integration step (hardware, broker, backend, database, frontend), and how did you solve it?
