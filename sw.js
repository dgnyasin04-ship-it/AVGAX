const CACHE_NAME = 'avgax-ultra-v1';

// Uygulamanın çalışması için gereken dosyalar
const assets = [
  './',
  './index.html',
  './manifest.json',
  './1577.jpg' 
];

// Servis çalışanını kur ve dosyaları önbelleğe al
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('Dosyalar önbelleğe alınıyor...');
      return cache.addAll(assets);
    })
  );
});

// Uygulama açıldığında dosyaları hızlıca getir
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});

// Eski önbellekleri temizle
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME)
            .map(key => caches.delete(key))
      );
    })
  );
});
