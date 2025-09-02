#from flask_login import login_user
#from app.forms import LoginForm
#from app.models import Usuario
#from app import app, db
#
#@app.route("/", methods=["GET", "POST"])
#def index():
#    form = LoginForm()
#    if form.validate_on_submit():
#        usuario = Usuario.query.filter_by(email=form.email.data).first()
#        if usuario and usuario.check_password(form.senha.data):
#            login_user(usuario)
#            flash("Login realizado com sucesso!", "success")
#            return redirect(url_for("listar_veiculos"))
#        else:
#           flash("Credenciais inválidas", "danger")
#    return render_template("index.html", title="Página inicial", form=form)



#@app.route("/login", methods=["GET", "POST"])
#def login():
#    if request.method == "POST":
#        email = request.form["email"]
#        senha = request.form["senha"]
#        usuario = Usuario.query.filter_by(email=email).first()
#        if usuario and usuario.check_password(senha):
#            login_user(usuario)
#            flash("Login realizado com sucesso!", "success")
#            return redirect(url_for("listar_veiculos"))
#        else:
#            flash("Credenciais inválidas", "danger")
#    return render_template("index.html", title="Login")




#Inicio
#@app.route("/")
#def index():
#    return render_template("index.html", title="Página Inicial")


#app = Flask(__name__, template_folder="templates", static_folder="static")

#app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
#app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'
#app.config['ENV'] = os.getenv('FLASK_ENV', 'development')


#Formulário
#@app.route("/form", methods=["GET", "POST"])
#def form():
#    form = NomeForm()
#    mensagem = None
#    if form.validate_on_submit():
#        nome = form.nome.data
#       mensagem = f"Olá, {nome}! Formulário recebido com sucesso."
#    return render_template("form.html", title="Formulário", form=form, mensagem=mensagem)


#class CarroForm(FlaskForm):
#    placa = StringField("Nome do Produto", validators=[DataRequired()])
#    modelo = FloatField("Preço", validators=[DataRequired(), NumberRange(min=0)])
#    cor = IntegerField("Estoque", validators=[NumberRange(min=0)])
#    submit = SubmitField("Salvar")




#@app.route("/", methods=["GET", "POST"])
#def index():
    

#    form = LoginForm()
#    if form.validate_on_submit():
#        usuario = Usuario.query.filter_by(email=form.email.data).first()
#        if usuario and usuario.check_password(form.senha.data):
#            login_user(usuario)
#            flash("Login realizado com sucesso!", "success")
#            return redirect(url_for("listar_veiculos"))
#        else:
#            flash("Credenciais inválidas", "danger")
#    return render_template("index.html", title="Página inicial", form=form)


#            access_token = create_access_token(
#                identity=str(usuario.id),
#                expires_delta=timedelta(minutes=15)
#            )

#            flash(f"Token JWT gerado (válido por 15m): {access_token}", "info")