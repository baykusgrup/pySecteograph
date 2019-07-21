import click
from datetime import datetime
from lib.classes.secteograph import Secteograph


@click.group()
def main():
    pass


@click.command()
@click.option('--user', type=click.STRING, help='Who you insert related to-dos')
@click.option('--start', required=True, type=click.STRING, help='When do you start your to-dos')
@click.option('--end', required=True, type=click.STRING, help='When do you end your to-dos')
@click.argument('desc', nargs=1, required=True, type=click.STRING)
def add(start, end, desc, user):
    #  TODO :: add a to-do to file
    # Examples :: desc from to user
    Secteograph.addTodo(start, end, desc, user)


@click.command()
@click.option('--user', required=True, type=click.STRING, help='When do you start your to-dos')
@click.option('--start', type=click.STRING, help='When do you start your to-dos')
@click.option('--end', type=click.STRING, help='When do you start your to-dos')
@click.option('-f', is_flag=True, required=False, type=click.STRING, help='When do you start your to-dos')
@click.argument('desc', nargs=1, required=True, type=click.STRING)
def delete(user, start, end, desc, f):
    #  TODO :: delete a todo by  specific user, start date or end date
    # Examples :: desc from to user
    Secteograph.deleteTodo(start, end, desc, user)


@click.command()
@click.option('--user', type=click.STRING, default='*', help='When do you start your to-dos')
@click.option('--start', type=click.STRING, help='When do you start your to-dos')
@click.option('--end', type=click.STRING, help='When do you start your to-dos')
@click.option('-a', '--all', is_flag=True, default=False, type=click.STRING, help='Get all to-dos')
@click.argument('desc', nargs=1, required=True, type=click.STRING)
def get(start, end, desc, user, all):
     #  TODO :: get to-do list by  specific user, start date or end date
    # Examples :: desc from to user
    Secteograph.getTodo(start, end, desc, user)


main.add_command(add)
main.add_command(delete)
main.add_command(get)

if __name__ == "__main__":
    main()
