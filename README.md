# Paketboter

Lieferroboter auf Basis von Pi-Top

## Anschlüsse

### Pi-Top

- USB-Stick an einem der USB 3 Ports
- Kamera am USB 2 Port
- Display am Micro-HDMI

### Expansion Plate

- M0: Rechter Motor
- M1: Linker Motor
- S0: Servo-Motor
- D0: "Gewichts-Sensor"-Knopf
- D3: Ultraschall-Distanz-Sensor

## Skripte
- venv.sh: Erstellt ein virtual env mit den Paketen aus requirements.txt
- scripts/install_streamer.sh: Installiert MJPEG-Streamer
- scripts/run_streamer.sh: Startet MJPEG-Streamer als screen
