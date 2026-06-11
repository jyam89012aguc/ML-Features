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

def _am_accrual(ncfo, rev, w): return (rev - ncfo).rolling(w).mean()

def f46_accounting_manipulation_revenue_base_w34_v076_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 76. This monitors 34-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w35_v077_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 77. This monitors 35-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w36_v078_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 78. This monitors 36-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w37_v079_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 79. This monitors 37-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w38_v080_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 80. This monitors 38-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w39_v081_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 81. This monitors 39-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w40_v082_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 82. This monitors 40-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w41_v083_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 83. This monitors 41-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w42_v084_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 84. This monitors 42-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w43_v085_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 85. This monitors 43-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w44_v086_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 86. This monitors 44-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w45_v087_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 87. This monitors 45-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 45)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w46_v088_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 88. This monitors 46-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 46)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w47_v089_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 89. This monitors 47-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 47)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w48_v090_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 90. This monitors 48-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 48)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w49_v091_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 91. This monitors 49-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 49)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w50_v092_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 92. This monitors 50-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 50)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w51_v093_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 93. This monitors 51-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 51)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w52_v094_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 94. This monitors 52-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 52)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w53_v095_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 95. This monitors 53-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 53)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w54_v096_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 96. This monitors 54-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 54)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w55_v097_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 97. This monitors 55-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 55)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w56_v098_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 98. This monitors 56-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 56)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w57_v099_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 99. This monitors 57-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 57)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w58_v100_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 100. This monitors 58-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 58)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w59_v101_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 101. This monitors 59-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 59)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w60_v102_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 102. This monitors 60-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 60)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w61_v103_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 103. This monitors 61-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 61)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w62_v104_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 104. This monitors 62-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 62)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w63_v105_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 105. This monitors 63-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w64_v106_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 106. This monitors 64-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 64)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w65_v107_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 107. This monitors 65-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 65)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w66_v108_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 108. This monitors 66-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 66)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w67_v109_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 109. This monitors 67-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 67)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w68_v110_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 110. This monitors 68-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 68)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w69_v111_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 111. This monitors 69-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 69)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w70_v112_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 112. This monitors 70-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 70)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w71_v113_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 113. This monitors 71-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 71)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w72_v114_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 114. This monitors 72-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 72)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w73_v115_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 115. This monitors 73-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 73)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w74_v116_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 116. This monitors 74-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 74)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w75_v117_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 117. This monitors 75-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 75)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w76_v118_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 118. This monitors 76-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 76)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w77_v119_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 119. This monitors 77-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 77)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w78_v120_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 120. This monitors 78-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 78)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w79_v121_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 121. This monitors 79-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 79)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w80_v122_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 122. This monitors 80-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 80)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w81_v123_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 123. This monitors 81-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 81)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w82_v124_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 124. This monitors 82-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 82)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w83_v125_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 125. This monitors 83-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 83)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w21_v126_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 126. This monitors 21-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w22_v127_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 127. This monitors 22-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 22)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w23_v128_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 128. This monitors 23-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 23)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w24_v129_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 129. This monitors 24-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 24)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w25_v130_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 130. This monitors 25-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 25)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w26_v131_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 131. This monitors 26-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 26)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w27_v132_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 132. This monitors 27-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 27)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w28_v133_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 133. This monitors 28-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 28)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w29_v134_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 134. This monitors 29-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 29)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w30_v135_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 135. This monitors 30-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 30)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w31_v136_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 136. This monitors 31-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 31)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w32_v137_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 137. This monitors 32-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 32)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w33_v138_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 138. This monitors 33-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 33)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w34_v139_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 139. This monitors 34-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 34)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w35_v140_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 140. This monitors 35-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 35)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w36_v141_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 141. This monitors 36-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 36)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w37_v142_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 142. This monitors 37-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 37)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w38_v143_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 143. This monitors 38-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 38)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w39_v144_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 144. This monitors 39-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 39)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w40_v145_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 145. This monitors 40-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 40)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w41_v146_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 146. This monitors 41-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 41)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w42_v147_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 147. This monitors 42-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_revenue_base_w43_v148_signal(revenue) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: revenue, Variation: 148. This monitors 43-period trends."""
    res = _am_accrual(ncfo if 'revenue' != 'ncfo' else revenue, revenue, 43)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_ncfo_base_w44_v149_signal(ncfo) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: ncfo, Variation: 149. This monitors 44-period trends."""
    res = _am_accrual(ncfo if 'ncfo' != 'ncfo' else revenue, ncfo, 44)
    return res.replace([np.inf, -np.inf], np.nan)

def f46_accounting_manipulation_assets_base_w45_v150_signal(assets) -> pd.Series:
    """Base feature for f46_accounting_manipulation. Input: assets, Variation: 150. This monitors 45-period trends."""
    res = _am_accrual(ncfo if 'assets' != 'ncfo' else revenue, assets, 45)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "assets": np.random.normal(1000, 100, n).cumsum() + 1000,
        "revenue": np.random.normal(1000, 100, n).cumsum() + 1000,
        "ncfo": np.random.normal(1000, 100, n).cumsum() + 1000
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f46_accounting_manipulation_"))]
    
    print(f"Testing {len(funcs)} functions for f46_accounting_manipulation...")
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

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f46_accounting_manipulation_"))]}
F46_ACCOUNTING_MANIPULATION_REGISTRY_BASE_076_150 = REGISTRY
