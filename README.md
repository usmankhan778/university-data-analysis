# Pakistan IT Universities Benchmarks Dashboard

A comprehensive data visualization project analyzing Pakistani IT universities using Matplotlib.

## Overview

This project visualizes performance benchmarks for 16 Pakistani universities based on:
- QS World University Rankings (2026)
- Academic Reputation
- Citations Per Paper
- Employer Reputation
- International Research Network
- Annual Academic Costs

## Dashboard Features

The interactive dashboard includes **9 different visualizations**:

1. **Scatter Plot** - Cost vs Academic Reputation relationship
2. **Bar Chart** - Top 5 Universities by Research Citations
3. **Comparison Chart** - Public vs Private universities metrics
4. **Histogram** - Citation distribution across universities
5. **Pie Chart** - University distribution by city location
6. **Line Chart** - Top 10 employer reputation trends
7. **Box Plot** - Annual cost distribution by institution type
8. **Heatmap** - Correlation between key metrics
9. **Bubble Chart** - Multi-dimensional metric comparison

## Installation

### Requirements
- Python 3.8+
- pandas
- matplotlib
- numpy

### Setup

```bash
pip install pandas matplotlib numpy
```

## Usage

Run the analysis script:

```bash
python analysis.py
```

This will generate `PakIT_Dashboard.png` (high resolution 300 DPI)

## Dataset

- **Source**: Kaggle - PakIT Benchmarks dataset
- **Universities**: 16 major Pakistani IT institutions
- **Metrics**: 9 key performance indicators
- **File**: `PakIT_Benchmarks_dataset.csv.csv`

## Key Insights

- **Top Ranked**: NUST leads at rank 114
- **Cost Range**: PKR 121,720 (Public) to PKR 1,938,600 (LUMS)
- **Research Leaders**: High citations from COMSATS (88.8) and UET (80.5)
- **Location Concentration**: Islamabad and Lahore host majority of universities

## Files

```
├── analysis.py                          # Main visualization script
├── PakIT_Dashboard.png                  # Generated dashboard image
├── PakIT_Benchmarks_dataset.csv.csv     # Dataset
└── README.md                            # Documentation
```

## Visualizations Used

- **Scatter Plots** - Relationship analysis
- **Bar Charts** - Comparative analysis
- **Histograms** - Distribution analysis
- **Pie Charts** - Composition analysis
- **Line Charts** - Trend analysis
- **Box Plots** - Statistical distribution
- **Heatmaps** - Correlation analysis
- **Bubble Charts** - Multi-dimensional analysis

## Author

Created as a Matplotlib learning project showcasing real-world data visualization techniques.

## License

MIT License - Feel free to use this project for educational purposes.
