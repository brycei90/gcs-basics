import { useState, useEffect } from 'react';

function TelemetryPanel() {
  const [telemetry, setTelemetry] = useState({});

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8000/ws/telemetry');
    ws.onmessage = e => {
      const data = JSON.parse(e.data);
      setTelemetry(data);
    };
    ws.onerror = console.error;
    return () => ws.close();
  }, []);

  return (
    <div>
      <h3>Live Telemetry</h3>
      <p>Altitude: {telemetry.altitude} m</p>
      <p>Speed: {telemetry.speed} m/s</p>
      <p>Battery: {telemetry.battery}%</p>
    </div>
  );
}

export default TelemetryPanel;