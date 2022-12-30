import string

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'


template_text = '''
  Delimiter : %%
  Replaced  : %with_underscore
  Ignored   : %notunderscored
'''

d = {
    'with_underscore': 'replaced',
    'notunderscored': 'not replaced',
}

def print_capwords():
    s = 'The quick brown fox jumped over the lazy dog.'
    print(s)
    print(string.capwords(s))

def use_template():
    values = {'var': 'foo'}

    t = string.Template("$var is here but $missing is not provided")
    print('patern' + t.pattern.pattern)

    try:
        print('TEMPLATE:', t.substitute(values))
    except KeyError as err:
        print('ERROR:', str(err))

    print('safe_substitute():', t.safe_substitute(values))

    s = """
    Variable        : %(var)s
    Escape          : %%
    Variable in text: %(var)siable
    """

    print('INTERPOLATION:', s % values)

    s = """
    Variable        : {var}
    Escape          : {{}}
    Variable in text: {var}iable
    """

    print('FORMAT:', s.format(**values))

def use_mytemplate():
    t = MyTemplate(template_text)
    print('Modified ID pattern:')
    print(t.safe_substitute(d))
