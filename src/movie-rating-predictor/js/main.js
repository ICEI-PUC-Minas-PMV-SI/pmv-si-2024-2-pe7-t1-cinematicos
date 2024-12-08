document.getElementById("movieForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita o comportamento padrão de envio do formulário

    // Obtém os valores dos gêneros selecionados
    const genresSelect = document.getElementById("genres");
    const selectedGenres = Array.from(genresSelect.selectedOptions).map(option => option.value);

    // Inicializa os gêneros como 0 (todos desmarcados)
    const genres = {
        "Action": 0, "Adventure": 0, "Fantasy": 0, "Science": 0, "Fiction": 0,
        "Crime": 0, "Drama": 0, "Thriller": 0, "Animation": 0, "Family": 0,
        "Western": 0, "Comedy": 0, "Romance": 0, "Horror": 0, "Mystery": 0,
        "History": 0, "War": 0, "Music": 0, "Documentary": 0, "Foreign": 0
    };

    // Atualiza os gêneros selecionados com 1
    selectedGenres.forEach(genre => {
        if (genres.hasOwnProperty(genre)) {
            genres[genre] = 1;
        }
    });

    // Coleta os valores das outras colunas do formulário
    const data = {
        budget: parseFloat(document.getElementById("budget").value), // Obtém o valor do campo 'budget'
        popularity: parseFloat(document.getElementById("popularity").value), // Obtém o valor do campo 'popularity'
        revenue: parseFloat(document.getElementById("revenue").value), // Obtém o valor do campo 'revenue'
        runtime: parseFloat(document.getElementById("runtime").value), // Obtém o valor do campo 'runtime'
        ...genres // Adiciona os gêneros ao objeto final
    };

    console.log(data); // Log para debug, pode ser removido em produção

    // Exibe uma mensagem de carregamento enquanto a API processa
    const resultsDiv = document.getElementById("predictionResults");
    resultsDiv.innerHTML = "<p>Carregando...</p>";

    // Envia os dados para a API via fetch
    fetch("http://40.78.23.140:8000/prever", {
        method: "POST",
        headers: {
            "Content-Type": "application/json" // Define o formato JSON
        },
        body: JSON.stringify(data) // Converte os dados para uma string JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Erro ao processar a solicitação.");
        }
        return response.json();
    })
    .then(data => {
        // Exibe os resultados retornados pela API
        resultsDiv.innerHTML = `
            <h3>Predictions:</h3>
            <p>RNA Prediction: ${data["RNA Prediction"]}</p>
            <p>Linear Regression Prediction: ${data["Linear Regression Prediction"]}</p>
            <p>Final Prediction: ${data["Final Prediction"]}</p>
        `;
    })
    .catch(error => {
        // Exibe uma mensagem de erro caso a chamada falhe
        resultsDiv.innerHTML = "<p>Ocorreu um erro ao tentar obter a previsão. Tente novamente mais tarde.</p>";
        console.error("Erro:", error);
    });
});
