from flask import render_template, request


def logout():
    mensaje = 'Su sesión ha finalizado con exito'
    return render_template(
        'login.html',
        title   = 'Login',
        message = mensaje
    )


def login():
    if request.method == 'POST':
        if request.form['user'] == "sd" and request.form['passwd'] == "test0815":
            return render_template(
                'home.html',
                title='Home'
            )
        else:
            return render_template(
                'login.html',
                title   = 'Login',
                message = 'Clave o usuario Incorrecto'
            )

    return render_template(
        'login.html',
        title   = 'Login',
        message = 'Bienvenido'
    )
