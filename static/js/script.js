document.addEventListener('DOMContentLoaded', function() {
    // Only run this script if we are on the analysis page (where charts exist)
    if(document.getElementById('pmChart')) {
        fetchDataAndRenderCharts();
    }
});

async function fetchDataAndRenderCharts() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();

        if (data.error) {
            console.error("Error fetching data:", data.error);
            return;
        }

        // Generate an array of labels (Sample 1, Sample 2, etc.)
        const labels = Array.from({length: data.pm25.length}, (_, i) => `Sample ${i + 1}`);

        // Chart 1: PM2.5 vs PM10
        const ctxPm = document.getElementById('pmChart').getContext('2d');
        new Chart(ctxPm, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'PM2.5',
                        data: data.pm25,
                        borderColor: '#2563eb', // Primary color
                        backgroundColor: 'rgba(37, 99, 235, 0.1)',
                        borderWidth: 2,
                        fill: true,
                        tension: 0.4
                    },
                    {
                        label: 'PM10',
                        data: data.pm10,
                        borderColor: '#10b981', // Secondary color
                        backgroundColor: 'rgba(16, 185, 129, 0.1)',
                        borderWidth: 2,
                        fill: true,
                        tension: 0.4
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' }
                }
            }
        });

        // Chart 2: AQI Trend
        const ctxAqi = document.getElementById('aqiChart').getContext('2d');
        new Chart(ctxAqi, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'AQI Level',
                    data: data.aqi,
                    backgroundColor: data.aqi.map(value => {
                        if (value <= 50) return '#10b981'; // Good
                        if (value <= 100) return '#f59e0b'; // Moderate
                        if (value <= 200) return '#f97316'; // Poor
                        return '#ef4444'; // Very Poor
                    }),
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                }
            }
        });

        // Chart 3: Other Pollutants
        const ctxPollutants = document.getElementById('pollutantsChart').getContext('2d');
        new Chart(ctxPollutants, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'NO2',
                        data: data.no2,
                        borderColor: '#8b5cf6', // Purple
                        tension: 0.4
                    },
                    {
                        label: 'CO',
                        data: data.co,
                        borderColor: '#f59e0b', // Yellow/Orange
                        tension: 0.4
                    },
                    {
                        label: 'SO2',
                        data: data.so2,
                        borderColor: '#ef4444', // Red
                        tension: 0.4
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' }
                }
            }
        });

    } catch (error) {
        console.error("Failed to fetch or render charts:", error);
    }
}
