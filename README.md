# TrendBoost AI

TrendBoost AI, sosyal medya içerik üreticileri için hazırlanmış basit ama şık bir demo projedir. Kullanıcıdan konu, platform ve ton bilgisi alarak içerik fikirleri, caption önerileri, hashtag listesi, paylaşım saatleri ve haftalık içerik planı üretir. Ayrıca örnek bir profil audit ekranı da içerir.

## Özellikler
- İçerik fikri üretimi
- Caption önerileri
- Hashtag üretimi
- En iyi paylaşım saatleri
- 5 günlük içerik planı
- Profil / rakip audit demo ekranı
- Responsive tasarım

## Teknolojiler
- Python
- Flask
- HTML
- CSS
- JavaScript

## Kurulum
```bash
python -m venv venv
source venv/bin/activate   # Windows için: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Ardından tarayıcıda `http://127.0.0.1:5000` adresini aç.

## Proje Yapısı
```text
trendboost_ai/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## Not
Bu proje demo amaçlıdır. Gerçek sosyal medya verisi çekmez. GitHub portföyü, frontend/backend pratiği ve ürün fikri göstermek için uygundur.
