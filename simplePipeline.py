#GERAR TEMPLATE DE PIPELINE PARA DATAFLOW 
#IMPORTANDO BIBLIOTECAS

import apache_beam as beam
import os
from apache_beam.options.pipeline_options import PipelineOptions

#OPÇÕES DE PIPELINE PARA DATAFLOW DO GOOGLE CLOUD PLATFORM

pipeline_options = {
    'project': 'pipelineprojeto',
    'runner': 'DataflowRunner',
    'region': 'southamerica-east1',
    'staging_location': 'gs://pipeline_batch/temp',
    'temp_location': 'gs://pipeline_batch/temp',
    'template_location': 'gs://pipeline_batch/template/template_arq_batch1' 
}

#CONTA DE SERVIÇO COM CHAVE JSON PARA COMUNICAÇÃO COM GOOGLE CLOUD PLATFORM

serviceAccount = r'C:\Users\paulo\Desktop\vscode\pipelineprojeto-b039b9a8daaf.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = serviceAccount

pipeline_options = PipelineOptions.from_dictionary(pipeline_options)
p = beam.Pipeline(options=pipeline_options)

#OPERAÇÕES DA PIPELINE - ETL

texto = (
    p
    |'Extrair dados' >> beam.io.ReadFromText('gs://pipeline_batch/entrada_dados/big_text.txt')
    |'Caixa alta' >> beam.Map(lambda record: record.upper())
    #|'Saida de dados' >> beam.Map(print)
    |'Gravar dados' >> beam.io.WriteToText('gs://pipeline_batch/saida_dados/big_text_uppercase.txt')
)

p.run()