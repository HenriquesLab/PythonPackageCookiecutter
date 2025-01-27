from {{cookiecutter.package_name}}.{{cookiecutter.file_name}} import {{cookiecutter.class_name}}

def test_{{cookiecutter.class_name}}():

    # initialize your class
    my_class = {{cookiecutter.class_name}}()

    # run the main method of the class
    example_output = my_class.run()

    # assert example output is 1
    assert example_output == 1
