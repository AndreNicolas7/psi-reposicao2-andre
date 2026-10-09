from flask import flash, redirect, session, url_for


def exigir_login():
    if "usuario_id" not in session or session["usuario_id"] is None:
        flash("Faça login para acessar esta página.")
        return redirect(url_for("auth.login"))
    return None
