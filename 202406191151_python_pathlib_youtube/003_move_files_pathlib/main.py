from pathlib import Path

# renomeando arquivo
path = Path(__file__).parent
file = path / 'file_1.txt'

new_file = file.with_suffix('.md')

file.replace(new_file)
print(f'Nome do arquivo {file.name} modificado com sucesso para {new_file.name}')

# copiando arquivo
copy_file = new_file.with_stem('file_2')
copy_file.write_bytes(new_file.read_bytes())
