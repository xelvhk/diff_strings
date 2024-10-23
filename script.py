def compare_files(file1, file2, output_file):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output_file, 'w', encoding='utf-8') as out_file:
        # Чтение всех строк из файлов, с удалением лишних пробелов
        lines1 = [line.strip() for line in f1.readlines()]
        lines2 = [line.strip() for line in f2.readlines()]

        total_lines = len(lines1)  # Общее количество строк для вычисления прогресса

        # Пробегаем по строкам первого файла
        for i, line1 in enumerate(lines1):
            # Проверяем, есть ли строка с такими же первыми 10 символами во втором файле
            for line2 in lines2:
                # Если первые 10 символов совпадают
                if line1[:10] == line2[:10]:
                    # Проверяем наличие слова "установлен" в одной строке, но отсутствие в другой
                    if ('установлен' in line1 and 'установлен' not in line2) or ('установлен' not in line1 and 'установлен' in line2):
                        # Записываем строки в выходной файл
                        out_file.write(f'Строка из {file1}: {line1}\n')
                        out_file.write(f'Строка из {file2}: {line2}\n')
                        out_file.write('-' * 40 + '\n')
                    break  # Найдена строка с совпадающими первыми 10 символами, переходим к следующей строке

            # Выводим прогресс выполнения
            progress = (i + 1) / total_lines * 100  # Вычисление процента выполнения
            print(f'Прогресс: {progress:.2f}%')

    print(f"Сравнение завершено, результат записан в {output_file}")

# Использование программы
file1 = 'listA.txt'
file2 = 'listJ.txt'
output_file = 'result.txt'

compare_files(file1, file2, output_file)
