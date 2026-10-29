# Finance & Economics

Economics → corporate finance → markets → derivatives → quant → risk → microstructure → systematic trading → research.
You already trade (VoidCodex, MT5). This track turns that intuition into rigour — and keeps testing it against
**your own data**, because the most valuable lesson in finance is how easily you fool yourself.

**How to use this file.** Strictly top to bottom; `today` shows the first unticked session. The quant modules lean on
maths (probability M16, stochastic calculus M26, optimisation M22). **Levels:** F · S · U · G · R (see `CURRICULUM.md`).

## E01 · Microeconomics
<!-- rung: F | prereq: none | feeds: everything in this track -->
**Goal:** Think like an economist — incentives, trade-offs, markets and when they fail.
**Resources:**
- [OpenStax — Principles of Economics](https://openstax.org/subjects/social-sciences) — free textbook
- [Marginal Revolution University](https://mru.org) — short free videos
- [MIT 14.01 Principles of Microeconomics](https://ocw.mit.edu/courses/14-01-principles-of-microeconomics-fall-2018/)
**Sessions:**
- [ ] E01.S01 — Placement and the economic way of thinking: scarcity, opportunity cost, incentives ([MRU](https://mru.org) intro videos).
- [ ] E01.S02 — Supply and demand; equilibrium; shifts vs movements along a curve.
- [ ] E01.S03 — Elasticity; taxes and subsidies; price controls.
- [ ] E01.S04 — Consumer choice and producer theory; costs.
- [ ] E01.S05 — Market structures: perfect competition, monopoly, oligopoly.
- [ ] E01.S06 — Game theory basics: Nash equilibrium, the prisoner's dilemma.
- [ ] E01.S07 — Market failure: externalities, public goods, information asymmetry.
- [ ] E01.S08 — Essay: model a real market (a currency pair or a commodity) with supply and demand — and state where the model breaks.
**Gate artifact:** the market-modelling essay.
**Anki seeds:** elasticity formula · deadweight loss · market structures · Nash equilibrium definition

## E02 · Macroeconomics & Central Banking
<!-- rung: F | prereq: E01 | feeds: E04, macro-driven trading -->
**Goal:** Understand the forces that move whole markets — growth, inflation, money, interest rates, central banks.
**Resources:**
- [OpenStax — Principles of Economics](https://openstax.org/subjects/social-sciences) — the macro chapters
- [Marginal Revolution University](https://mru.org) — Principles of Macroeconomics
- [Bank of England — Knowledge Bank](https://www.bankofengland.co.uk/knowledgebank)
**Sessions:**
- [ ] E02.S01 — GDP and growth, and how they're measured.
- [ ] E02.S02 — Inflation and unemployment; the Phillips curve.
- [ ] E02.S03 — Money and banking; how banks create money.
- [ ] E02.S04 — Monetary policy: central banks, interest rates, QE — the Fed, ECB and BoE.
- [ ] E02.S05 — Fiscal policy and public debt.
- [ ] E02.S06 — Exchange rates, trade and the balance of payments.
- [ ] E02.S07 — Essay: how a rate decision transmits to FX and indices — checked against a real Fed day in your data.
**Gate artifact:** the transmission essay, tested against your own data.

## E03 · Accounting & Corporate Finance
<!-- rung: U | prereq: E01 | feeds: E04, valuation -->
**Goal:** Read a company's financial statements and value it from first principles.
**Resources:**
- [OpenStax — Principles of Accounting](https://openstax.org/subjects/business) — free
- [Aswath Damodaran's valuation classes](https://pages.stern.nyu.edu/~adamodar/) — free lectures and spreadsheets
**Sessions:**
- [ ] E03.S01 — The three statements: income statement, balance sheet, cash-flow statement.
- [ ] E03.S02 — Ratios: profitability, liquidity, leverage, efficiency.
- [ ] E03.S03 — The time value of money: PV, FV, annuities, perpetuities.
- [ ] E03.S04 — The cost of capital; WACC; a first look at CAPM.
- [ ] E03.S05 — Discounted cash-flow valuation (Damodaran).
- [ ] E03.S06 — Relative valuation and multiples.
- [ ] E03.S07 — Build: value a real listed company — a DCF with every assumption written down.
**Gate artifact:** the DCF valuation with an assumptions page and a sensitivity table.

## E04 · Financial Markets & Portfolio Theory
<!-- rung: U | prereq: E02, E03, math M16 | feeds: E06, E09 -->
**Goal:** What markets are for, how risk and return relate, and how to build a portfolio — and why that's fragile.
**Resources:**
- [Yale ECON 252 Financial Markets — Robert Shiller](https://oyc.yale.edu/economics/econ-252) — free
- [MIT 15.401 Finance Theory I](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/)
**Sessions:**
- [ ] E04.S01 — Markets and institutions: what financial markets are for (Shiller).
- [ ] E04.S02 — Risk and return; diversification; the efficient-markets hypothesis.
- [ ] E04.S03 — Bonds: pricing, yields, duration, convexity.
- [ ] E04.S04 — Stocks; the dividend discount model.
- [ ] E04.S05 — Mean–variance optimisation and the efficient frontier.
- [ ] E04.S06 — CAPM and factor models (Fama–French).
- [ ] E04.S07 — Build: a portfolio optimiser in Python with an efficient-frontier plot (uses math M22).
**Gate artifact:** the optimiser + a note on why its outputs are fragile (estimation error).

## E05 · Behavioural Finance & Decision-Making
<!-- rung: U | prereq: E04 | feeds: your own trading, E11 -->
**Goal:** Find the biases in your own decisions — with evidence from your journal — and build habits that counter them.
**Resources:**
- [Yale ECON 159 Game Theory — Ben Polak](https://oyc.yale.edu/economics/econ-159) — free
- Shiller's ECON 252 lectures on behavioural finance
- Kahneman — *Thinking, Fast and Slow* (paid)
**Sessions:**
- [ ] E05.S01 — Heuristics and biases; prospect theory.
- [ ] E05.S02 — Overconfidence, loss aversion, the disposition effect — find each one in your trading journal.
- [ ] E05.S03 — Game theory deeper: repeated games, signalling, auctions.
- [ ] E05.S04 — Decision journals and pre-mortems for trading — start one.
**Gate artifact:** an essay auditing your own trading for biases, with evidence from your journal.

## E06 · Derivatives
<!-- rung: U | prereq: E04, math M16 | feeds: E08, E09 -->
**Goal:** Forwards, futures, swaps and options — pricing by no-arbitrage, the Greeks, and hedging.
**Resources:**
- [CME Group education](https://www.cmegroup.com/education.html) — free
- [MIT 18.S096](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/)
- Hull — *Options, Futures and Other Derivatives* (paid — the standard)
**Sessions:**
- [ ] E06.S01 — Forwards and futures; pricing by no-arbitrage; margining.
- [ ] E06.S02 — Swaps: interest-rate and currency.
- [ ] E06.S03 — Options: payoffs, strategies, put–call parity.
- [ ] E06.S04 — The binomial model; risk-neutral valuation.
- [ ] E06.S05 — Black–Scholes: the formula and its assumptions (the derivation comes in E08).
- [ ] E06.S06 — The Greeks; delta hedging — simulate a hedged position.
- [ ] E06.S07 — Volatility: implied vs realised; the smile.
- [ ] E06.S08 — Build: price an option three ways — binomial tree, Black–Scholes, Monte Carlo — and compute the Greeks.
**Gate artifact:** the three-way pricer with convergence plots.
**Anki seeds:** put–call parity · option payoff shapes · each Greek's meaning · Black–Scholes inputs

## E07 · Econometrics & Financial Time Series
<!-- rung: U | prereq: math M20, E04 | feeds: E11, ai-ml A12 -->
**Goal:** Statistics for economic and market data — regression done right, stationarity, ARIMA, GARCH, cointegration.
**Resources:**
- [Forecasting: Principles and Practice](https://otexts.com/fpp3/) — free
- Ben Lambert's econometrics lectures (YouTube, free)
- Wooldridge — *Introductory Econometrics* (paid)
**Sessions:**
- [ ] E07.S01 — Regression revisited: OLS assumptions, heteroskedasticity, robust standard errors.
- [ ] E07.S02 — Endogeneity, instrumental variables, an introduction to panel data.
- [ ] E07.S03 — Stationarity, unit roots, differencing.
- [ ] E07.S04 — ARIMA modelling.
- [ ] E07.S05 — Volatility: ARCH and GARCH — fit them to your instruments.
- [ ] E07.S06 — Cointegration and pairs trading.
**Gate artifact:** a GARCH volatility model on your instruments + a cointegration-test write-up.

## E08 · Quantitative Finance
<!-- rung: G | prereq: math M26, E06 | feeds: E09, E10 -->
**Goal:** Rigorous derivatives pricing — risk-neutral measures, martingale pricing, PDE and Monte Carlo methods, rate models.
**Resources:**
- math M26 (stochastic calculus)
- [MIT 18.S096](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/)
- Shreve — *Stochastic Calculus for Finance I & II* (paid)
**Sessions:**
- [ ] E08.S01 — Shreve I: the binomial asset-pricing model, rigorously.
- [ ] E08.S02 — The risk-neutral measure; martingale pricing.
- [ ] E08.S03 — Black–Scholes derived, by hedging and by risk-neutral expectation (from math M26).
- [ ] E08.S04 — Exotic options: barriers, Asians, lookbacks — Monte Carlo pricing.
- [ ] E08.S05 — American options: early exercise; finite-difference PDE methods.
- [ ] E08.S06 — Interest-rate models: Vasicek, CIR; an introduction to HJM.
- [ ] E08.S07 — Build: a pricing library (Monte Carlo + finite differences) tested against closed forms.
**Gate artifact:** the pricing library.

## E09 · Risk Management
<!-- rung: G | prereq: E06, E07 | feeds: your own risk rules -->
**Goal:** Measure and manage risk — VaR, Expected Shortfall, stress tests, position sizing — on your own book.
**Resources:**
- [Bank for International Settlements — Basel framework](https://www.bis.org/basel_framework/)
- Hull — *Risk Management and Financial Institutions* (paid)
**Sessions:**
- [ ] E09.S01 — Types of risk: market, credit, liquidity, operational.
- [ ] E09.S02 — Value-at-Risk: historical, parametric, Monte Carlo.
- [ ] E09.S03 — Expected Shortfall, and why regulators moved to it.
- [ ] E09.S04 — Backtesting VaR (the Kupiec test).
- [ ] E09.S05 — Stress testing and scenario analysis.
- [ ] E09.S06 — Position sizing and risk of ruin — applied to your own trading rules.
**Gate artifact:** a risk report (VaR and ES with a backtest) on your own book.

## E10 · Market Microstructure & Trading Systems
<!-- rung: G | prereq: E06, systems S15, programming G10 | feeds: E11, low-latency careers -->
**Goal:** How trading actually happens — order books, liquidity, market making, execution, latency.
**Resources:**
- Almgren & Chriss — "Optimal Execution of Portfolio Transactions" (2000, free online)
- Harris — *Trading and Exchanges* (paid)
- Cartea, Jaimungal, Penalva — *Algorithmic and High-Frequency Trading* (paid)
**Sessions:**
- [ ] E10.S01 — Market structure: exchanges, order types, the limit order book.
- [ ] E10.S02 — Liquidity, spreads and market impact.
- [ ] E10.S03 — Market making: inventory risk and quoting.
- [ ] E10.S04 — Optimal execution: TWAP, VWAP, Almgren–Chriss.
- [ ] E10.S05 — Latency and HFT: why microseconds matter (links to systems S15).
- [ ] E10.S06 — Build: a limit-order-book simulator + a simple market-making strategy (reuse programming G10's order book).
**Gate artifact:** the simulator, with a P&L and inventory analysis of your market maker.

## E11 · Systematic Trading, Done Honestly
<!-- rung: G | prereq: E07, E09, ai-ml A12 | feeds: your edge, if it's real -->
**Goal:** Backtest your own strategy the way a sceptical quant would — and find out whether the edge is real.
**Resources:**
- Bailey & López de Prado — "The Deflated Sharpe Ratio" (free paper)
- López de Prado — *Advances in Financial Machine Learning* (paid)
- your VoidCodex research and data
**Sessions:**
- [ ] E11.S01 — Backtesting pitfalls: look-ahead bias, survivorship, data snooping, costs.
- [ ] E11.S02 — Walk-forward analysis and out-of-sample discipline.
- [ ] E11.S03 — The deflated Sharpe ratio and the probability of backtest overfitting.
- [ ] E11.S04 — Transaction-cost modelling and slippage.
- [ ] E11.S05 — Build: backtest your VoidCodex strategy with all of the above applied.
- [ ] E11.S06 — Write the critique: everything that could still be wrong.
**Gate artifact:** the honest backtest + its self-critique.

## E12 · Research: Quant Papers
<!-- rung: R | prereq: E11 | feeds: your niche -->
**Goal:** Ask a real research question about markets, answer it with data, and write it up.
**Resources:**
- [SSRN](https://www.ssrn.com) and [arXiv q-fin](https://arxiv.org/archive/q-fin)
**Sessions:**
- [ ] E12.S01 — Pick a question (a microstructure effect or a factor); read five papers on it.
- [ ] E12.S02 — Replicate a published result with your own data.
- [ ] E12.S03 — Extend it, and write it up.
**Gate artifact:** a replication + extension note.
