with open('input.txt', 'r') as input_file:
    content = input_file.read().replace('\n', '')

with open('output.txt', 'w') as output:
    output.write(content)

# (((b|eps)(b|eps)*(a)|(a))((b)(b|eps)*(a)|(eps))*((b)(b|eps)*({})|(a))|((b|eps)(b|eps)*({})|({})))(((b)(b|eps)*(a)|({}))((b)(b|eps)*(a)|(eps))*((b)(b|eps)*({})|(a))|((b)(b|eps)*({})|(a|eps)))*(((b)(b|eps)*(a)|({}))((b)(b|eps)*(a)|(eps))*((b)(b|eps)*(b|eps)|(b))|((b)(b|eps)*(b|eps)|(b)))|(((b|eps)(b|eps)*(a)|(a))((b)(b|eps)*(a)|(eps))*((b)(b|eps)*(b|eps)|(b))|((b|eps)(b|eps)*(b|eps)|(b|eps)))|(((b|eps)(b|eps)*(a)|(a))((b)(b|eps)*(a)|(eps))*((b)(b|eps)*({})|(a))|((b|eps)(b|eps)*({})|({})))(((b)(b|eps)*(a)|({}))((b)(b|eps)*(a)|(eps))*((b)(b|eps)*({})|(a))|((b)(b|eps)*({})|(a|eps)))*(((b)(b|eps)*(a)|({}))((b)(b|eps)*(a)|(eps))*((b)(b|eps)*({})|(a))|((b)(b|eps)*({})|(a|eps)))|(((b|eps)(b|eps)*(a)|(a))((b)(b|eps)*(a)|(eps))*((b)(b|eps)*({})|(a))|((b|eps)(b|eps)*({})|({})))