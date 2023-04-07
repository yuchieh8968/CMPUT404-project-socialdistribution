/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./backend/apps/**/templates/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
