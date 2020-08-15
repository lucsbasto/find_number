from datetime import datetime
def find_number(numbers, output):
    start_time = datetime.now().microsecond
    number = numbers.pop(0)
    size = numbers.pop(0)
    if number not in numbers:
        output.write('False\n')
        output.write("%s\n" % -1)
        output.write("%s" % (datetime.now().microsecond - start_time))
    else:
        output.write('True\n')
        output.write("%s\n" % numbers.index(number))
        output.write("%s\n" % (datetime.now().microsecond - start_time))
for i in ['a', 'b', 'c']:
    input_name = 'dataset-1-{i}.csv'.format(i=i)
    output_name = 'resposta-dataset-1-{i}.txt'.format(i=i)
    input = open(input_name, 'r')
    output = open(output_name, 'w+');
    lines = input.read();
    numbers = lines.split("\n")
    find_number(numbers, output)
