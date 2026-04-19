from flask import Flask, render_template, request

app = Flask(__name__)

# ====================== 1. KONTAKT ======================
@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    res = None
    if request.method == 'POST':
        ism = request.form.get('ism', '').strip()
        email = request.form.get('email', '').strip()
        xabar = request.form.get('xabar', '').strip()

        if len(ism) > 2 and '@' in email and len(xabar) >= 15:
            res = [ism, email, xabar]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('kontakt.html', res=res, title="Kontakt")


# ====================== 2. RO‘YXATDAN O‘TISH ======================
@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    res = None
    if request.method == 'POST':
        foydalanuvchi_nomi = request.form.get('foydalanuvchi_nomi', '').strip()
        telefon = request.form.get('telefon', '').strip()
        yosh_str = request.form.get('yosh', '').strip()

        try:
            yosh = int(yosh_str)
            yosh_togri = 18 <= yosh <= 99
        except ValueError:
            yosh_togri = False

        if (len(foydalanuvchi_nomi) > 4 and 
            telefon.startswith('+') and len(telefon) >= 11 and 
            yosh_togri):
            res = [foydalanuvchi_nomi, telefon, str(yosh)]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('register.html', res=res, title="Ro'yxatdan o'tish")


# ====================== 3. KITOB QO‘SHISH ======================
@app.route('/kitob', methods=['GET', 'POST'])
def kitob():
    res = None
    if request.method == 'POST':
        kitob_nomi = request.form.get('kitob_nomi', '').strip()
        muallif = request.form.get('muallif', '').strip()
        sahifalar_str = request.form.get('sahifalar', '').strip()

        try:
            sahifalar = int(sahifalar_str)
            sahifalar_togri = sahifalar >= 50
        except ValueError:
            sahifalar_togri = False

        if len(kitob_nomi) > 3 and len(muallif) > 3 and sahifalar_togri:
            res = [kitob_nomi, muallif, str(sahifalar)]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('kitob.html', res=res, title="Kitob qo'shish")


# ====================== 4. FIKR-MULOHAZA (BAHOLASH) ======================
@app.route('/fikr', methods=['GET', 'POST'])
def fikr():
    res = None
    if request.method == 'POST':
        ism = request.form.get('ism', '').strip()
        baho_str = request.form.get('baho', '').strip()
        sharh = request.form.get('sharh', '').strip()

        # Baho validatsiyasi: faqat 1,2,3,4,5 bo‘lishi mumkin
        try:
            baho = int(baho_str)
            baho_togri = baho in [1, 2, 3, 4, 5]
        except ValueError:
            baho_togri = False

        if len(ism) > 2 and baho_togri and len(sharh) >= 10:
            res = [ism, str(baho), sharh]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('fikr.html', res=res, title="Fikr-mulohaza")


if __name__ == '__main__':
    app.run(debug=True)
