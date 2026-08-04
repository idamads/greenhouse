const temperature = document.getElementById("temperature");
const humidity = document.getElementById("humidity");
const light = document.getElementById("light");
const co2 = document.getElementById("co2");

const signal = document.getElementById("signal");
const connection = document.getElementById("connection");
const alerts = document.getElementById("alerts");
const history = document.getElementById("history");
const clock = document.getElementById("clock");

async function loadClimate() {

    try {

        const response = await fetch("/api/climate");
        const result = await response.json();

        const data = result.data;

        temperature.textContent = data.temperature;
        humidity.textContent = data.humidity;
        light.textContent = data.light;
        co2.textContent = data.co2;

        signal.textContent = data.signal + "%";
        connection.textContent = "Connected";

        renderAlerts(result.alerts);

        loadHistory();

    } catch {

        connection.textContent = "Offline";

    }

}

async function loadHistory() {

    const response = await fetch("/api/history");
    const result = await response.json();

    history.innerHTML = "";

    const records = result.history.slice(-8).reverse();

    records.forEach(item => {

        history.innerHTML += `
        <tr>
            <td>${item.timestamp}</td>
            <td>${item.temperature} °C</td>
            <td>${item.humidity} %</td>
            <td>${item.light} lux</td>
            <td>${item.co2} ppm</td>
        </tr>
        `;

    });

}

function renderAlerts(items){

    if(items.length===0){

        alerts.innerHTML =
        '<p class="empty">No active alerts.</p>';

        return;

    }

    alerts.innerHTML="";

    items.forEach(item=>{

        alerts.innerHTML+=`
        <div class="alert">
            <strong>${item.metric.toUpperCase()}</strong>
            is
            <strong>${item.level}</strong>
            (${item.value})
        </div>
        `;

    });

}

function updateClock(){

    clock.textContent =
        new Date().toLocaleTimeString();

}

loadClimate();
updateClock();

setInterval(loadClimate,5000);
setInterval(updateClock,1000);
