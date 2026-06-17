import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import { VitePWA } from 'vite-plugin-pwa'

// https://vite.dev/config/
export default defineConfig({
  // 相対パスにしておくと、どのホスティング（ルート/サブパス）でも動く
  base: './',
  plugins: [
    react(),
    tailwindcss(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.svg', 'icons/apple-touch-icon.png'],
      manifest: {
        name: '土地家屋調査士 トレーニング',
        short_name: '調査士学習',
        description: '過去問択一＋暗記の学習アプリ',
        start_url: '.',
        scope: '.',
        display: 'standalone',
        orientation: 'any',
        background_color: '#f1f5f9',
        theme_color: '#4f46e5',
        lang: 'ja',
        categories: ['education', 'productivity'],
        icons: [
          { src: 'icons/icon-192.png', sizes: '192x192', type: 'image/png', purpose: 'any' },
          { src: 'icons/icon-512.png', sizes: '512x512', type: 'image/png', purpose: 'any' },
          { src: 'icons/icon-maskable-512.png', sizes: '512x512', type: 'image/png', purpose: 'maskable' },
        ],
      },
      workbox: {
        // アプリシェル・データのみ起動時キャッシュ（35MBの書式図面は除外）
        globPatterns: ['**/*.{js,css,html,svg,png,json,woff2}'],
        maximumFileSizeToCacheInBytes: 5 * 1024 * 1024,
        runtimeCaching: [
          {
            // 書式図面 WebP はアクセス時にキャッシュ（CacheFirst 30日）
            urlPattern: /\/kijutsu\/.*\.webp$/,
            handler: 'CacheFirst',
            options: {
              cacheName: 'kijutsu-images-v1',
              expiration: { maxEntries: 800, maxAgeSeconds: 30 * 24 * 60 * 60 },
            },
          },
        ],
      },
    }),
  ],
})
