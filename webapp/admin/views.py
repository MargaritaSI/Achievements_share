from flask import Blueprint, render_template
from webapp.user.decorators import admin_required #like login_required - decorator for check user rights/access

blueprint = Blueprint('admin', __name__, url_prefix='/admin') # name Blueprint, modul name, start of all urls)

@blueprint.route('/')
@admin_required  # decorator - before function will be accessed it goes for flask handler, if user doesn't authenticated -> return error and user returned to login, and if user not an admin he doesn't shell
def admin_index():
    #return 'Hello admin!'
    title = 'control Panel'
    return render_template('admin/index.html', page_title=title)