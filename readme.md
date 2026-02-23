# Comic Crafter 🎨🧠

Comic Crafter is an AI-powered project that generates comics using the Gemini API.

---

## 🚀 Setup Instructions

Follow the steps below to run this project locally.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rohan-Aroli/Comic-Crafter-.git
cd Comic-Crafter-
```

---

## 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

### Activate the Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create a `.env` File

In the root directory of the project, create a file named:

```
.env
```

Inside the `.env` file, paste your Gemini API key like this:

```
GEMINI_API_KEY=your_actual_api_key_here
```

Replace `your_actual_api_key_here` with your real Gemini API key.

⚠️ Important:
- Do NOT share your API key.
- Do NOT commit or push the `.env` file to GitHub.

---

## 5️⃣ Run the Project

```bash
python main.py
```

(If your entry file has a different name, replace `main.py` accordingly.)

---

## 🔐 Required Environment Variable

This project requires:

- `GEMINI_API_KEY`

Make sure it is correctly added inside your `.env` file.

---

## 📦 Requirements

All required packages are listed in:

```
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🛑 Notes

- Python 3.8+ recommended
- Keep your API key private
- Ensure `.env` is added to `.gitignore`
