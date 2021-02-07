import os


# getting all the classes and ids declared in your specified markup file
def markup_check(file_name):
    classes_name = []
    with open(f'{file_name}.html', 'r') as file:
        for f in file:
            for word in f.split():
                if 'class="' in word or 'id="' in word:
                    try:
                        classes_name.append(word.split('"')[1])
                    except:
                        pass

    return classes_name


def cls_helper(delimiter, f):  # function helper for style_sheet function
    classes_id = []

    for clsid in f.split(delimiter)[:-1]:
        if clsid != 'body' and clsid != '*' and clsid != ':root':
            classes_id.append(clsid[1:])

    return classes_id


# getting all the classes and ids declared in your css except for body, * and :root element type selector
def style_sheet(file_name):
    classes_id = []

    with open(f'{file_name}.css', 'r') as file:
        for f in file:
            delimiter = ' '
            if '{' in f:
                classes_id += cls_helper(delimiter, f)
            elif ',' in f:
                delimiter = ','
                classes_id += cls_helper(delimiter, f)

    return classes_id


# getting all the dead class and id in your specified style sheet
def dead_class(markup, stylesheet):
    markup_idx = 0
    stylesheet_idx = 0

    unused_classes = stylesheet

    for curr_mark in markup:
        for curr_style in stylesheet:
            if curr_mark == curr_style:
                unused_classes.remove(curr_style)

    return unused_classes


def remove_dead_class(dead_class, style):  # removing all the dead class and id
    with open(f'{style}.css', 'r') as file:
        dcls = [f'.{w}' for w in dead_class]

        lines = []
        for f in file:
            for word in dcls:
                if word in f:
                    dcls.remove(word)
                    f = f.replace(word, '')
            lines.append(f)

    with open(f'{style}.css', 'w') as file:
        for no, line in enumerate(lines):
            if line != ',\n':
                file.write(line)


def main():

    # make sure to specify the correct file name or path
    markup = input('markup name: ')
    style = input('stylesheet name: ')

    markup_classes = markup_check(markup)
    style_classes = style_sheet(style)
    # print('markup classes:', markup_classes)
    # print('style classes:', style_classes)
    dead_cls = dead_class(markup_classes, style_classes)
    # print('dead classes:', dead_cls)
    remove_dead_class(dead_cls, style)


if __name__ == '__main__':
    main()
