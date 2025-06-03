from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('main1.html')

msg = template.render(title='Домашнее задание')

print(msg)

