# AI & Machine Learning

Classical ML → deep learning from scratch → transformers and LLMs → RL, generative models, MLOps → markets → research.
The rule of this track: **implement it before you import it.** You understand a model when you've built its gradients.

**How to use this file.** Strictly top to bottom; `today` shows the first unticked session. This track leans on the maths
track — linear algebra (M14), multivariable calculus (M15), probability (M16), optimisation (M22). Where a session says
"pair with", do the maths session first if you haven't. **Levels:** F · S · U · G · R (see `CURRICULUM.md`).

## A01 · Python for Data
<!-- rung: F | prereq: programming G01 | feeds: everything in this track -->
**Goal:** Handle real data fluently — NumPy, pandas and plots — starting with your own trading history.
**Resources:**
- [Python Data Science Handbook (Jake VanderPlas)](https://jakevdp.github.io/PythonDataScienceHandbook/) — free
**Sessions:**
- [ ] A01.S01 — Placement & setup: a uv project with Jupyter (or VS Code notebooks); skim the [Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) contents and note what you already know.
- [ ] A01.S02 — NumPy: arrays, broadcasting, vectorisation — time it against plain Python loops.
- [ ] A01.S03 — pandas: Series, DataFrames, indexing, groupby.
- [ ] A01.S04 — pandas time series: resampling, rolling windows — on your own price/trade data.
- [ ] A01.S05 — Visualisation: matplotlib and seaborn.
- [ ] A01.S06 — Build: an exploratory analysis of your trading history.
**Gate artifact:** the exploratory notebook — clean data, six honest charts, three observations, three open questions.

## A02 · ML Intuition & the Maths You Need
<!-- rung: F | prereq: A01, math M09 | feeds: A03 onwards -->
**Goal:** See what a neural network is and how gradient descent learns — before any heavy maths — then connect it to the maths track.
**Resources:**
- [3Blue1Brown — Neural Networks](https://www.3blue1brown.com/?topic=neural-networks)
- [StatQuest](https://statquest.org) — friendly explanations of every ML idea
- [Mathematics for Machine Learning](https://mml-book.github.io) — free book
**Sessions:**
- [ ] A02.S01 — [3Blue1Brown Neural Networks](https://www.3blue1brown.com/?topic=neural-networks) chapters 1–2: what a network is; gradient descent.
- [ ] A02.S02 — 3Blue1Brown chapters 3–4: backpropagation and its calculus.
- [ ] A02.S03 — MML: linear algebra for ML (pair with math M14).
- [ ] A02.S04 — MML: vector calculus and the gradient (pair with math M15).
- [ ] A02.S05 — MML: probability and distributions for ML (pair with math M16).
- [ ] A02.S06 — Build: gradient descent from scratch on a two-parameter problem; animate its path over the loss surface.
**Gate artifact:** the from-scratch gradient-descent animation + an explanation of backpropagation in your own words.

## A03 · Classical Machine Learning
<!-- rung: U | prereq: A02, math M14, M16 | feeds: A12, every applied ML problem -->
**Goal:** The workhorse methods — regression, classification, trees, SVMs, clustering — built from scratch and evaluated honestly.
**Resources:**
- [ISLP — An Introduction to Statistical Learning with Python](https://www.statlearning.com) — free book + labs
- [Stanford CS229](https://cs229.stanford.edu) — lectures for the theory
- [Andrew Ng — Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) — free to audit
**Sessions:**
- [ ] A03.S01 — ISLP ch. 2: what statistical learning is; the bias–variance trade-off.
- [ ] A03.S02 — ISLP ch. 3: linear regression — implement OLS from scratch and compare with scikit-learn.
- [ ] A03.S03 — ISLP ch. 4: classification — logistic regression from scratch.
- [ ] A03.S04 — ISLP ch. 5: resampling — cross-validation and the bootstrap.
- [ ] A03.S05 — ISLP ch. 6: model selection and regularisation (ridge, lasso).
- [ ] A03.S06 — ISLP ch. 7: beyond linearity (splines, GAMs).
- [ ] A03.S07 — ISLP ch. 8: trees, random forests, boosting — a decision tree from scratch.
- [ ] A03.S08 — ISLP ch. 9: support vector machines.
- [ ] A03.S09 — ISLP ch. 12: unsupervised learning — PCA (via your SVD from M14) and k-means from scratch.
- [ ] A03.S10 — Evaluation done honestly: leakage, metrics, calibration.
- [ ] A03.S11 — Kaggle: enter a tabular competition; write up what worked and what didn't.
**Gate artifact:** from-scratch linear/logistic regression, decision tree, k-means and PCA (tested against scikit-learn) + the Kaggle write-up.
**Anki seeds:** bias–variance decomposition · cross-validation procedure · ridge vs lasso · precision/recall/F1 · PCA via SVD

## A04 · Neural Networks from Scratch
<!-- rung: U | prereq: A02, math M15 | feeds: A05–A10 -->
**Goal:** Build an autograd engine and language models by hand, until backpropagation holds no mystery.
**Resources:**
- [Andrej Karpathy — Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)
**Sessions:**
- [ ] A04.S01 — micrograd, part 1: build an autograd engine.
- [ ] A04.S02 — micrograd, part 2: train a tiny MLP with it.
- [ ] A04.S03 — makemore 1: a bigram language model.
- [ ] A04.S04 — makemore 2: an MLP language model.
- [ ] A04.S05 — makemore 3: activations, gradients, BatchNorm.
- [ ] A04.S06 — makemore 4: becoming a backprop ninja (manual backprop).
- [ ] A04.S07 — makemore 5: building a WaveNet.
**Gate artifact:** your micrograd + makemore MLP, with your own notes on every gradient.

## A05 · Transformers & GPT from Scratch
<!-- rung: U | prereq: A04 | feeds: A08, the modern AI world -->
**Goal:** Build and train a GPT yourself — attention, tokenisation, the training loop — and explain every part.
**Resources:**
- [Karpathy — Zero to Hero](https://karpathy.ai/zero-to-hero.html) — "Let's build GPT", "Let's build the GPT tokenizer", "Let's reproduce GPT-2"
- [nanoGPT](https://github.com/karpathy/nanoGPT)
- ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762)
**Sessions:**
- [ ] A05.S01 — Read ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762); draw the architecture yourself.
- [ ] A05.S02 — Let's build GPT, part 1: data, a bigram baseline, self-attention.
- [ ] A05.S03 — Let's build GPT, part 2: multi-head attention, feed-forward, residuals, layer norm.
- [ ] A05.S04 — Train it on a corpus you care about (your trading notes, or a favourite book).
- [ ] A05.S05 — The tokenizer: byte-pair encoding from scratch.
- [ ] A05.S06 — Let's reproduce GPT-2 (124M): the training loop at scale — watch it, run a small version on your GPU.
**Gate artifact:** a small GPT trained on your corpus + a written explainer of attention with your own diagrams.

## A06 · Practical Deep Learning
<!-- rung: U | prereq: A04 | feeds: A08, A11 -->
**Goal:** Get state-of-the-art results quickly with PyTorch — CNNs, transfer learning, NLP — and ship a model people can use.
**Resources:**
- [fast.ai — Practical Deep Learning for Coders](https://course.fast.ai)
- [Dive into Deep Learning](https://d2l.ai) — free, with runnable code
**Sessions:**
- [ ] A06.S01 — fast.ai lessons 1–2: getting started and deployment.
- [ ] A06.S02 — Neural-net foundations; PyTorch fluency (d2l preliminaries).
- [ ] A06.S03 — CNNs: convolutions, pooling, ResNets.
- [ ] A06.S04 — Transfer learning and fine-tuning.
- [ ] A06.S05 — NLP with pretrained transformers (Hugging Face).
- [ ] A06.S06 — Tabular deep learning and collaborative filtering.
- [ ] A06.S07 — Training tricks: learning-rate schedules, mixed precision, augmentation.
- [ ] A06.S08 — Build and deploy a classifier on Hugging Face Spaces.
**Gate artifact:** a deployed model with a model card (data, metrics, limitations).

## A07 · Deep Learning Theory
<!-- rung: G | prereq: A05, math M22, M16 | feeds: research -->
**Goal:** Why deep learning works (when it does) — losses, optimisation, initialisation, generalisation.
**Resources:**
- [Simon Prince — Understanding Deep Learning](https://udlbook.github.io/udlbook/) — free
- [Goodfellow, Bengio, Courville — Deep Learning](https://www.deeplearningbook.org) — free
**Sessions:**
- [ ] A07.S01 — Loss functions from maximum likelihood.
- [ ] A07.S02 — Optimisation: SGD, momentum, Adam — implement and compare them.
- [ ] A07.S03 — Initialisation, normalisation, residual connections — why they work.
- [ ] A07.S04 — Regularisation and generalisation; double descent.
- [ ] A07.S05 — Convolutional and recurrent networks, in theory.
- [ ] A07.S06 — Transformers and graph neural networks, in theory.
- [ ] A07.S07 — Reproduce a theory experiment (e.g. double descent) and write it up.
**Gate artifact:** a reproduced experiment with a short paper-style write-up.

## A08 · LLM Engineering
<!-- rung: G | prereq: A05, A06 | feeds: real-world AI products -->
**Goal:** How modern language models are trained, made efficient, adapted and evaluated — hands-on on your own GPU.
**Resources:**
- [Stanford CS336 — Language Modeling from Scratch](https://cs336.stanford.edu/)
- [Hugging Face Learn](https://huggingface.co/learn)
- your `ai-local/` setup (RTX 4060)
**Sessions:**
- [ ] A08.S01 — Tokenisation and data pipelines at scale.
- [ ] A08.S02 — Pretraining: scaling laws and compute budgets.
- [ ] A08.S03 — Efficient inference: the KV cache, quantisation — measure them on your GPU.
- [ ] A08.S04 — Fine-tuning: LoRA / QLoRA on a small open model.
- [ ] A08.S05 — Alignment overview: RLHF and DPO.
- [ ] A08.S06 — Retrieval-augmented generation done properly (chunking, evaluation).
- [ ] A08.S07 — Evaluation: build an eval set that measures what you actually care about.
**Gate artifact:** a LoRA fine-tune of a small model + an eval report comparing base and tuned.

## A09 · Reinforcement Learning
<!-- rung: G | prereq: A04, math M16 | feeds: A12, decision-making systems -->
**Goal:** Learning from reward — bandits, MDPs, TD learning, policy gradients — from the textbook to a trained agent.
**Resources:**
- [Sutton & Barto — Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html) — free
- [David Silver's RL course](https://www.davidsilver.uk/teaching/)
- [OpenAI Spinning Up](https://spinningup.openai.com)
**Sessions:**
- [ ] A09.S01 — Multi-armed bandits — implement ε-greedy and UCB.
- [ ] A09.S02 — Finite MDPs and the Bellman equations.
- [ ] A09.S03 — Dynamic programming: policy and value iteration.
- [ ] A09.S04 — Monte Carlo methods.
- [ ] A09.S05 — Temporal-difference learning: SARSA and Q-learning.
- [ ] A09.S06 — Function approximation; DQN.
- [ ] A09.S07 — Policy gradients and actor–critic (Spinning Up).
- [ ] A09.S08 — Build: train an agent on a Gymnasium environment; plot its learning curves.
**Gate artifact:** from-scratch Q-learning + a policy-gradient agent with learning curves.

## A10 · Generative Models & Diffusion
<!-- rung: G | prereq: A07, math M26 | feeds: research -->
**Goal:** VAEs, GANs, flows and diffusion — and the stochastic-calculus view that ties diffusion to the maths track.
**Resources:**
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/) — the generative-model chapters
- math M26 (stochastic calculus)
**Sessions:**
- [ ] A10.S01 — Variational autoencoders.
- [ ] A10.S02 — Generative adversarial networks.
- [ ] A10.S03 — Normalising flows.
- [ ] A10.S04 — Diffusion models: the forward and reverse processes.
- [ ] A10.S05 — The SDE view of diffusion (connects to math M26).
- [ ] A10.S06 — Build: a DDPM on MNIST.
**Gate artifact:** a working DDPM + an explainer linking diffusion to stochastic differential equations.

## A11 · MLOps & Serving
<!-- rung: G | prereq: A06, systems S06 | feeds: production ML -->
**Goal:** Get models into production and keep them healthy — testing, serving, monitoring, drift.
**Resources:**
- [Made With ML](https://madewithml.com) — free
- [Full Stack Deep Learning](https://fullstackdeeplearning.com) — free
**Sessions:**
- [ ] A11.S01 — Problem framing, data versioning, experiment tracking.
- [ ] A11.S02 — Testing ML systems: data, model and code.
- [ ] A11.S03 — Serving: batch vs online; latency budgets (ties to systems).
- [ ] A11.S04 — Monitoring: drift, performance decay, alerting.
- [ ] A11.S05 — CI/CD for models.
- [ ] A11.S06 — Build: a deployed, monitored model service, reusing DataPulse's observability stack.
**Gate artifact:** a model service with dashboards and a drift alert you've watched fire.

## A12 · ML for Markets & Time Series
<!-- rung: G | prereq: A03, finance E07 | feeds: finance E11, your edge -->
**Goal:** Apply ML to markets without fooling yourself — time-series foundations, financial labelling, purged validation.
**Resources:**
- [Hyndman & Athanasopoulos — Forecasting: Principles and Practice](https://otexts.com/fpp3/) — free
- López de Prado — *Advances in Financial Machine Learning* (paid)
**Sessions:**
- [ ] A12.S01 — Time-series fundamentals: stationarity, autocorrelation (FPP3).
- [ ] A12.S02 — Classical forecasting: exponential smoothing, ARIMA.
- [ ] A12.S03 — Financial data structures: time/volume/dollar bars; triple-barrier labelling.
- [ ] A12.S04 — Purged and embargoed cross-validation — why ordinary CV lies in finance.
- [ ] A12.S05 — Feature importance and backtest overfitting.
- [ ] A12.S06 — Build: an ML signal study on your instruments with honest, purged evaluation.
**Gate artifact:** a signal study that reports deflated performance and says clearly whether the edge is real.

## A13 · Research: Papers & Reproductions
<!-- rung: R | prereq: A07 | feeds: your niche -->
**Goal:** Read ML research critically, reproduce it, and add something.
**Resources:**
- [arXiv](https://arxiv.org) — cs.LG, stat.ML
- [Hugging Face Papers (successor to Papers with Code)](https://huggingface.co/papers/trending)
**Sessions:**
- [ ] A13.S01 — Choose a niche (efficient inference, RL, or time series) and start a weekly paper habit.
- [ ] A13.S02 — Read five papers; summarise each in a paragraph.
- [ ] A13.S03 — Reproduce one.
- [ ] A13.S04 — Write it up as a blog post or arXiv-style note.
**Gate artifact:** a public reproduction.
