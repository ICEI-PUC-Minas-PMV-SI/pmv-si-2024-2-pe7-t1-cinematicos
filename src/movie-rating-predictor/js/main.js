document.getElementById("movieForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const data = {
        budget: document.getElementById("budget").value,
        popularity: document.getElementById("popularity").value,
        revenue: document.getElementById("revenue").value,
        runtime: document.getElementById("runtime").value,
        genres: document.getElementById("genres").value.split(",").map(str => str.trim())
    };

    // Substituir pela chamada à API quando o back-end estiver implementado
    console.log(data);

    // Limpeza da área de resultados
    const resultsDiv = document.getElementById("predictionResults");
    resultsDiv.innerHTML = "<p>Carregando...</p>";

    // Enviar os dados para a API através de uma requisição POST (substituir o URL quando o back-end estiver pronto)
    fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Exibir os resultados da previsão
        resultsDiv.innerHTML = `
            <h3>Predictions:</h3>
            <p>RNA Prediction: ${data["RNA Prediction"]}</p>
            <p>Linear Regression Prediction: ${data["Linear Regression Prediction"]}</p>
            <p>Final Prediction: ${data["Final Prediction"]}</p>
        `;
    })
    .catch(error => {
        resultsDiv.innerHTML = "<p>Ocorreu um erro ao tentar obter a previsão. Tente novamente mais tarde.</p>";
        console.error("Erro:", error);
    });
});
