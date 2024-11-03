def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    num_str = 0
    start_byte_str = file.seek(0)
    for i in strings:
        file.write(i + '\n')
        num_str += 1
        key = (num_str,start_byte_str)
        string_positions[key] = i
        start_byte_str = file.tell()
    file.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)