import apache_beam as beam

p1 = beam.Pipeline()

voos = (
    p1
    |'Extrair os dados' >> beam.io.ReadFromText(r'C:\Users\paulo\Desktop\covid_lowercase.txt', skip_header_lines= 1)
    |'Separador' >> beam.Map(lambda record: record.upper())
    #|'Separador' >> beam.FlatMap(lambda record: record.split(' '))
    #|'Contador' >> beam.combiners.Count.Globally() 
    |'Saida de dados' >> beam.Map(print)
    #|'Gravar resultado' >> beam.io.WriteToText('resultado.txt')

)
p1.run()