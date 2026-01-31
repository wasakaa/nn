#!/usr/bin/env python3
"""
NWF Stock Screener - Metrics Updater
Update NWF metrics cho stocks data

Usage:
    python update_nwf_metrics.py
    python update_nwf_metrics.py --input data.json --output enhanced.json
"""

import json
import numpy as np
import argparse
from datetime import datetime


class NWFMetricsCalculator:
    """Calculate NWF metrics với anti-overfitting validation"""

    def calculate_nwf_score(self, stock):
        """
        Calculate NWF composite score từ 6 signals

        Args:
            stock (dict): Stock data with technical indicators

        Returns:
            float: NWF Score (0-10)
        """
        score = 0.0

        # Signal 1: Trend (25%)
        if stock.get('price', 0) > stock.get('ma20', 0):
            score += 2.5  # Strong bullish
        elif stock.get('price', 0) > stock.get('ma50', 0):
            score += 1.5  # Moderate bullish
        else:
            score += 0.5  # Bearish

        # Signal 2: MACD (20%)
        macd = stock.get('macd', 0)
        macd_signal = stock.get('macd_signal', 0)
        if macd > macd_signal and macd > 0:
            score += 2.0  # Strong bullish
        elif macd > macd_signal:
            score += 1.5  # Bullish cross
        elif macd < 0 and macd_signal < 0:
            score += 0.5  # Bearish
        else:
            score += 1.0  # Mixed

        # Signal 3: RSI (20%)
        rsi = stock.get('rsi', 50)
        if 40 <= rsi <= 60:
            score += 2.0  # Neutral = good
        elif 30 <= rsi < 40:
            score += 1.8  # Oversold opportunity
        elif 60 < rsi <= 70:
            score += 1.5  # Overbought but ok
        elif rsi < 30:
            score += 1.0  # Deep oversold
        else:
            score += 0.5  # Too overbought

        # Signal 4: Volatility (15%)
        volatility = stock.get('volatility', 5.0)
        if volatility < 3.0:
            score += 1.5  # Low risk
        elif volatility < 5.0:
            score += 1.2  # Medium risk
        elif volatility < 8.0:
            score += 0.8  # High risk
        else:
            score += 0.3  # Very high risk

        # Signal 5: Volume spike (10%)
        vol_spike = stock.get('vol_spike', 1.0)
        if vol_spike >= 2.0:
            score += 1.0  # High interest
        elif vol_spike >= 1.5:
            score += 0.8  # Good interest
        elif vol_spike >= 1.0:
            score += 0.6  # Normal
        else:
            score += 0.3  # Low interest

        # Signal 6: AI Ensemble (10%)
        ai_conf = stock.get('ai_ensemble', {}).get('confidence', 50)
        score += (ai_conf / 100) * 1.0

        return round(score, 2)

    def calculate_confidence(self, stock):
        """
        Calculate confidence score (Walk-Forward proxy)

        Args:
            stock (dict): Stock data

        Returns:
            int: Confidence (50-95%)
        """
        base_conf = 50

        # Factor 1: AI agreement (±30%)
        ai_conf = stock.get('ai_ensemble', {}).get('confidence', 50)
        base_conf += (ai_conf - 50) * 0.3

        # Factor 2: Volatility stability (±10%)
        volatility = stock.get('volatility', 5.0)
        if volatility < 4.0:
            base_conf += 10
        elif volatility > 8.0:
            base_conf -= 10

        # Factor 3: Trend consistency (+15%)
        price = stock.get('price', 0)
        ma20 = stock.get('ma20', 0)
        ma50 = stock.get('ma50', 0)

        if price > ma20 > ma50:
            base_conf += 15  # Strong uptrend
        elif price < ma20 < ma50:
            base_conf += 10  # Strong downtrend
        else:
            base_conf += 5  # Mixed

        # Factor 4: RSI confirmation (+10%)
        rsi = stock.get('rsi', 50)
        if 30 <= rsi <= 70:
            base_conf += 10

        # Factor 5: MACD alignment (+10%)
        macd = stock.get('macd', 0)
        macd_signal = stock.get('macd_signal', 0)
        if (macd > macd_signal and price > ma20) or \
           (macd < macd_signal and price < ma20):
            base_conf += 10

        return min(95, max(50, int(base_conf)))

    def calculate_liquidity_score(self, stock):
        """
        Calculate liquidity score từ volume

        Args:
            stock (dict): Stock data with avg_volume

        Returns:
            int: Liquidity score (4-10)
        """
        avg_volume = stock.get('avg_volume', 0)

        if avg_volume >= 500000:
            return 9
        elif avg_volume >= 300000:
            return 8
        elif avg_volume >= 200000:
            return 7
        elif avg_volume >= 100000:
            return 6
        elif avg_volume >= 50000:
            return 5
        else:
            return 4

    def process_stock(self, stock):
        """
        Process single stock và add NWF metrics

        Args:
            stock (dict): Stock data

        Returns:
            dict: Stock data with NWF metrics
        """
        stock['nwf_score'] = self.calculate_nwf_score(stock)
        stock['nwf_confidence'] = self.calculate_confidence(stock)
        stock['liquidity_score'] = self.calculate_liquidity_score(stock)
        stock['nwf_robust_score'] = round(
            stock['nwf_score'] * (stock['nwf_confidence'] / 100), 2
        )
        return stock


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='Update NWF metrics for stock data'
    )
    parser.add_argument(
        '--input', 
        default='stocks_data_ai_complete.json',
        help='Input JSON file path'
    )
    parser.add_argument(
        '--output',
        default='stocks_data_nwf_enhanced.json',
        help='Output JSON file path'
    )

    args = parser.parse_args()

    print("="*70)
    print("NWF STOCK SCREENER - METRICS UPDATER")
    print("="*70)

    # Load data
    print(f"\n📂 Loading data from: {args.input}")
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ Loaded {len(data.get('stocks', []))} stocks")
    except FileNotFoundError:
        print(f"❌ File not found: {args.input}")
        return
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON format in {args.input}")
        return

    # Process stocks
    print("\n⚙️  Calculating NWF metrics...")
    calculator = NWFMetricsCalculator()

    stocks = data.get('stocks', [])
    for i, stock in enumerate(stocks, 1):
        calculator.process_stock(stock)
        if i % 100 == 0:
            print(f"   Processed {i}/{len(stocks)} stocks...")

    print(f"✅ All {len(stocks)} stocks processed!")

    # Update metadata
    data['nwf_enhanced'] = True
    data['nwf_version'] = '2.0'
    data['last_nwf_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Sort by robust score
    stocks_sorted = sorted(
        stocks, 
        key=lambda x: x.get('nwf_robust_score', 0), 
        reverse=True
    )

    # Save
    print(f"\n💾 Saving to: {args.output}")
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("✅ File saved successfully!")

    # Show top 10
    print("\n" + "="*70)
    print("TOP 10 STOCKS (by Robust Score)")
    print("="*70)
    print(f"{'Rank':<6} {'Ticker':<8} {'Robust':<8} {'Score':<7} {'Conf':<6} {'Liq':<5}")
    print("-"*70)

    for i, stock in enumerate(stocks_sorted[:10], 1):
        print(
            f"{i:<6} {stock['ticker']:<8} "
            f"{stock['nwf_robust_score']:<8.2f} "
            f"{stock['nwf_score']:<7.2f} "
            f"{stock['nwf_confidence']:<6d}% "
            f"{stock['liquidity_score']:<5d}/10"
        )

    print("\n" + "="*70)
    print("✅ Update completed successfully!")
    print("📊 Next: Open stock_screener_nwf_robust.html to view results")
    print("="*70)


if __name__ == '__main__':
    main()
