import pandas as pd
import numpy as np

def _sma(s, w):
    """Simple Moving Average with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()

def _std(s, w):
    """Standard Deviation with min_periods handling."""
    return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()

def _z(s, w):
    """Z-score calculation."""
    return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _ol_leverage(s, w): return s.pct_change(w)

def f40_operating_leverage_composite_opinc_base_w34_v076_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 76. This monitors 34-period trends."""
    res = _ol_leverage(opinc, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w35_v077_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 77. This monitors 35-period trends."""
    res = _ol_leverage(sga, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w36_v078_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 78. This monitors 36-period trends."""
    res = _ol_leverage(revenue, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w37_v079_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 79. This monitors 37-period trends."""
    res = _ol_leverage(opinc, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w38_v080_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 80. This monitors 38-period trends."""
    res = _ol_leverage(sga, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w39_v081_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 81. This monitors 39-period trends."""
    res = _ol_leverage(revenue, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w40_v082_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 82. This monitors 40-period trends."""
    res = _ol_leverage(opinc, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w41_v083_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 83. This monitors 41-period trends."""
    res = _ol_leverage(sga, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w42_v084_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 84. This monitors 42-period trends."""
    res = _ol_leverage(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w43_v085_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 85. This monitors 43-period trends."""
    res = _ol_leverage(opinc, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w44_v086_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 86. This monitors 44-period trends."""
    res = _ol_leverage(sga, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w45_v087_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 87. This monitors 45-period trends."""
    res = _ol_leverage(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w46_v088_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 88. This monitors 46-period trends."""
    res = _ol_leverage(opinc, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w47_v089_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 89. This monitors 47-period trends."""
    res = _ol_leverage(sga, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w48_v090_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 90. This monitors 48-period trends."""
    res = _ol_leverage(revenue, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w49_v091_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 91. This monitors 49-period trends."""
    res = _ol_leverage(opinc, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w50_v092_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 92. This monitors 50-period trends."""
    res = _ol_leverage(sga, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w51_v093_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 93. This monitors 51-period trends."""
    res = _ol_leverage(revenue, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w52_v094_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 94. This monitors 52-period trends."""
    res = _ol_leverage(opinc, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w53_v095_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 95. This monitors 53-period trends."""
    res = _ol_leverage(sga, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w54_v096_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 96. This monitors 54-period trends."""
    res = _ol_leverage(revenue, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w55_v097_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 97. This monitors 55-period trends."""
    res = _ol_leverage(opinc, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w56_v098_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 98. This monitors 56-period trends."""
    res = _ol_leverage(sga, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w57_v099_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 99. This monitors 57-period trends."""
    res = _ol_leverage(revenue, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w58_v100_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 100. This monitors 58-period trends."""
    res = _ol_leverage(opinc, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w59_v101_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 101. This monitors 59-period trends."""
    res = _ol_leverage(sga, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w60_v102_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 102. This monitors 60-period trends."""
    res = _ol_leverage(revenue, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w61_v103_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 103. This monitors 61-period trends."""
    res = _ol_leverage(opinc, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w62_v104_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 104. This monitors 62-period trends."""
    res = _ol_leverage(sga, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w63_v105_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 105. This monitors 63-period trends."""
    res = _ol_leverage(revenue, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w64_v106_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 106. This monitors 64-period trends."""
    res = _ol_leverage(opinc, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w65_v107_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 107. This monitors 65-period trends."""
    res = _ol_leverage(sga, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w66_v108_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 108. This monitors 66-period trends."""
    res = _ol_leverage(revenue, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w67_v109_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 109. This monitors 67-period trends."""
    res = _ol_leverage(opinc, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w68_v110_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 110. This monitors 68-period trends."""
    res = _ol_leverage(sga, 68)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w69_v111_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 111. This monitors 69-period trends."""
    res = _ol_leverage(revenue, 69)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w70_v112_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 112. This monitors 70-period trends."""
    res = _ol_leverage(opinc, 70)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w71_v113_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 113. This monitors 71-period trends."""
    res = _ol_leverage(sga, 71)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w72_v114_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 114. This monitors 72-period trends."""
    res = _ol_leverage(revenue, 72)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w73_v115_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 115. This monitors 73-period trends."""
    res = _ol_leverage(opinc, 73)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w74_v116_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 116. This monitors 74-period trends."""
    res = _ol_leverage(sga, 74)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w75_v117_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 117. This monitors 75-period trends."""
    res = _ol_leverage(revenue, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w76_v118_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 118. This monitors 76-period trends."""
    res = _ol_leverage(opinc, 76)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w77_v119_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 119. This monitors 77-period trends."""
    res = _ol_leverage(sga, 77)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w78_v120_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 120. This monitors 78-period trends."""
    res = _ol_leverage(revenue, 78)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w79_v121_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 121. This monitors 79-period trends."""
    res = _ol_leverage(opinc, 79)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w80_v122_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 122. This monitors 80-period trends."""
    res = _ol_leverage(sga, 80)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w81_v123_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 123. This monitors 81-period trends."""
    res = _ol_leverage(revenue, 81)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w82_v124_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 124. This monitors 82-period trends."""
    res = _ol_leverage(opinc, 82)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w83_v125_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 125. This monitors 83-period trends."""
    res = _ol_leverage(sga, 83)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w21_v126_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 126. This monitors 21-period trends."""
    res = _ol_leverage(revenue, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w22_v127_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 127. This monitors 22-period trends."""
    res = _ol_leverage(opinc, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w23_v128_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 128. This monitors 23-period trends."""
    res = _ol_leverage(sga, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w24_v129_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 129. This monitors 24-period trends."""
    res = _ol_leverage(revenue, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w25_v130_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 130. This monitors 25-period trends."""
    res = _ol_leverage(opinc, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w26_v131_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 131. This monitors 26-period trends."""
    res = _ol_leverage(sga, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w27_v132_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 132. This monitors 27-period trends."""
    res = _ol_leverage(revenue, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w28_v133_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 133. This monitors 28-period trends."""
    res = _ol_leverage(opinc, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w29_v134_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 134. This monitors 29-period trends."""
    res = _ol_leverage(sga, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w30_v135_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 135. This monitors 30-period trends."""
    res = _ol_leverage(revenue, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w31_v136_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 136. This monitors 31-period trends."""
    res = _ol_leverage(opinc, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w32_v137_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 137. This monitors 32-period trends."""
    res = _ol_leverage(sga, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w33_v138_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 138. This monitors 33-period trends."""
    res = _ol_leverage(revenue, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w34_v139_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 139. This monitors 34-period trends."""
    res = _ol_leverage(opinc, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w35_v140_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 140. This monitors 35-period trends."""
    res = _ol_leverage(sga, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w36_v141_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 141. This monitors 36-period trends."""
    res = _ol_leverage(revenue, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w37_v142_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 142. This monitors 37-period trends."""
    res = _ol_leverage(opinc, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w38_v143_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 143. This monitors 38-period trends."""
    res = _ol_leverage(sga, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w39_v144_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 144. This monitors 39-period trends."""
    res = _ol_leverage(revenue, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w40_v145_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 145. This monitors 40-period trends."""
    res = _ol_leverage(opinc, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w41_v146_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 146. This monitors 41-period trends."""
    res = _ol_leverage(sga, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w42_v147_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 147. This monitors 42-period trends."""
    res = _ol_leverage(revenue, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_opinc_base_w43_v148_signal(opinc) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: opinc, Variation: 148. This monitors 43-period trends."""
    res = _ol_leverage(opinc, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_sga_base_w44_v149_signal(sga) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: sga, Variation: 149. This monitors 44-period trends."""
    res = _ol_leverage(sga, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f40_operating_leverage_composite_revenue_base_w45_v150_signal(revenue) -> pd.Series:
    """Base feature for f40_operating_leverage_composite. Input: revenue, Variation: 150. This monitors 45-period trends."""
    res = _ol_leverage(revenue, 45)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000,
        "opinc": np.random.normal(1000, 100, n).cumsum() + 1000,
        "sga": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f40_operating_leverage_composite_"))]
    
    print(f"Testing {len(funcs)} functions for f40_operating_leverage_composite...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        if len(q) == 0:
            continue
        assert q.nunique() > 10, f"{func.__name__} has too few unique values: {q.nunique()}"

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f40_operating_leverage_composite_"))]}
F40_OPERATING_LEVERAGE_COMPOSITE_REGISTRY_BASE_076_150 = REGISTRY
