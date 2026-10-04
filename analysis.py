import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the dataset
df = pd.read_csv(r'C:\Users\uk248\Downloads\archive\PakIT_Benchmarks_dataset.csv.csv')

# Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

# Data cleaning
df['Annual Academic Cost (PKR)'] = df['Annual Academic Cost (PKR)'].str.replace(',', '').replace('NA', '0')
df['Annual Academic Cost (PKR)'] = pd.to_numeric(df['Annual Academic Cost (PKR)'], errors='coerce')

# Create figure with subplots (3 rows, 3 columns)
fig = plt.figure(figsize=(20, 14))
fig.suptitle('Pakistan IT Universities - Performance Benchmarks Dashboard', fontsize=20, fontweight='bold', y=0.995)

# ===== PLOT 1: Scatter - Cost vs Academic Reputation =====
ax1 = plt.subplot(3, 3, 1)
colors = ['#FF6B6B' if x == 'Private' else '#4ECDC4' for x in df['Institution Type']]
ax1.scatter(df['Annual Academic Cost (PKR)'], df['Academic Reputation'],
            s=200, c=colors, alpha=0.6, edgecolors='black', linewidth=1.5)
ax1.set_xlabel('Annual Cost (PKR)', fontweight='bold')
ax1.set_ylabel('Academic Reputation Score', fontweight='bold')
ax1.set_title('Cost vs Academic Reputation', fontweight='bold', fontsize=12)
ax1.grid(True, alpha=0.3)
for idx, row in df.iterrows():
    ax1.annotate(row['University Name'][:10],
                (row['Annual Academic Cost (PKR)'], row['Academic Reputation']),
                fontsize=8, alpha=0.7)

# ===== PLOT 2: Bar Chart - Top 5 Universities by Ranking =====
ax2 = plt.subplot(3, 3, 2)
top_5 = df.nlargest(5, 'Citations Per Paper')[['University Name', 'Citations Per Paper']].sort_values('Citations Per Paper')
bars = ax2.barh(top_5['University Name'].str[:20], top_5['Citations Per Paper'], color='#95E1D3')
ax2.set_xlabel('Citations Per Paper', fontweight='bold')
ax2.set_title('Top 5 Universities - Citations', fontweight='bold', fontsize=12)
ax2.invert_yaxis()
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax2.text(width, bar.get_y() + bar.get_height()/2, f'{width:.1f}',
            ha='left', va='center', fontweight='bold')

# ===== PLOT 3: Public vs Private - Average Metrics =====
ax3 = plt.subplot(3, 3, 3)
type_stats = df.groupby('Institution Type')[['Academic Reputation', 'Citations Per Paper', 'Employer Reputation']].mean()
type_stats.plot(kind='bar', ax=ax3, color=['#FF6B6B', '#4ECDC4', '#FFE66D'], width=0.7)
ax3.set_xlabel('Institution Type', fontweight='bold')
ax3.set_ylabel('Average Score', fontweight='bold')
ax3.set_title('Public vs Private Universities - Metrics', fontweight='bold', fontsize=12)
ax3.legend(loc='upper left', fontsize=9)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=0)
ax3.grid(True, alpha=0.3, axis='y')

# ===== PLOT 4: Histogram - Citations Distribution =====
ax4 = plt.subplot(3, 3, 4)
ax4.hist(df['Citations Per Paper'], bins=8, color='#95E1D3', edgecolor='black', linewidth=1.5, alpha=0.7)
ax4.set_xlabel('Citations Per Paper', fontweight='bold')
ax4.set_ylabel('Frequency', fontweight='bold')
ax4.set_title('Citations Distribution', fontweight='bold', fontsize=12)
ax4.grid(True, alpha=0.3, axis='y')

# ===== PLOT 5: Pie Chart - Universities by Location =====
ax5 = plt.subplot(3, 3, 5)
location_counts = df['Campus Location'].value_counts()
colors_pie = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#95E1D3', '#A8E6CF']
wedges, texts, autotexts = ax5.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%',
                                     colors=colors_pie, startangle=90, textprops={'fontweight': 'bold'})
ax5.set_title('Universities by City', fontweight='bold', fontsize=12)

# ===== PLOT 6: Line Chart - Employer Reputation Trend =====
ax6 = plt.subplot(3, 3, 6)
employer_sorted = df.sort_values('Employer Reputation', ascending=False).head(10)
ax6.plot(range(len(employer_sorted)), employer_sorted['Employer Reputation'],
         marker='o', linewidth=2.5, markersize=8, color='#FF6B6B')
ax6.fill_between(range(len(employer_sorted)), employer_sorted['Employer Reputation'], alpha=0.3, color='#FF6B6B')
ax6.set_xlabel('University Rank', fontweight='bold')
ax6.set_ylabel('Employer Reputation Score', fontweight='bold')
ax6.set_title('Top 10 - Employer Reputation Trend', fontweight='bold', fontsize=12)
ax6.grid(True, alpha=0.3)
ax6.set_xticks(range(len(employer_sorted)))
ax6.set_xticklabels(range(1, len(employer_sorted) + 1))

# ===== PLOT 7: Box Plot - Cost by Institution Type =====
ax7 = plt.subplot(3, 3, 7)
public_cost = df[df['Institution Type'] == 'Public']['Annual Academic Cost (PKR)'].dropna()
private_cost = df[df['Institution Type'] == 'Private']['Annual Academic Cost (PKR)'].dropna()
bp = ax7.boxplot([public_cost, private_cost], tick_labels=['Public', 'Private'], patch_artist=True)
for patch, color in zip(bp['boxes'], ['#4ECDC4', '#FF6B6B']):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
ax7.set_ylabel('Annual Cost (PKR)', fontweight='bold')
ax7.set_title('Cost Distribution - Box Plot', fontweight='bold', fontsize=12)
ax7.grid(True, alpha=0.3, axis='y')

# ===== PLOT 8: Correlation Heatmap (Numeric columns) =====
ax8 = plt.subplot(3, 3, 8)
numeric_cols = ['Citations Per Paper', 'Academic Reputation', 'International Research Network', 'Employer Reputation']
corr_matrix = df[numeric_cols].corr()
im = ax8.imshow(corr_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
ax8.set_xticks(range(len(numeric_cols)))
ax8.set_yticks(range(len(numeric_cols)))
ax8.set_xticklabels([col[:15] for col in numeric_cols], rotation=45, ha='right', fontsize=9)
ax8.set_yticklabels([col[:15] for col in numeric_cols], fontsize=9)
ax8.set_title('Correlation Matrix', fontweight='bold', fontsize=12)
# Add correlation values
for i in range(len(numeric_cols)):
    for j in range(len(numeric_cols)):
        text = ax8.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                       ha="center", va="center", color="black", fontsize=9, fontweight='bold')
plt.colorbar(im, ax=ax8, label='Correlation')

# ===== PLOT 9: Multi-metric Comparison (Radar-style using scatter) =====
ax9 = plt.subplot(3, 3, 9)
metrics_normalized = df[['Academic Reputation', 'Citations Per Paper', 'Employer Reputation']].copy()
metrics_normalized = (metrics_normalized - metrics_normalized.min()) / (metrics_normalized.max() - metrics_normalized.min())
ax9.scatter(metrics_normalized['Academic Reputation'],
           metrics_normalized['Employer Reputation'],
           s=metrics_normalized['Citations Per Paper']*300,
           alpha=0.6, c=range(len(df)), cmap='viridis', edgecolors='black', linewidth=1)
ax9.set_xlabel('Academic Reputation (Normalized)', fontweight='bold')
ax9.set_ylabel('Employer Reputation (Normalized)', fontweight='bold')
ax9.set_title('Multi-Metric Comparison\n(Size = Citations)', fontweight='bold', fontsize=12)
ax9.grid(True, alpha=0.3)

# Adjust layout
plt.tight_layout()

# Save the dashboard
plt.savefig(r'C:\Users\uk248\PakIT_Dashboard.png', dpi=300, bbox_inches='tight')
print("Dashboard saved as 'PakIT_Dashboard.png'")

# Display
plt.show()
