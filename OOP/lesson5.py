import re

my_text = 'Vasya 1964 vasya@gmail.com' \
          'Adilet 1997 adilet@gmail.com' \
          'Radomir 1997 radomir@gmail.com' \
          'Maksim 1997 maks@gmail.com' \
          'Bekzat 1988 bek@gmail.com'

file_path = 'class_mock_data.txt'
result_file_patch = 'results.txt'
file_read = open(file_path, mode='r', encoding='Latin')
final_result = open(result_file_patch, mode='w')
class_text = file_read.read()
# seacher = r'@\w+.\w+.[a-z]'
seacher = r'\w+\s+\d+'
result_all = re.findall(seacher,class_text)

for item in result_all:
    print(item)
    final_result.write(item+'\n')

print(f'Total res:{str(len(result_all))}')