# 💼 Flask Portfolio Website with Contact Form (SMTP Integration)

This is a personal **portfolio website** built using **Flask** that showcases your profile and projects. It includes a fully functional **contact form** that sends emails using **SMTP** and custom **HTML email templates**.

## 🚀 Features

- Clean and responsive HTML/CSS design
- Flask backend with Jinja2 templating
- Contact form with validation and success message
- Sends emails with SMTP using custom HTML templates
- Modular and easy to customize

## 🖼️ Screenshots

![Portfolio Screenshot](https://via.placeholder.com/800x400.png?text=Add+Your+Screenshot+Here)

## 📂 Folder Structure

```
portfolio/
│
├── static/
│   └── style.css             # Custom styles
│
├── templates/
│   ├── index.html            # Main portfolio page
│   └── email_template.html   # HTML email design
│
├── .env                      # Environment variables (EMAIL, PASSWORD)
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/flask-portfolio.git
cd flask-portfolio
```

2. **Create and Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**

Create a `.env` file in the root directory and add your email and password:
```
EMAIL=youremail@example.com
PASSWORD=yourpassword
```

> ⚠️ Use [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) if you're using Gmail.

5. **Run the App**
```bash
python app.py
```

6. **Visit in Browser**
```
http://127.0.0.1:5000/
```

## 💌 Email Template

Beautifully designed HTML email template with custom animation and style, embedded with user-submitted details.

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3
- **Backend:** Flask (Python)
- **Email:** SMTP with smtplib, email.message
- **Templating:** Jinja2

## 📧 Contact

If you'd like to connect or collaborate, feel free to use the contact form on the website — it works! 😄

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

### 🌟 Show some love!

If you liked this project, give it a ⭐ on GitHub!
