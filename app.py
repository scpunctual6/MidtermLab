from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        subject = request.form.get('subject')
        other_subject = request.form.get('other_subject')
        contact_method = request.form.getlist('contact_method')
        agreement = request.form.get('agreement')

        errors = []

        if not name or not email or not phone or not message:
            errors.append("Please fill out all required fields.")
        if not phone.isnumeric():
            errors.append("Phone number must be numeric.")
        if subject == 'Other' and not other_subject:
            errors.append("Please specify the subject.")
        if not agreement:
            errors.append("You must agree to the terms.")

        if errors:
            return render_template('contact_form.html', errors=errors, form=request.form)

        subject_final = other_subject if subject == 'Other' else subject

        return render_template('confirmation.html', name=name, email=email, phone=phone,
                               message=message, subject=subject_final,
                               contact_method=", ".join(contact_method),
                               agreement="Yes" if agreement else "No")

    return render_template('contact_form.html', errors=[])

if __name__ == '__main__':
    app.run(debug=True)