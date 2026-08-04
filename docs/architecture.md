# Architecture

Greenhouse Climate Dashboard follows a modular Flask architecture.

```
Browser
     │
     ▼
 Flask Blueprint
     │
     ├── SensorManager
     ├── ClimateSimulator
     ├── AlertManager
     ├── Storage
     └── ClimateStatus
```

## Components

### Dashboard

Provides HTML pages and REST endpoints.

### Sensor Manager

Obtains sensor values from the simulator.

### Climate Simulator

Produces realistic greenhouse measurements.

### Alert Manager

Checks whether readings exceed configured thresholds.

### Storage

Stores the latest measurements in JSON format.

### Climate Status

Converts numeric values into readable health states.

## Data Flow

1. Browser requests `/api/climate`
2. Simulator generates new values
3. Storage saves the reading
4. Alerts are evaluated
5. JSON response is returned
