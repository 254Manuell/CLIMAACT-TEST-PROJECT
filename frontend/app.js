document.getElementById("check").addEventListener("click", () => {
    const city = document.getElementById("city").value;
    if (!city) {
        alert("Please enter a city name!");
        return;
    }

    fetch(`/api/air-quality?city=${city}`)
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById("result");
            if (data.error) {
                resultDiv.textContent = `Error: ${data.error}`;
            } else {
                resultDiv.textContent = `Air Quality Index: ${data.list[0].main.aqi}`;
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
});
