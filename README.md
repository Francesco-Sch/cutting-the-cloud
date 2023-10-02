# Cutting the Cloud

## Setup

### Virtual Environment

1. Create folder for virtual environment

```bash
python3 -m venv venv
```

2. Activate virtual environment

```bash
source venv/bin/activate
```

3. Deactivate virtual environment

```bash
deactivate
```

### Install packages

1. Install packages

```bash
pip install -r requirements.txt
```

2. Freeze packages list

```bash
pip freeze
```

## Hacking devices

### Scanning for devices

```bash
python3 -m tinytuya scan 9999
```

9999 sets the time for the scan to 9999 seconds. This long scan is needed to actually get the devices.
Make sure the devices werea already connected to the Smart Life app. After that reboot the device while scan is running.

### Add devices to Tuya IoT Development Platform

Development Platform: https://iot.tuya.com/

1. Create Cloud project
