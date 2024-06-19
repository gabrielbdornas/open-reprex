from pathlib import Path

current_folder = Path(__file__).parent
# import ipdb; ipdb.set_trace(context=10)
new_folder = current_folder / 'archive'
Path.mkdir(new_folder)

for file_path in current_folder.glob('*.txt'):
    new_path = new_folder / file_path.name
    file_path.replace(new_path)
