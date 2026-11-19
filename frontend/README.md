# Frontend

React + Vite + Tailwind CSS + React Router + Recharts + Lucide React + Axios + Supabase JS.

## Suggested setup

```powershell
cd frontend
npm create vite@latest . -- --template react
npm install
npm install @supabase/supabase-js axios react-router-dom recharts lucide-react
npm install -D tailwindcss @tailwindcss/vite
```

Create `.env` from `.env.example`, then run:

```powershell
npm run dev
```

## Environment

See `.env.example`. Only the Supabase publishable/anon key belongs in the browser.
