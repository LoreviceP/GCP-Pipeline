## Modelo Simples de Pipeline para Dataflow com Python e Apache Beam.

</div>
<div style="display: inline_block"><br>
  <img align="center" alt="Pipeline-GCP" height="600" width="800" src="https://github.com/LoreviceP/GCP-Pipeline/blob/13aeae904f59cb98c372781ac34a04ebb5478a7b/Diagrama_Simple_Pipeline.png">
</div>

### Criação de um template de pipeline, dados em Batch, para utilizar no Dataflow.

Este script utiliza o Apache Beam para gerar um arquivo modelo personalizado de pipeline que será utilizado no Dataflow e o salva em uma bucket no Google Storage.
É necessário alterar os caminhos das buckets para funcionar. 

#### Localmente se fez necessário instalar os seguintes pacotes:

- pip install apache-beam[interactive]
- pip install apache-beam[GCP]


#### Descrição da pipeline utilizando Apache Beam:

- Extração de um arquivo de texto (*.txt) de uma bucket no GCP Storage;
- Transformação para caixa alta de todo o conteúdo utilizando uma função anônima;
- Carregamento do arquivo como (*.txt) para outra bucket em GCP Storage.

</div>
<div style="display: inline_block"><br>
  <img align="center" alt="Pipeline-GCP" height="600" width="800" src="https://github.com/LoreviceP/GCP-Pipeline/blob/852bd878cc9de02728c604654b81886eb416d47e/Diagrama_Simple_Pipeline1.PNG">
</div>

#### Fonte do arquivo:

https://www.kaggle.com/bittlingmayer/amazonreviews/version/7?select=train.ft.txt.bz2

#### Chave de liberação para comunicar com GCP

Foi necessário criar uma chave, na conta de serviço, para autorizar o acesso ao GCP. 
