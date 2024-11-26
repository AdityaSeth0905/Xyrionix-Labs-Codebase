/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'xyronix-primary': '#3B82F6',
        'xyronix-secondary': '#10B981',
      },
    },
  },
  plugins: [],
}