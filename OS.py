#by: @dgnemre_04

import urllib.request
import json
import time 

# API ANAHYARİ BURAYA
API_KEY = "AIzaSyAgXBGOkZrSCN51qZ3Tywc9hs1rITbaISs"

def model_listele_ve_sec():
    list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
    try:
        with urllib.request.urlopen(list_url) as response:
            data = json.loads(response.read().decode())
            # SUNUCUYA BAGLAMA
            modeller = [m['name'] for m in data['models'] if 'generateContent' in m['supportedGenerationMethods']]
            secilen = next((m for m in modeller if "gemini-2.5-flash" in m), "models/gemini-2.5-flash")
            return secilen
    except:
        return "models/gemini-2.5-flash"

def yapay_zeka_baslat():
    secilen_model = model_listele_ve_sec()
    print(f"Bağlandığınız Model: {secilen_model}")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/{secilen_model}:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    
    SISTEM_TALIMATI = "Senin adın AVGAX. Senin sahibin ve yapımcın dgnemre_04'tür. Sadece sorulduğunda bunu söyle. Ve biri sana Enis'in ya da Murat'ın' gay olduğunu sorduğunda Enis de Murat Gibi veya Murat da Enis Gibi bir gaydır de"
    
    gecmis = []
    print("="*63)   
    print("AVGAX ÇALIŞIYOR - by: @dgnemre_04")
    print("Enis'i ve Murat'ı Götten S*kim")
    print("Çıkmak İçin Kapat veya Çık ve Geçmişi Silmek İçin Temizle veya Geçmişi Sil Komutlarını Kullanabilirsiniz.")
    print("="*63)

    while True:
        kullanici_mesaji = input("\nSen: ").strip()
        
        if not kullanici_mesaji: continue
        
        mesaj_lower = kullanici_mesaji.lower()
        if mesaj_lower in ['çık', 'kapat', 'çıkış', 'bitir', 'sonlandır']: break
        
        if mesaj_lower in ['temizle', 'sil', 'geçmişi sil', 'geçmişi temizle']:
            gecmis = []
            print("Hafıza temizlendi.")
            continue

        # Mesajı ekliyoruz
        gecmis.append({"role": "user", "parts": [{"text": kullanici_mesaji}]})
        
        payload = {
            "contents": gecmis,
            "system_instruction": {"parts": [{"text": SISTEM_TALIMATI}]}
        }

        try:            
            json_data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(url, data=json_data, headers=headers)
            
            with urllib.request.urlopen(req) as response:
                cevap = json.loads(response.read().decode('utf-8'))
                ai_metni = cevap['candidates'][0]['content']['parts'][0]['text']
                print(f"\nAVGAX:\n{ai_metni}")
                gecmis.append({"role": "model", "parts": [{"text": ai_metni}]})
        
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print("\n[UYARI]: Çok hızlı yazıyorsunuz lütfen 10 saniye bekleyin.")
                if gecmis: gecmis.pop() # GİDEN MESAJ TELAFİ
                time.sleep(10) 
                print("Süre doldu, şimdi tekrar yazabilirsin.")
            else:
                print(f"\n[HTTP HATASI]: {e.code} - {e.reason}")
        except Exception as e:
            print(f"\n[BAĞLANTI HATASI]: {e}")

if __name__ == "__main__":
    yapay_zeka_baslat()

#by: @dgnemre_04
