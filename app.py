from flask import Flask, render_template, request, jsonify
import os
import random
from datetime import datetime

app = Flask(__name__)

CONTENT_TEMPLATES = {
    "moda": [
        "{topic} için 3 kombin hatası ve doğru alternatifler",
        "{topic} trendini uygun fiyatla nasıl uygularsın?",
        "1 parçayla 5 farklı {topic} görünümü",
        "Kimse konuşmuyor ama {topic} seçerken buna dikkat et",
        "Öncesi / sonrası: {topic} ile görünüm dönüşümü",
        "{topic} alışverişinde paranı boşa harcatan 5 hata",
        "Bu sezonun en kurtarıcı {topic} parçaları",
        "{topic} için sabah 5 dakikada hazır olma rehberi",
        "Takipçilerime göre en iyi {topic} tercihi hangisi?",
        "Bunu giyince herkes nereden aldığını soracak: {topic} önerileri"
    ],
    "güzellik": [
        "{topic} için sabah rutini: 10 dakikalık plan",
        "{topic} konusunda en sık yapılan 5 hata",
        "Uygun fiyatlı vs pahalı: {topic} ürün karşılaştırması",
        "Bir hafta boyunca {topic} rutinimi denedim",
        "{topic} hakkında doğru bilinen yanlışlar",
        "Takipçilerden gelen en iyi {topic} soruları",
        "{topic} ile daha bakımlı görünmenin kolay yolu",
        "{topic} için mini rehber: ne zaman, nasıl, neden?",
        "Gerçek sonuçlar: {topic} öncesi ve sonrası",
        "Yeni başlayanlar için {topic} checklist"
    ],
    "fitness": [
        "{topic} için 15 dakikalık ev rutini",
        "{topic} hedefi olanlar için en büyük 5 hata",
        "1 haftalık {topic} challenge başlıyor",
        "{topic} için marketten alınabilecek pratik ürünler",
        "Yeni başlayanlar için {topic} planı",
        "{topic} yaparken motivasyonu koruma yolları",
        "Öncesi / sonrası: {topic} sürecim",
        "{topic} için en etkili 3 hareket",
        "Takipçilerimin en çok sorduğu {topic} soruları",
        "{topic} sürecinde düzen nasıl kurulur?"
    ],
    "genel": [
        "{topic} hakkında kimsenin söylemediği 3 şey",
        "{topic} için yeni başlayan rehberi",
        "{topic} ile ilgili sık yapılan hatalar",
        "Takipçilerden gelen {topic} sorularını cevaplıyorum",
        "{topic} konusunda bildiklerimi 30 saniyede anlatıyorum",
        "{topic} için mini kontrol listesi",
        "Bir günde değil ama düzenli yapınca {topic} böyle değişiyor",
        "{topic} hakkında dürüst yorumlarım",
        "Neden herkes {topic} konuşuyor?",
        "{topic} için kolay uygulanabilir 5 öneri"
    ]
}

CAPTION_TEMPLATES = [
    "Bunu kaydet çünkü sonra lazım olacak. {topic} konusunda işine yarayacak en net ipuçlarını topladım.",
    "Herkes aynı şeyi yapıyor ama sonuç alamıyor. {topic} için gerçekten çalışan detaylar burada.",
    "Bu içerik tam paylaşmalık. {topic} ile ilgilenen birine gönder.",
    "Ben olsam bunu kaçırmazdım. {topic} konusunda küçük ama etkili farklar büyük sonuç getiriyor.",
    "Yorumlara fikrini yaz: {topic} için senin en büyük problemin ne?",
    "Kaydet, dene, sonra bana sonucu yaz. {topic} için pratik öneriler burada.",
    "Bu kadar basit olup bu kadar işe yarayan az şey var. {topic} için net rehber.",
    "Gerçekçi konuşalım: {topic} konusunda mükemmel olman gerekmiyor, sürdürülebilir olman gerekiyor."
]

HASHTAG_BANK = {
    "moda": ["#moda", "#kombin", "#stil", "#outfitinspo", "#fashiontips", "#gununkombini", "#dolapduzeni", "#trendler", "#modailhamı", "#reelsfashion"],
    "güzellik": ["#güzellik", "#bakım", "#skincare", "#makeup", "#ciltbakımı", "#beautytips", "#güzellikönerileri", "#selfcare", "#reelsbeauty", "#bakımrutini"],
    "fitness": ["#fitness", "#spormotivasyon", "#evdeantrenman", "#saglikliyasam", "#fityasam", "#hedef", "#routine", "#egzersiz", "#reelsfitness", "#motivasyon"],
    "genel": ["#keşfet", "#reels", "#viral", "#icerik", "#sosyalmedya", "#üretkenlik", "#ipucu", "#öneri", "#growth", "#creator"]
}

BEST_TIMES = {
    "instagram": ["12:30", "18:00", "20:30", "21:30"],
    "tiktok": ["13:00", "19:00", "21:00", "22:30"],
    "linkedin": ["08:30", "12:00", "17:30"],
}

DAYS = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
FORMATS = ["Reels", "Carousel", "Story", "Tek görsel", "Mini vlog"]
HOOKS = [
    "Bunu kimse konuşmuyor ama...",
    "Eğer {topic} ile ilgileniyorsan bunu bilmelisin:",
    "Bu hatayı yapıyorsan büyümen yavaşlıyor.",
    "30 saniyede anlatıyorum:",
    "Kaydetmelik içerik geldi:",
]


def pick_category(topic: str) -> str:
    lowered = topic.lower()
    if any(word in lowered for word in ["moda", "kombin", "stil", "giyim", "kıyafet"]):
        return "moda"
    if any(word in lowered for word in ["makyaj", "cilt", "güzellik", "bakım", "saç"]):
        return "güzellik"
    if any(word in lowered for word in ["spor", "fitness", "diyet", "antrenman", "kilo"]):
        return "fitness"
    return "genel"


def generate_pack(topic: str, platform: str, tone: str):
    category = pick_category(topic)
    ideas = random.sample(CONTENT_TEMPLATES[category], 6)
    ideas = [idea.format(topic=topic.title()) for idea in ideas]

    captions = random.sample(CAPTION_TEMPLATES, 3)
    captions = [f"{random.choice(HOOKS).format(topic=topic.title())} {c.format(topic=topic.title())} Ton: {tone.title()}." for c in captions]

    hashtags = random.sample(HASHTAG_BANK[category], min(8, len(HASHTAG_BANK[category])))
    hashtags += random.sample(HASHTAG_BANK["genel"], 4)

    best_times = BEST_TIMES.get(platform, BEST_TIMES["instagram"])
    calendar = []
    for i, day in enumerate(DAYS[:5]):
        calendar.append({
            "day": day,
            "format": random.choice(FORMATS),
            "idea": ideas[i % len(ideas)],
            "time": best_times[i % len(best_times)]
        })

    return {
        "ideas": ideas,
        "captions": captions,
        "hashtags": hashtags,
        "best_times": best_times,
        "calendar": calendar,
    }


@app.route("/")
def index():
    return render_template("index.html", year=datetime.now().year)


@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json(force=True)
    topic = (data.get("topic") or "içerik üretimi").strip()
    platform = (data.get("platform") or "instagram").strip().lower()
    tone = (data.get("tone") or "samimi").strip().lower()

    result = generate_pack(topic, platform, tone)
    return jsonify(result)


@app.route("/api/audit", methods=["POST"])
def api_audit():
    data = request.get_json(force=True)
    username = (data.get("username") or "creator").replace("@", "").strip()
    niche = (data.get("niche") or "genel içerik").strip()

    seed = sum(ord(c) for c in username)
    random.seed(seed)
    score = random.randint(68, 91)
    strengths = random.sample([
        "Kullanıcı adı akılda kalıcı görünüyor",
        "Niş alanı netleştirilebilir ama potansiyel var",
        "Reels odaklı büyüme için uygun bir yapı var",
        "Düzenli seri içerik oluşturulursa görünürlük artabilir",
        "Topluluk etkileşimini artıracak soru formatı uygun",
        "Kaydetmelik içerik üretimine yatkın bir konu seçimi"
    ], 3)
    improvements = random.sample([
        "Biyografi kısmında değer önerisi daha net yazılmalı",
        "Sabit içerik serileri oluşturulmalı",
        "Kapak görselleri daha tutarlı olmalı",
        "İlk 3 saniyeyi güçlendiren kanca cümleler eklenmeli",
        "Yorum çağrısı ve DM yönlendirmesi artırılmalı",
        "Aynı nişte haftada en az 4 içerik paylaşılmalı"
    ], 4)

    audit = {
        "username": username,
        "niche": niche,
        "score": score,
        "strengths": strengths,
        "improvements": improvements,
        "content_pillars": [
            f"{niche} ipuçları",
            f"{niche} öncesi/sonrası",
            f"{niche} sık yapılan hatalar",
            f"{niche} mini rehberler"
        ]
    }
    return jsonify(audit)


if __name__ == "__main__":
    app.run(debug=True)
