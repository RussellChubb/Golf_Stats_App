# Golfah ⛳

> Using Data to Improve Your Golf Game

A modern, data-driven golf analytics platform built with Streamlit. Track your rounds, analyze your performance, and improve your game with beautiful visualizations and insightful metrics.

## ✨ Features

- **📊 Performance Dashboard** - View your best scores, averages, and trends at a glance
- **🏌️ Round Tracking** - Log and review all your golf rounds with detailed statistics
- **📈 Score Trends** - Visualize your improvement over time with interactive charts
- **⛳ Hole Analysis** - Deep dive into performance by individual holes
- **🎯 Par Analysis** - Track how you perform against par across different courses

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/golfah.git
cd golfah
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 📦 Dependencies

- `streamlit` - Web application framework
- `pandas` - Data manipulation and analysis
- `plotly` - Interactive visualizations
- `streamlit-option-menu` - Enhanced navigation menu

## 🎨 Design Philosophy

Golfah features a modern, dark-themed interface with:

- **Custom Fonts**: Space Grotesk for headings, Martian Mono for accents
- **Golf-Themed Colors**: Green accents inspired by the fairway
- **Responsive Layout**: Optimized for desktop and mobile viewing
- **Clean Metrics**: Easy-to-read performance indicators

## 📁 Project Structure

```
golfah/
├── app.py                 # Main application file
├── utils/
│   ├── data_loader.py    # Data loading utilities
│   ├── metrics.py        # Statistical calculations
│   └── visuals.py        # Chart generation
├── data/
│   ├── summary_df.csv    # Round summaries
│   ├── rounds_df.csv     # Detailed round data
│   └── course_df.csv     # Course information
└── requirements.txt      # Python dependencies
```

## 🎯 Usage

### Adding a Round

1. Navigate to the **Add Round** page
2. Select your course and date
3. Enter your scores for each hole
4. Save your round to see updated statistics

### Analyzing Performance

- Use the **Home** page to view overall statistics
- Check **Hole Analysis** for detailed breakdowns
- Review **Round Summary** for comprehensive reports
- Toggle between 9-hole and 18-hole views

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Icons from [Bootstrap Icons](https://icons.getbootstrap.com/)
- Inspired by the love of golf and data analytics

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Golfing!** 🏌️‍♂️⛳

*Track your progress. Lower your scores. Enjoy the game.*
