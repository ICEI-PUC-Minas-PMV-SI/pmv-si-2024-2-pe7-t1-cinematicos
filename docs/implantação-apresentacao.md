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

---
Nesta seção, a implantação da solução proposta em nuvem deverá ser realizada e detalhadamente descrita. Além disso, deverá ser descrito também, o planejamento da capacidade operacional através da modelagem matemática e da simulação do sistema computacional.

Após a implantação, realize testes que mostrem o correto funcionamento da aplicação.

# Apresentação da solução

Nesta seção, um vídeo de, no máximo, 5 minutos onde deverá ser descrito o escopo todo do projeto, um resumo do trabalho desenvolvido, incluindo a comprovação de que a implantação foi realizada e, as conclusões alcançadas.

