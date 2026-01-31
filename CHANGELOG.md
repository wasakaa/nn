# Changelog

All notable changes to NWF Stock Screener will be documented here.

## [2.0.0] - 2026-01-31

### Added
- 🎯 **NWF Composite Score** (6-signal weighted system)
- 🛡️ **Confidence Calculation** (Walk-Forward validation proxy)
- ⭐ **Robust Score** (True edge = Score × Confidence)
- 💧 **Liquidity Score** (4-10 scale for execution safety)
- 🎨 **Modern Web UI** with gradient design
- 🔍 **Real-time Filtering** by exchange, score, confidence, liquidity
- 📊 **Live Stats Dashboard** (total stocks, avg metrics)
- 🔢 **Sortable Columns** (click headers to sort)
- 🔎 **Ticker Search** (instant filter)
- 📖 **Full Documentation** (algorithm + usage)

### Changed
- Migrated from simple AI scoring to multi-signal NWF algorithm
- Enhanced data structure with 4 new metrics
- Improved UI/UX with responsive design

### Technical Details
- 654 stocks across HOSE, HNX, UPCOM
- 5-layer validation pipeline
- Anti-overfitting measures implemented
- Mobile-responsive layout

---

## [1.0.0] - 2026-01-20

### Initial Release
- Basic stock screener with AI ensemble signals
- Simple filtering by exchange and liquidity
- CSV data export
- 600+ stocks coverage

---

## Future Releases

### [3.0.0] - Planned
- Real Walk-Forward testing (3-year split)
- Monte Carlo simulation per stock
- Regime detection (Bull/Bear/Sideway)
- Portfolio optimization
- API integration for live data
- Backtesting module
- Alert system (email/telegram)
