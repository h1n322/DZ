# OpenRouter AI Chatbot 

Цей проєкт є виконанням Домашнього завдання 18. Це вебзастосунок на базі Streamlit, який працює з моделями через OpenRouter REST API.

## Функціонал
- **Три режими асистента:** Python tutor, Code reviewer, Study assistant.
- **Експорт чату:** можливість завантажити історію діалогу у форматі Markdown.
- **Безпека:** API ключі зберігаються безпечно через Streamlit Secrets і не потрапляють у код.

## Локальний запуск
1. Клонуйте репозиторій.
2. Створіть віртуальне оточення та встановіть залежності: `pip install -r requirements.txt`
3. Створіть файл `.streamlit/secrets.toml` у корені проєкту та додайте ваш ключ:
   `OPENROUTER_API_KEY="ваш_ключ"`
4. Запустіть застосунок: `streamlit run app.py`
