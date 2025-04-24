/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        'primary-bg': '#0F0F1A',
        'primary-text': '#FFFFFF',
        'secondary-text': '#CCCCCC',
        'accent': '#F0F',
        'gradient-start': '#E100FF',
        'gradient-end': '#7F00FF'
      },
      fontFamily: {
        'rethink': ['"Rethink Sans"', 'sans-serif']
      }
    }
  },
  plugins: []
};
