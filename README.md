# CV RAG Chatbot 

Bu proje, Flask tabanlı bir RAG (Retrieval-Augmented Generation) sistemi kullanarak kullanıcının yüklediği CV (PDF) dokümanı üzerinden soru–cevap yapan bir chatbot uygulamasıdır. Sistem, kullanıcı sorularını önce CV içeriğinden ilgili bölümlerle eşleştirir ve yalnızca bu bağlama dayanarak cevap üretir. CV’de bulunmayan bilgiler için “CV’de bu bilgi yer almıyor.” şeklinde yanıt verir.

Özellikler:
- CV PDF’ten otomatik metin çıkarma
- Metin parçalama (chunking)
- Sentence Transformers ile embedding oluşturma
- FAISS ile vektör tabanlı benzerlik araması
- OpenAI GPT ile bağlama dayalı cevap üretimi
- Flask tabanlı REST API
- Tek sayfalı web chatbot arayüzü

Kullanılan Teknolojiler:
Python, Flask, Sentence-Transformers, FAISS, OpenAI GPT, HTML, CSS, JavaScript

Proje Yapısı:
cv-rag-chatbot/
app.py
requirements.txt
.env
data/cv.pdf
rag/
templates/
static/
README.md

Kurulum:
git clone https://github.com/yourusername/cv-rag-chatbot.git
cd cv-rag-chatbot
pip install -r requirements.txt

.env dosyasına OpenAI API anahtarınızı ekleyin:
OPENAI_API_KEY=your_openai_api_key

CV dosyanızı data/cv.pdf olarak projeye ekleyin.

Çalıştırma:
python app.py
Tarayıcıdan erişim:
http://127.0.0.1:5000

Kullanım:
Chatbot’a CV ile ilgili sorular sorabilirsiniz.
Örnek:
- Hangi teknolojilerle çalışmış?
- Staj deneyimleri neler?
- Makine öğrenmesi tecrübesi var mı?

Sistem yalnızca CV içeriğine göre cevap üretir.

Amaç:
Bu proje, doküman tabanlı soru–cevap sistemlerinin ve RAG mimarisinin gerçek hayatta (CV analizi) nasıl uygulanabileceğini göstermek amacıyla geliştirilmiştir.
