## Modelo Simples de Pipeline para Dataflow

#### Criação de um template de pipeline, dados em Batch, para utilizar no Dataflow.

Este script gera um arquivo template para utilizar no Dataflow e o salva em uma bucket no Google Storage.
É necessário alterar os caminhos das buckets para funcionar. 

##### Localmente se fez necessário instalar os seguintes pacotes:

- pip install apache-beam[interactive]
- pip install apache-beam[GCP]


##### Descrição da pipeline utilizando Apache Beam:

- Extração de um arquivo de texto (*.txt) de uma bucket no GCP Storage;
- Transformação para caixa alta de todo o conteúdo utilizando uma função anônima;
- Carregamento do arquivo como (*.txt) para outra bucket em GCP Storage.

##### Chave de liberação para comunicar com GCP

Foi necessário criar uma chave, na conta de serviço, para autorizar o acesso ao GCP. 