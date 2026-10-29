# Mathematics

Year 9 → research level. The load-bearing track: physics, ML, quant finance and CS are all written in it.

**How to use this file.** Work strictly top to bottom — `today` always shows the first unticked session. Each session
is sized for one deep block (60–90 min); if it takes two, that's fine — only tick it when it's done. Each rung opens
with a **placement** session that lets you tick off what you already own (append "placed out"). Be honest; if in doubt,
do it anyway — a fast review is cheap, a gap is expensive.

**Levels:** F foundation (KS3–GCSE) · S school-leaving (A-level + Further) · U undergraduate · G graduate · R research.
**Cost:** everything you need to start is free. Books marked (paid) are optional — buy them only when you reach them.

## M01 · Placement & Number Foundations
<!-- rung: F | prereq: none | feeds: everything -->
**Goal:** Know exactly where you stand, and make number work automatic — fractions, percentages, powers and ratio without hesitation.
**Resources:**
- [Dr Frost Maths](https://www.drfrost.org) — free KS3 / GCSE / A-level practice, auto-marked
- [Corbettmaths](https://corbettmaths.com/contents/) — a short video and a worksheet for every topic
- [Physics & Maths Tutor](https://www.physicsandmathstutor.com) — past papers and topic questions
- [Khan Academy Maths](https://www.khanacademy.org/math) — course challenges, useful for placement
**Sessions:**
- [ ] M01.S01 — Placement I: a GCSE Higher paper 1 (non-calculator) from [PMT](https://www.physicsandmathstutor.com/maths-revision/gcse-maths/papers/), timed. Mark it honestly; list every topic you dropped marks on in your notes.
- [ ] M01.S02 — Placement II: a GCSE Higher calculator paper, timed and marked. Tick the sessions in M01–M06 you clearly already own (append "placed out").
- [ ] M01.S03 — Fractions, decimals, percentages: four operations with fractions, recurring decimals → fractions, percentage change and reverse percentages.
- [ ] M01.S04 — Powers and roots: index laws incl. negative and fractional indices, standard form, surds (simplify and rationalise).
- [ ] M01.S05 — Ratio, proportion and rates: direct/inverse proportion, compound measures (speed, density, pressure).
- [ ] M01.S06 — Number theory basics: primes, prime factorisation, HCF/LCM — then write a Python function for each.
- [ ] M01.S07 — Estimation, bounds and accuracy: rounding, significant figures, upper and lower bounds in calculations.
- [ ] M01.S08 — Mixed review: 40 mixed number questions on Dr Frost; target 90%+. Repeat the topics you miss.
**Gate artifact:** a placement report (what you own / what you don't) + a 90%+ mixed number set + `number_tools.py` (prime factorisation, gcd/lcm via Euclid) with tests.
**Anki seeds:** index laws · surd rules · Euclid's algorithm · how bounds combine in + − × ÷

## M02 · Algebra I
<!-- rung: F | prereq: M01 | feeds: everything -->
**Goal:** Manipulate expressions and solve equations fluently — the grammar of all later maths.
**Resources:**
- [Dr Frost Maths](https://www.drfrost.org) — algebra key skills
- [Corbettmaths](https://corbettmaths.com/contents/) — videos + worksheets
- [Khan Academy Algebra 1](https://www.khanacademy.org/math/algebra)
**Sessions:**
- [ ] M02.S01 — Expressions: expanding single, double and triple brackets; collecting terms; substitution.
- [ ] M02.S02 — Factorising: common factors, difference of two squares, quadratics with a = 1 and a ≠ 1.
- [ ] M02.S03 — Linear equations and inequalities: unknowns on both sides, fractions, number lines and set notation.
- [ ] M02.S04 — Rearranging formulae, including when the subject appears twice.
- [ ] M02.S05 — Simultaneous equations: elimination and substitution; linear–linear and linear–quadratic.
- [ ] M02.S06 — Quadratics I: solve by factorising and by the formula; the discriminant and what it tells you.
- [ ] M02.S07 — Quadratics II: completing the square — then derive the quadratic formula yourself.
- [ ] M02.S08 — Algebraic fractions and simple proof: simplify, add, solve; prove identities (e.g. the sum of three consecutive integers is divisible by 3).
- [ ] M02.S09 — Sequences: linear and quadratic nth term, geometric and Fibonacci-type sequences.
**Gate artifact:** the quadratic formula derived by completing the square (written up in Markdown/LaTeX) + a Dr Frost algebra mixed test at 85%+.
**Anki seeds:** factorising patterns · discriminant cases · completed-square form · nth-term methods

## M03 · Functions & Graphs
<!-- rung: F | prereq: M02 | feeds: calculus, ML, physics -->
**Goal:** See equations as shapes — read, sketch and transform graphs, and treat functions as objects.
**Resources:**
- [Dr Frost Maths](https://www.drfrost.org)
- [Desmos graphing calculator](https://www.desmos.com/calculator) — experiment freely
- [matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
**Sessions:**
- [ ] M03.S01 — Straight lines: gradient, y = mx + c, parallel and perpendicular lines, the equation through two points.
- [ ] M03.S02 — Quadratic graphs: roots, turning point via completing the square, sketching.
- [ ] M03.S03 — Other graphs: cubic, reciprocal, exponential — recognise them on sight.
- [ ] M03.S04 — Transformations: y = f(x) + a, f(x + a), −f(x), f(−x), af(x), f(ax). Play in Desmos until each one is obvious.
- [ ] M03.S05 — Functions: notation, domain/range, composite and inverse functions.
- [ ] M03.S06 — Iteration and graphical solutions: solving equations by iteration and by intersecting graphs.
- [ ] M03.S07 — Rates and area: gradients of curves (tangents), area under a graph (trapezia), real-life graphs.
- [ ] M03.S08 — Build it: plot every function family and every transformation in Python (matplotlib) — your graph gallery.
**Gate artifact:** a labelled Python graph gallery + a short written explanation of why f(x + a) shifts the graph *left*.
**Anki seeds:** each transformation and its effect · shape of each graph family · composite/inverse notation

## M04 · Geometry & Trigonometry
<!-- rung: F | prereq: M02 | feeds: physics, vectors, graphics -->
**Goal:** Reason about shape and space, and own the trigonometry that physics leans on.
**Resources:**
- [Dr Frost Maths](https://www.drfrost.org)
- [Corbettmaths](https://corbettmaths.com/contents/)
- [Khan Academy Geometry](https://www.khanacademy.org/math/geometry)
**Sessions:**
- [ ] M04.S01 — Angles and polygons: parallel lines, interior/exterior angles, short angle proofs.
- [ ] M04.S02 — Area and volume: compound shapes, circles, sectors and arcs, prisms, cylinders, cones, spheres, frusta.
- [ ] M04.S03 — Pythagoras and right-angled trig: SOHCAHTOA, exact values for 30°/45°/60°, 3D problems.
- [ ] M04.S04 — Non-right-angled trig: sine rule, cosine rule, area = ½ab sin C, bearings.
- [ ] M04.S05 — Trig graphs: sin, cos and tan and their transformations.
- [ ] M04.S06 — Circle theorems: learn the set, then prove three of them.
- [ ] M04.S07 — Congruence, similarity and transformations: area/volume scale factors, reflections, rotations, enlargements.
- [ ] M04.S08 — Vectors (GCSE): column vectors and vector-geometry proofs (midpoints, parallel lines).
**Gate artifact:** three circle-theorem proofs + one vector-geometry proof, written up + a trig mixed test at 85%+.
**Anki seeds:** exact trig values · sine/cosine rules · circle theorems · volume formulas

## M05 · Probability & Statistics (GCSE)
<!-- rung: F | prereq: M01 | feeds: statistics, ML, quant -->
**Goal:** Reason about chance and data — the seed of statistics, ML and every risk model you'll build.
**Resources:**
- [Dr Frost Maths](https://www.drfrost.org)
- [Khan Academy Statistics & Probability](https://www.khanacademy.org/math/statistics-probability)
**Sessions:**
- [ ] M05.S01 — Probability rules: sample spaces, mutually exclusive and independent events, the OR and AND rules.
- [ ] M05.S02 — Tree diagrams and conditional probability, with and without replacement.
- [ ] M05.S03 — Venn diagrams and set notation; conditional probability from Venns.
- [ ] M05.S04 — Averages and spread from tables; estimates from grouped data.
- [ ] M05.S05 — Statistical diagrams: histograms (frequency density), cumulative frequency, box plots, comparing distributions.
- [ ] M05.S06 — Sampling and correlation: sampling methods, scatter graphs, correlation vs causation.
- [ ] M05.S07 — Simulate it: Monte Carlo in Python — estimate the probabilities from S01–S03 by simulation and compare with the exact answers.
**Gate artifact:** a Monte Carlo script comparing simulated and exact probabilities, with a paragraph on why they converge.

## M06 · GCSE Mastery
<!-- rung: F | prereq: M01–M05 | feeds: the A-level rung -->
**Goal:** Prove the foundation is solid — grade-9 standard under exam conditions.
**Resources:**
- [Physics & Maths Tutor — GCSE past papers](https://www.physicsandmathstutor.com/maths-revision/gcse-maths/papers/)
- [Dr Frost Maths](https://www.drfrost.org)
**Sessions:**
- [ ] M06.S01 — Past paper (non-calculator), timed; mark it; start an "error log" of mistake types.
- [ ] M06.S02 — Repair: relearn the two weakest topics from S01.
- [ ] M06.S03 — Past paper (calculator), timed; mark it.
- [ ] M06.S04 — Repair session.
- [ ] M06.S05 — Past paper (calculator), timed; mark it.
- [ ] M06.S06 — Hard-question set: the last five questions of five different papers (the grade 8–9 problems).
**Gate artifact:** three full papers at or above the grade-9 boundary + the error log showing what you fixed.

## M07 · A-level Pure I: Proof, Algebra & Functions
<!-- rung: S | prereq: M06 | feeds: all proof-based maths -->
**Goal:** Make the jump from doing to showing *why* — proof, and algebra at A-level depth.
**Resources:**
- [Dr Frost Maths — A-level](https://www.drfrost.org)
- [Physics & Maths Tutor — A-level Maths](https://www.physicsandmathstutor.com/maths-revision/a-level-maths/)
- [OpenStax Algebra and Trigonometry](https://openstax.org/subjects/math) — free textbook
- [Khan Academy Precalculus](https://www.khanacademy.org/math/precalculus)
**Sessions:**
- [ ] M07.S01 — A-level placement: a Pure paper from PMT, timed and marked; tick what you already own in M07–M12.
- [ ] M07.S02 — Proof: direct proof, proof by exhaustion, disproof by counterexample.
- [ ] M07.S03 — Proof by contradiction: √2 is irrational; there are infinitely many primes. Write both up properly.
- [ ] M07.S04 — Indices, surds and quadratics revisited: harder manipulation, quadratic inequalities, line–circle intersections.
- [ ] M07.S05 — Polynomials: algebraic division, the factor theorem, the remainder theorem.
- [ ] M07.S06 — Functions at depth: modulus functions, composite and inverse functions, graph transformations combined.
- [ ] M07.S07 — Partial fractions: linear and repeated factors (you'll need them for integration).
**Gate artifact:** a proof portfolio (6+ proofs, including √2 irrational and the infinitude of primes) in Markdown/LaTeX.
**Anki seeds:** proof templates (direct, contradiction, counterexample) · factor and remainder theorems · partial-fraction forms

## M08 · A-level Pure II: Coordinates, Series, Trig & Logs
<!-- rung: S | prereq: M07 | feeds: calculus, physics, finance -->
**Goal:** The toolkit calculus will use — circles, series, radians, identities and logarithms.
**Resources:**
- [Dr Frost Maths — A-level](https://www.drfrost.org)
- [OpenStax Precalculus](https://openstax.org/subjects/math) — free textbook
**Sessions:**
- [ ] M08.S01 — Coordinate geometry: lines and circles (centre/radius by completing the square), tangents and chords.
- [ ] M08.S02 — Binomial expansion: positive integer powers, then rational powers and when the series is valid.
- [ ] M08.S03 — Arithmetic and geometric series, sums to infinity, sigma notation, recurrence relations.
- [ ] M08.S04 — Radians and trig identities: arc length and sector area in radians, small-angle approximations, sec/cosec/cot.
- [ ] M08.S05 — Compound and double-angle formulae; the R sin(x + α) form; solving trig equations.
- [ ] M08.S06 — Exponentials and logarithms: laws of logs, solving exponential equations, e and ln.
- [ ] M08.S07 — Modelling with exponentials: growth and decay; use log–linear graphs to find parameters from data.
**Gate artifact:** the compound-angle formula derived geometrically + an exponential model fitted to real data via logs (Python), written up.
**Anki seeds:** trig identities · log laws · series sum formulas · binomial validity condition

## M09 · Calculus I
<!-- rung: S | prereq: M08 | feeds: physics, ML, quant, everything after -->
**Goal:** Understand change and accumulation — derivatives and integrals from first principles to real applications.
**Resources:**
- [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/topics/calculus) — watch first, for intuition
- [MIT 18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/)
- [OpenStax Calculus Volume 1](https://openstax.org/subjects/math) — free textbook
- [Dr Frost Maths — A-level](https://www.drfrost.org)
**Sessions:**
- [ ] M09.S01 — Intuition first: [3Blue1Brown Essence of Calculus](https://www.3blue1brown.com/topics/calculus) chapters 1–4 (derivatives as rates; the rules seen visually).
- [ ] M09.S02 — Limits and first principles: derive d/dx of xⁿ, sin x and eˣ from the definition.
- [ ] M09.S03 — The rules: product, quotient, chain; derivatives of eˣ, ln x, trig functions and their inverses.
- [ ] M09.S04 — Applications: tangents and normals, stationary points and the second derivative, optimisation problems.
- [ ] M09.S05 — Implicit and parametric differentiation; connected rates of change.
- [ ] M09.S06 — Integration as anti-differentiation and as area; definite integrals; area between curves (3B1B chapters 8–9 for the fundamental theorem).
- [ ] M09.S07 — Techniques: substitution, by parts, using partial fractions, trig integrals.
- [ ] M09.S08 — Differential equations: forming and solving separable ODEs (growth, cooling, mixing).
- [ ] M09.S09 — Numerical methods: Newton–Raphson and the trapezium rule — implement both and compare with exact answers.
**Gate artifact:** first-principles derivations of d/dx(sin x), d/dx(eˣ), d/dx(ln x) + a Python numerical-methods script with an error-vs-step-size plot.
**Anki seeds:** standard derivatives and integrals · chain/product/quotient forms · integration by parts · Newton–Raphson update

## M10 · A-level Statistics
<!-- rung: S | prereq: M05, M09 | feeds: statistics, ML, quant -->
**Goal:** From describing data to testing claims about it — the start of real inference.
**Resources:**
- [Dr Frost Maths — A-level statistics](https://www.drfrost.org)
- [OpenIntro Statistics](https://www.openintro.org/book/os/) — free textbook
**Sessions:**
- [ ] M10.S01 — Data at A-level: location and spread, outliers, coding, interpreting large data sets.
- [ ] M10.S02 — Probability in depth: Venn and tree diagrams, conditional probability, testing for independence.
- [ ] M10.S03 — The binomial distribution: modelling, cumulative probabilities.
- [ ] M10.S04 — Hypothesis testing with the binomial: one- and two-tailed tests, critical regions, significance.
- [ ] M10.S05 — The normal distribution: standardising, the inverse normal, approximating the binomial.
- [ ] M10.S06 — Correlation and regression; hypothesis tests for correlation.
- [ ] M10.S07 — Apply it: test a claim about your own trading (e.g. "my win rate is above 50%") and write it up honestly.
**Gate artifact:** a hypothesis-test write-up on your own data with assumptions, result and limitations stated plainly.

## M11 · A-level Mechanics
<!-- rung: S | prereq: M09 | feeds: physics -->
**Goal:** Mathematics that moves — the bridge into physics.
**Resources:**
- [Dr Frost Maths — mechanics](https://www.drfrost.org)
- [Isaac Physics](https://isaacphysics.org) — excellent free problem platform
**Sessions:**
- [ ] M11.S01 — Kinematics: derive SUVAT; displacement–time and velocity–time graphs; calculus in kinematics.
- [ ] M11.S02 — Forces and Newton's laws: resolving forces, connected particles, pulleys.
- [ ] M11.S03 — Friction and inclined planes.
- [ ] M11.S04 — Projectiles: trajectory equation, range, maximum height.
- [ ] M11.S05 — Moments: equilibrium of rigid bodies, ladder problems.
- [ ] M11.S06 — Simulate a projectile with air resistance in Python and compare it with the drag-free analytic result.
**Gate artifact:** the projectile-with-drag simulation compared to the analytic solution + a written derivation of the trajectory equation.

## M12 · Further Maths Core
<!-- rung: S | prereq: M09 | feeds: linear algebra, physics, signal processing -->
**Goal:** The extra tools every undergraduate course assumes — complex numbers, matrices, induction, series.
**Resources:**
- [Dr Frost Maths — Further Maths](https://www.drfrost.org)
- [Physics & Maths Tutor — Further Maths](https://www.physicsandmathstutor.com/maths-revision/a-level-further-maths/)
- [3Blue1Brown](https://www.3blue1brown.com) — Euler's formula and complex numbers videos
- [OpenStax Calculus Volume 2](https://openstax.org/subjects/math)
**Sessions:**
- [ ] M12.S01 — Complex numbers: arithmetic, the Argand diagram, modulus–argument form.
- [ ] M12.S02 — Exponential form, de Moivre's theorem, nth roots of unity.
- [ ] M12.S03 — Matrices: operations, 2×2 and 3×3 determinants and inverses, matrices as transformations.
- [ ] M12.S04 — Proof by induction: sums, divisibility, matrix powers.
- [ ] M12.S05 — Further algebra: roots of polynomials, the method of differences, series summation.
- [ ] M12.S06 — Maclaurin series: derive the series for eˣ, sin x, cos x and ln(1 + x); convergence intuition.
- [ ] M12.S07 — Euler's formula: derive e^(iθ) = cos θ + i sin θ from the series — and see why it matters.
- [ ] M12.S08 — Hyperbolic functions, polar coordinates, volumes of revolution.
- [ ] M12.S09 — Second-order linear ODEs with constant coefficients (auxiliary equation, complementary function + particular integral).
**Gate artifact:** Euler's formula derived from Maclaurin series + 5+ induction proofs + roots of unity visualised in Python.
**Anki seeds:** de Moivre · Maclaurin series of the standard functions · matrix inverse (2×2) · induction template

## M13 · Proof & Discrete Mathematics
<!-- rung: U | prereq: M12 | feeds: CS, cryptography, probability -->
**Goal:** Think like a mathematician and a computer scientist at once — logic, proof, counting, graphs. (Shared with the CS track.)
**Resources:**
- [MIT 6.042J Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — lectures + the free textbook (Lehman, Leighton, Meyer)
**Sessions:**
- [ ] M13.S01 — Propositional and predicate logic; what a proof actually is.
- [ ] M13.S02 — Induction (ordinary and strong) and the well-ordering principle.
- [ ] M13.S03 — Sets, functions and relations; countable vs uncountable (Cantor's diagonal argument).
- [ ] M13.S04 — Number theory: gcd, modular arithmetic, Fermat's little theorem, RSA — implement RSA in Python.
- [ ] M13.S05 — Graph theory: definitions, trees, matchings, colouring, connectivity.
- [ ] M13.S06 — Directed graphs and partial orders; state machines and invariants.
- [ ] M13.S07 — Counting: sums and asymptotics, bijections, permutations/combinations, inclusion–exclusion, pigeonhole.
- [ ] M13.S08 — Discrete probability: events, conditional probability, random variables, expectation (6.042 style).
**Gate artifact:** a proof set (10+, mixed techniques) + a working RSA implementation with a written correctness argument.
**Anki seeds:** proof techniques · Fermat's little theorem · RSA steps · counting principles

## M14 · Linear Algebra I (computational)
<!-- rung: U | prereq: M12 | feeds: ML (heavily), physics, CS -->
**Goal:** Fluency with vectors, matrices, subspaces, eigenvalues and the SVD — the single most useful maths for ML.
**Resources:**
- [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)
- [MIT 18.06SC Linear Algebra (Gilbert Strang)](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) — lectures + problem sets
**Sessions:**
- [ ] M14.S01 — Intuition first: [Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra) chapters 1–7 (vectors, span, linear maps, matrix multiplication, determinants, inverses).
- [ ] M14.S02 — 18.06: the geometry of Ax = b, elimination, multiplication and inverses, A = LU.
- [ ] M14.S03 — Vector spaces and subspaces; column space and nullspace; solving Ax = 0 and Ax = b.
- [ ] M14.S04 — Independence, basis and dimension; the four fundamental subspaces.
- [ ] M14.S05 — Orthogonality, projections and least squares — fit a line to data by projection.
- [ ] M14.S06 — Orthogonal matrices and Gram–Schmidt (QR); determinants and their properties.
- [ ] M14.S07 — Eigenvalues and eigenvectors; diagonalisation; powers of matrices; Markov matrices.
- [ ] M14.S08 — Symmetric and positive-definite matrices.
- [ ] M14.S09 — The singular value decomposition: what it is and why it matters.
- [ ] M14.S10 — Build it in NumPy: Gaussian elimination, Gram–Schmidt QR, power iteration, SVD image compression.
**Gate artifact:** a `linalg` mini-library (elimination, QR, power iteration) tested against `numpy.linalg` + an SVD image-compression demo with a rank-vs-error plot.
**Anki seeds:** the four subspaces · rank–nullity · projection formula · eigen definitions · SVD statement

## M15 · Calculus II: Series & Multivariable
<!-- rung: U | prereq: M09, M14 | feeds: ML, physics, optimisation -->
**Goal:** Finish single-variable calculus properly, then go to several variables — gradients, multiple integrals, vector calculus.
**Resources:**
- [MIT 18.01SC](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) — the series unit
- [MIT 18.02SC Multivariable Calculus](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/)
- [OpenStax Calculus Volumes 2–3](https://openstax.org/subjects/math)
**Sessions:**
- [ ] M15.S01 — Sequences and series: convergence tests, power series, Taylor's theorem with remainder.
- [ ] M15.S02 — Improper integrals and L'Hôpital's rule.
- [ ] M15.S03 — Vectors in 3D: dot and cross products, lines and planes.
- [ ] M15.S04 — Partial derivatives, the gradient, directional derivatives, the multivariable chain rule.
- [ ] M15.S05 — Optimisation in several variables; Lagrange multipliers.
- [ ] M15.S06 — Double integrals; polar coordinates; change of variables and the Jacobian.
- [ ] M15.S07 — Line integrals, conservative fields, Green's theorem.
- [ ] M15.S08 — Triple and surface integrals; the divergence theorem; Stokes' theorem.
- [ ] M15.S09 — Build it: visualise a gradient field and verify Green's theorem numerically in Python.
**Gate artifact:** a numerical verification of Green's (or Stokes') theorem + a written Lagrange-multiplier solution to a real problem (e.g. a portfolio with a budget constraint).

## M16 · Probability
<!-- rung: U | prereq: M13, M15 | feeds: statistics, ML, quant, physics -->
**Goal:** Real probability — random variables, distributions, expectation, limit theorems, Markov chains.
**Resources:**
- [Harvard Stat 110 (Joe Blitzstein)](https://projects.iq.harvard.edu/stat110) — lectures, problem sets, and the free book *Introduction to Probability* (Blitzstein & Hwang)
**Sessions:**
- [ ] M16.S01 — Probability and counting; story proofs; the naive definition and its limits.
- [ ] M16.S02 — Conditional probability, Bayes' rule, independence; the Monty Hall problem done right.
- [ ] M16.S03 — Random variables: Bernoulli, binomial, hypergeometric, geometric, Poisson — and their stories.
- [ ] M16.S04 — Expectation: linearity, indicator random variables, LOTUS.
- [ ] M16.S05 — Continuous random variables: uniform, normal, exponential; universality of the uniform.
- [ ] M16.S06 — Moments and moment generating functions.
- [ ] M16.S07 — Joint distributions, covariance and correlation, the multivariate normal.
- [ ] M16.S08 — Transformations and convolutions; beta and gamma distributions.
- [ ] M16.S09 — Conditional expectation; Markov, Chebyshev and Jensen inequalities; the law of large numbers and the CLT.
- [ ] M16.S10 — Markov chains: transition matrices, stationary distributions — simulate one.
**Gate artifact:** written solutions to selected Stat 110 problems + a CLT simulation showing convergence for three different distributions.
**Anki seeds:** distribution stories and PMFs/PDFs · expectation/variance table · Bayes · LOTUS · CLT statement

## M17 · Linear Algebra II (proof-based)
<!-- rung: U | prereq: M14, M13 | feeds: quantum mechanics, functional analysis, ML theory -->
**Goal:** Understand linear algebra as a theory — abstract vector spaces, operators, the spectral theorem.
**Resources:**
- [Axler — Linear Algebra Done Right, 4th ed.](https://linear.axler.net) — free, with the author's video lectures
**Sessions:**
- [ ] M17.S01 — Vector spaces: fields, definitions, subspaces, sums and direct sums.
- [ ] M17.S02 — Finite-dimensional spaces: span, independence, bases, dimension.
- [ ] M17.S03 — Linear maps: null space and range, the fundamental theorem, matrices, invertibility, duality.
- [ ] M17.S04 — Polynomials; eigenvalues, eigenvectors and invariant subspaces; upper-triangular matrices.
- [ ] M17.S05 — Inner product spaces: norms, orthonormal bases, Gram–Schmidt, orthogonal complements.
- [ ] M17.S06 — Operators on inner product spaces: self-adjoint and normal operators, the spectral theorem, the SVD.
- [ ] M17.S07 — Operators on complex vector spaces: generalised eigenvectors, Jordan form.
- [ ] M17.S08 — Multilinear algebra and determinants.
**Gate artifact:** the spectral theorem proved in your own words + selected Axler exercises written up in LaTeX.

## M18 · Real Analysis
<!-- rung: U | prereq: M15, M13 | feeds: measure theory, probability, everything rigorous -->
**Goal:** Put calculus on solid ground — completeness, limits, continuity, derivatives and integrals, with ε–δ rigour.
**Resources:**
- [MIT 18.100A Real Analysis](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/)
- [Lebl — Basic Analysis](https://www.jirka.org/ra/) — free textbook
- Abbott — *Understanding Analysis* (paid, the friendliest text)
**Sessions:**
- [ ] M18.S01 — The real numbers: ordered fields, the least-upper-bound property, the Archimedean property.
- [ ] M18.S02 — Sequences: limits, monotone convergence, Bolzano–Weierstrass, Cauchy sequences.
- [ ] M18.S03 — Series: the convergence tests revisited, now with proofs.
- [ ] M18.S04 — Continuity: ε–δ, the intermediate and extreme value theorems, uniform continuity.
- [ ] M18.S05 — The derivative: the mean value theorem and Taylor's theorem, proved.
- [ ] M18.S06 — The Riemann integral: definition, integrability, the fundamental theorem of calculus, proved.
- [ ] M18.S07 — Sequences of functions: pointwise vs uniform convergence; when you may swap limits.
- [ ] M18.S08 — Metric spaces: open/closed sets, compactness, completeness.
**Gate artifact:** an ε–δ proof portfolio including your own proofs of the MVT and the FTC.

## M19 · Differential Equations
<!-- rung: U | prereq: M15, M14 | feeds: physics, quant, engineering -->
**Goal:** Model change in physics, finance and engineering — and solve the equations analytically and numerically.
**Resources:**
- [MIT 18.03SC Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/)
- [OpenStax Calculus Volume 3](https://openstax.org/subjects/math) — second-order equations chapter
**Sessions:**
- [ ] M19.S01 — First-order ODEs: separable and linear (integrating factor); modelling.
- [ ] M19.S02 — Numerics: Euler's method and its error; RK4 — implement both.
- [ ] M19.S03 — Second-order linear ODEs with constant coefficients; the harmonic oscillator, damping, resonance.
- [ ] M19.S04 — Fourier series.
- [ ] M19.S05 — Laplace transforms; solving ODEs with them; convolution.
- [ ] M19.S06 — First-order linear systems; the eigenvalue method; phase portraits.
- [ ] M19.S07 — Nonlinear systems and stability; linearisation (pendulum, predator–prey).
- [ ] M19.S08 — Build it: a phase-portrait plotter for 2D systems.
**Gate artifact:** the phase-portrait tool + an RK4-vs-Euler error study + one modelling write-up (e.g. a damped, driven oscillator).

## M20 · Statistics & Inference
<!-- rung: U | prereq: M16 | feeds: ML, econometrics, quant -->
**Goal:** Learn from data properly — estimation, uncertainty, testing, regression, Bayesian reasoning.
**Resources:**
- [MIT 18.650 Statistics for Applications](https://ocw.mit.edu/courses/18-650-statistics-for-applications-fall-2016/)
- [OpenIntro Statistics](https://www.openintro.org/book/os/) — free
- [ISLP](https://www.statlearning.com) — free, for regression
**Sessions:**
- [ ] M20.S01 — Estimation: bias, variance, MSE, consistency.
- [ ] M20.S02 — Maximum likelihood; Fisher information; the method of moments.
- [ ] M20.S03 — Confidence intervals; the bootstrap — implement it.
- [ ] M20.S04 — Hypothesis testing done honestly: p-values, power, multiple testing.
- [ ] M20.S05 — Linear regression: least squares as projection (from M14), inference on coefficients, diagnostics.
- [ ] M20.S06 — Bayesian inference: priors, posteriors, conjugacy, MAP vs MLE.
- [ ] M20.S07 — Goodness of fit and nonparametric tests.
- [ ] M20.S08 — Apply it: a full analysis of your trading data — estimates, intervals, a test, a regression, and what you *can't* conclude.
**Gate artifact:** a complete statistical report on a real dataset, including a section on what the data cannot tell you.

## M21 · Numerical Methods
<!-- rung: U | prereq: M14, M19 | feeds: physics simulation, quant, ML -->
**Goal:** Compute reliably — understand floating point, error and stability so your numbers can be trusted.
**Resources:**
- [MIT 18.335J Introduction to Numerical Methods](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/)
- Trefethen & Bau — *Numerical Linear Algebra* (paid)
**Sessions:**
- [ ] M21.S01 — Floating point: IEEE 754, rounding error, catastrophic cancellation — demonstrate each in Python.
- [ ] M21.S02 — Root finding: bisection, Newton, secant; rates of convergence.
- [ ] M21.S03 — Interpolation and approximation: polynomial interpolation, Runge's phenomenon, splines.
- [ ] M21.S04 — Numerical integration: quadrature rules and their error.
- [ ] M21.S05 — Numerical linear algebra: conditioning, LU with pivoting, QR, iterative methods.
- [ ] M21.S06 — ODE solvers revisited: stiffness, stability regions, adaptive step sizes.
- [ ] M21.S07 — Build it: a small numerics library with an error-analysis notebook.
**Gate artifact:** the numerics library + an essay on conditioning vs stability, with examples.

## M22 · Optimisation
<!-- rung: U | prereq: M15, M14 | feeds: ML training, portfolio construction -->
**Goal:** The mathematics of "best" — convexity, gradients and duality, behind ML training and portfolio construction.
**Resources:**
- [Boyd & Vandenberghe — Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/) — free PDF + Stanford EE364a lectures
**Sessions:**
- [ ] M22.S01 — Convex sets.
- [ ] M22.S02 — Convex functions.
- [ ] M22.S03 — Convex optimisation problems: LP, QP and standard forms.
- [ ] M22.S04 — Duality and the KKT conditions.
- [ ] M22.S05 — Unconstrained minimisation: gradient descent and Newton's method — implement both.
- [ ] M22.S06 — Equality-constrained minimisation; interior-point methods (intuition).
- [ ] M22.S07 — Apply it: mean–variance portfolio optimisation (finance) and logistic-regression training (ML).
**Gate artifact:** gradient descent + Newton implementations with convergence plots + a solved portfolio optimisation, written up.

## M23 · Abstract Algebra
<!-- rung: U | prereq: M13 | feeds: cryptography, physics (symmetry) -->
**Goal:** Structure for its own sake — groups, rings and fields — with payoffs in cryptography and the symmetries of physics.
**Resources:**
- [Judson — Abstract Algebra: Theory and Applications](http://abstract.ups.edu) — free textbook
**Sessions:**
- [ ] M23.S01 — Groups: definitions, examples, subgroups.
- [ ] M23.S02 — Cyclic groups and permutation groups.
- [ ] M23.S03 — Cosets and Lagrange's theorem; applications to number theory.
- [ ] M23.S04 — Homomorphisms, isomorphisms, normal subgroups, quotient groups.
- [ ] M23.S05 — Rings, ideals, integral domains.
- [ ] M23.S06 — Fields; polynomial rings; finite fields.
- [ ] M23.S07 — Build it: finite-field arithmetic in Python (feeds cryptography).
**Gate artifact:** selected exercises proved + a tested GF(p) and GF(2⁸) implementation.

## M24 · Complex Analysis
<!-- rung: U | prereq: M12, M18 | feeds: physics, signal processing -->
**Goal:** Calculus with complex numbers — contour integrals and residues, used throughout physics and signal processing.
**Resources:**
- [MIT 18.04 Complex Variables with Applications](https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/)
- Beck et al. — *A First Course in Complex Analysis* (free online)
**Sessions:**
- [ ] M24.S01 — Complex functions, limits, analyticity, the Cauchy–Riemann equations.
- [ ] M24.S02 — Elementary functions: exp, log and branch cuts.
- [ ] M24.S03 — Contour integrals; Cauchy's theorem and integral formula.
- [ ] M24.S04 — Taylor and Laurent series; singularities.
- [ ] M24.S05 — The residue theorem; evaluating real integrals with residues.
- [ ] M24.S06 — Conformal maps and their applications.
**Gate artifact:** a residue-calculus problem set + one real integral evaluated by contour integration, fully written up.

## M25 · Measure Theory & Probability
<!-- rung: G | prereq: M18, M16 | feeds: stochastic calculus, ML theory -->
**Goal:** Probability on rigorous foundations — what stochastic calculus and serious ML theory are built on.
**Resources:**
- [Axler — Measure, Integration & Real Analysis](https://measure.axler.net) — free
- Durrett — *Probability: Theory and Examples* (free PDF on the author's Duke page)
**Sessions:**
- [ ] M25.S01 — Why Riemann integration isn't enough; σ-algebras and measures.
- [ ] M25.S02 — Lebesgue measure; measurable functions.
- [ ] M25.S03 — Integration with respect to a measure; the monotone and dominated convergence theorems.
- [ ] M25.S04 — Product measures and Fubini; Lᵖ spaces.
- [ ] M25.S05 — Probability spaces; random variables as measurable functions; expectation as an integral.
- [ ] M25.S06 — The weak and strong laws of large numbers, with proofs.
- [ ] M25.S07 — The central limit theorem via characteristic functions.
- [ ] M25.S08 — Measure-theoretic conditional expectation and martingales — the bridge to stochastic calculus.
**Gate artifact:** your proofs of the monotone and dominated convergence theorems + a write-up of conditional expectation as a projection.

## M26 · Stochastic Processes & Stochastic Calculus
<!-- rung: G | prereq: M25, M19 | feeds: quant finance (E08), diffusion models (A10) -->
**Goal:** Brownian motion, Itô calculus and SDEs — the mathematics of quantitative finance and of diffusion models.
**Resources:**
- [MIT 18.S096 Topics in Mathematics with Applications in Finance](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/)
- Shreve — *Stochastic Calculus for Finance II* (paid — the standard)
**Sessions:**
- [ ] M26.S01 — Random walks → Brownian motion; its properties; simulate paths.
- [ ] M26.S02 — Continuous-time martingales; quadratic variation.
- [ ] M26.S03 — The Itô integral: construction and properties.
- [ ] M26.S04 — Itô's lemma: derive it, then apply it to geometric Brownian motion.
- [ ] M26.S05 — Stochastic differential equations; Euler–Maruyama simulation.
- [ ] M26.S06 — Girsanov's theorem and change of measure (risk-neutral pricing intuition).
- [ ] M26.S07 — Feynman–Kac; derive the Black–Scholes PDE.
- [ ] M26.S08 — Build it: an SDE simulator (GBM, OU, CIR) with convergence checks.
**Gate artifact:** Itô's lemma derived + the Black–Scholes PDE derived two ways (hedging and risk-neutral expectation) + the SDE simulator.

## M27 · Functional Analysis
<!-- rung: G | prereq: M25, M17 | feeds: quantum mechanics, kernel methods -->
**Goal:** Infinite-dimensional linear algebra — the language of quantum mechanics and kernel methods in ML.
**Resources:**
- [Axler — Measure, Integration & Real Analysis](https://measure.axler.net) — the Banach, Lᵖ and Hilbert space chapters
- [MIT 18.102 Introduction to Functional Analysis](https://ocw.mit.edu/search/?q=18.102)
**Sessions:**
- [ ] M27.S01 — Normed and Banach spaces; bounded linear operators.
- [ ] M27.S02 — Hilbert spaces; orthonormal bases; projections.
- [ ] M27.S03 — Lᵖ spaces and duality.
- [ ] M27.S04 — Compact and self-adjoint operators; the infinite-dimensional spectral theorem.
- [ ] M27.S05 — Applications: Fourier series as an orthonormal basis; reproducing kernel Hilbert spaces (ML).
**Gate artifact:** a write-up connecting the finite spectral theorem (M17) to its infinite-dimensional version, with a quantum-mechanics example.

## M28 · High-Dimensional Probability
<!-- rung: G | prereq: M25, M17 | feeds: ML theory, statistics -->
**Goal:** Why learning works in high dimensions — concentration of measure and random matrices.
**Resources:**
- Vershynin — *High-Dimensional Probability* (free PDF on the author's site)
**Sessions:**
- [ ] M28.S01 — Concentration of sums: Hoeffding, Chernoff, Bernstein.
- [ ] M28.S02 — Sub-Gaussian and sub-exponential random variables.
- [ ] M28.S03 — Random vectors in high dimensions; the geometry of high-dimensional space.
- [ ] M28.S04 — Random matrices and operator norms.
- [ ] M28.S05 — Applications: covariance estimation, the Johnson–Lindenstrauss lemma, generalisation in ML.
**Gate artifact:** a Johnson–Lindenstrauss demonstration in Python + an explainer on concentration inequalities.

## M29 · Research: Your Specialisation
<!-- rung: R | prereq: the G rung | feeds: your niche -->
**Goal:** Read, reproduce and extend work at the frontier of your chosen area.
**Resources:**
- [arXiv](https://arxiv.org) — math.PR, math.OC, stat.ML, q-fin
**Sessions:**
- [ ] M29.S01 — Choose the area (likely stochastic processes, optimisation or high-dimensional statistics) and write a one-page research-interest statement.
- [ ] M29.S02 — Build a reading list of ten papers; read the two most-cited carefully.
- [ ] M29.S03 — Reproduce a key result from one paper (a proof or a computation).
- [ ] M29.S04 — Write an expository note on it — the explanation you wish had existed.
- [ ] M29.S05 — Find an open question or an extension; attempt it; write up what happened.
**Gate artifact:** a reproduced result + an expository note, published (blog or arXiv-style PDF).
