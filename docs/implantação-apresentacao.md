# Implantação da Solução

## API

A solução foi implantada em uma máquina virtual na **Azure**, utilizando o framework Python **FastAPI** para disponibilizar o modelo de aprendizado de máquina baseado em rede neural, desenvolvido com **TensorFlow**. A arquitetura do sistema foi organizada de forma a permitir que a API fosse acessada externamente, executando previsões de acordo com as entradas enviadas pelos usuários.

A máquina virtual foi configurada na plataforma **Azure**, com a instalação do sistema operacional **Ubuntu**. Durante a configuração, foram alocados recursos suficientes para garantir que o sistema pudesse rodar de forma eficiente, incluindo **CPU**, **memória** e **armazenamento** adequados para o tamanho do modelo e do conjunto de dados.

O modelo de rede neural foi treinado previamente e salvo como um arquivo `.keras`. Ele foi carregado utilizando a função `load_model` do **TensorFlow**. Da mesma forma, os objetos de escalamento dos dados (**X_scaler** e **y_scaler**) foram carregados utilizando a biblioteca **Joblib**.

Foi desenvolvido um endpoint **POST** em `/prever` que recebe os dados de entrada, processa os valores utilizando os escaladores e faz a previsão com o modelo carregado. A resposta é enviada de volta para o cliente com o valor da previsão.

A API foi exposta para a internet utilizando a configuração de **Firewall** e **Segurança** da **Azure**, permitindo acesso remoto através de um IP público. A API foi executada utilizando o **Uvicorn**, servidor de aplicação que roda a aplicação FastAPI.

### Testes para Verificar o Funcionamento da Aplicação

Após a implantação, foi realizado um conjunto de testes para garantir que a aplicação estava funcionando conforme esperado.

#### Testes de Resposta da API
Foram enviadas múltiplas requisições via **curl** para verificar a consistência e a velocidade das respostas da API. A resposta para dados de entrada válidos foi gerada dentro de um tempo aceitável, confirmando que a API estava funcionando corretamente.

#### Testes de Carga
Foi realizada uma simulação de carga com a biblioteca Python Locust para verificar o comportamento da API sob alta carga de requisições. O sistema conseguiu lidar com múltiplas requisições simultâneas sem falhas, e o tempo de resposta permaneceu dentro de limites aceitáveis.

#### Testes de Robustez
Também foram realizados testes de robustez para verificar o comportamento do sistema em condições de falha, como dados de entrada inválidos ou problemas de rede. O sistema foi configurado para retornar mensagens de erro apropriadas quando as entradas não estivessem de acordo com o formato esperado.


## Front-End
O front-end foi desenvolvido para criar uma interface simples que permita ao usuário fornecer dados de entrada e visualizar os resultados de previsão fornecidos pela API. A interface foi projetada com HTML, CSS e JavaScript puro, com foco na simplicidade e responsividade.

#### Funcionalidades

* Entrada de Dados: 
Campos para fornecer informações como orçamento, popularidade, receita, número de votos e gêneros de filmes.
Suporte para seleção múltipla no campo de gêneros.

* Integração com a API: O front-end consome a API via requisição HTTP POST. Os dados fornecidos são enviados em formato JSON e o resultado da previsão é exibido na tela.

* Exibição de Resultados: A interface exibe o valor de predição retornado pela API diretamente abaixo do formulário.

#### Estrutura:
* HTML: Define a estrutura da interface.
* CSS: Proporciona um design limpo e responsivo, com cores suaves e layout ajustável.
* JavaScript: Gerencia a lógica da aplicação, como captura de eventos, envio de dados e exibição de resultados.

#### Requisição POST:

URL da API: http://40.78.23.140:8000/prever

O usuário preenche os campos disponíveis no formulário:

* Orçamento: 237000000
* Receita: 9691000000
* Popularidade: 250.082653
* Contagem de Votos: 9466
* Gêneros: Action, Adventure e Comedy.
  
Após clicar em "Gerar Predição", os dados são enviados para a API via POST, exibindo os valores da predição:

Valor da Predição: 7.5

# Apresentação da solução

#### Vídeo da Parte 1 - API Back End
https://github.com/user-attachments/assets/04466283-77de-4b70-b62c-6c45b9a74bd3

#### Vídeo da Parte 2 - Front-end
https://github.com/user-attachments/assets/822437aa-3d0f-47f7-baf8-d6bc135f7bae


