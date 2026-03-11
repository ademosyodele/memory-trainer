const CACHE_NAME = 'memory-trainer-v6';
const ASSETS = [
    './',
    'index.html',
    'https://cdn.jsdelivr.net/npm/chart.js',
    'manifest.json',
    'icon-192.png',
    'icon-512.png'
];

// Install Service Worker
self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
    );
});

// Fetch from Cache
self.addEventListener('fetch', (e) => {
    e.respondWith(
        caches.match(e.request).then((response) => response || fetch(e.request))
    );
});