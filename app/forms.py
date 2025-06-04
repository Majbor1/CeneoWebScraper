from wtforms import Form, StringField, SubmitField, validators

class ProductForm(Form):
    product_id = StringField("Kod produktu", 
                            name='product_id', 
                            id='product_id',
                            validators=[
                                validators.DataRequired(message="Kod produktu jest wymagany"),
                                validators.Regexp("^[0-9]*$", message="Kod produktu musi zawierać jedynie cyfry"),
                                validators.Length(min=5, max=10, message="Kod produktu musi zawierać od 5 do 10 cyfr")
                            ])
    submit = SubmitField("Pobierz opinie")
    