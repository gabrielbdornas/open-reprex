from pathlib import Path

path = Path(__file__).parent
file = path / 'shopping_list.md'

with file.open(mode="r", encoding="utf-8") as md_file:
    content = md_file.read()
    groceries = [line for line in content.splitlines() if line.startswith("*")]
print('Print usando open!')
print("\n".join(groceries))

content = file.read_text(encoding="utf-8")
groceries2 = [line for line in content.splitlines() if line.startswith("*")]

print('Print usando read_text!')
print("\n".join(groceries2))

new_file = path / 'plain_list.md'
new_file.write_text("\n".join(groceries), encoding="utf-8")
