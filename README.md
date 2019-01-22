# **ORIE 7191: Topics in Optimization for Machine Learning**

This reading course will explore modern challenges
at the interface of continuous optimization and machine learning.
Our inquiry will be guided by two motivating questions:

1) Can we use classical ideas in optimization to better understand
(and improve) algorithms for challenging problems in machine learning?
2) How can modern insights in machine learning guide the design of
new and improved methods for optimization?

Topics may include low rank optimization,
generalization in deep learning,
regularization (implicit and explicit) for deep learning,
connections between control theory and modern reinforcement learning,
and optimization for trustworthy machine learning (including fair, causal, or interpretable models).
Topics may change according to student interest.

The format will consist of student-guided discussion on papers.
The course will culminate in a final research project
which will constitute a majority of the grade.
Students will deliver short presentations on their projects in class
in addition to written reports.

# Logistics

* **When:** 11:40 - 12:55 TTh
* **Where:** Hollister Hall 372 or via [Zoom](https://zoom.us/j/7221862735)
* [Quiz](https://goo.gl/forms/yOKLIbzP68M0qac52) (same link for all quizzes)
* [CMT](https://cmt3.research.microsoft.com/ORIE7191S2019) for paper reviews and peer reviews
* [Slack](https://join.slack.com/t/orie7191/signup) (use your cornell.edu address)
for general questions and comments.

Office hours will be chosen via an in-class poll.
You can also talk with Prof. Udell after class or
contact her by email at udell@cornell.edu to set up an appointment.

# Course format and requirements

Students are required to attend class, with at most two absences.
(Up to two classes may also be attended remotely via [Zoom](https://zoom.us/j/7221862735)
by prior arrangement with the instructor.
Students at Cornell Tech may attend all classes remotely.)

Course grades have four components (weights in parentheses for 3 credit option):

* **Reviews** (.3): Students will write reviews
of some (about half) of the papers we read for class
and upload them to CMT.
* **Quiz** (.1): Most classes will begin with a two-question quiz.
The questions will be easy to answer if you read the paper.
Grading on this portion of the course will be nonlinear
(eg, 0 points if too few quiz questions are answered correctly).
* **Present a paper** (.3): Students will each lead the discussion twice (or so), possibly in teams
depending on course enrollment.
The student leading the discussion will prepare a 30 minute presentation using slides,
two true/false or multiple choice questions on the paper,
and a class activity or questions for discussion.
The presentations will be graded by peer review.
* **Research project** (.3):
The final research project should be on a topic with connections
to both continuous optimization and machine learning.
Projects can be in teams of up to two students except by
special advance permission from the instructor.
Students will prepare an initial project proposal, midterm report, and final report
on the project, and will make an in-class presentation.
Research projects can (and should!) advance your PhD research.

Students taking the class for 1 credit will be required
to write fewer reviews,
present only one paper,
and will not be required to complete the research project.
The quiz requirement will be the same.

# Schedule

[This google doc serves as our schedule.](https://docs.google.com/spreadsheets/d/1eSJn0_ANEXfOsZZrYwHoQ6F00FKBLz4olbKVtOLoE40/edit?usp=sharing)
Sign up for presentation slots on the google doc
by adding your names and a link to the paper you'll present.
(Make sure not to choose a paper someone else has already picked!)
We may spend more or less time on a topic depending on student interest.

# Reading

The course readings will be selected from the following,
or other papers suggested by students in the class.

## Low Rank Optimization

Our tour begins with low rank optimization.
Many of the ideas developed (rigorously) for low rank optimization
carry over (heuristically) to deep learning.
Here we see two ways to formulate the problem: as a biconvex
problem, or as a convex problem with a low rank constraint
(or, sometimes, side information).
Here, we know how to provably find the solution to the problem
(using convex methods); we can sometimes prove that the nonconvex
method finds the same solution, and can always evaluate the quality
of any putative solution relative to the true optimal solution.

### Smooth nonconvex low rank optimization

* [Barvinok 1995](https://link.springer.com/article/10.1007/BF02574037), [Pataki 1998](https://pubsonline.informs.org/doi/abs/10.1287/moor.23.2.339) show that rank of exact solutions to SDP with m linear constraints grow as O(sqrt(m))
* [Barvinok 2002](???) p. 140: rank of epsilon approximation to a PSD matrix satisfying m linear constraints grows as log(m / epsilon)
* [So, Ye, and Zhang 2008](http://www1.se.cuhk.edu.hk/~manchoso/papers/SDPrank-MOR.pdf) Similar to above low rank approximation idea, more algorithmic. Still requires solving the SDP first.
* [Hazan 2008](???) suggests using Franke Wolfe for semidefinite programming
* [Garber and Hazan 2011](http://papers.nips.cc/paper/4198-approximating-semidefinite-programs-in-sublinear-time) integrates the above idea into a method to produce approximate solutions of SDP
* [Jaggi 2013](???) Solving matrix completion with Frank Wolfe ensures rank is bounded by number of iterations
* [Yurtsever et al. 2017](https://arxiv.org/abs/1702.06838) The first storage-optimal convex method for matrix completion

### Nonsmooth convex low rank optimization

* [Burer and Monteiro 2003](???) Original paper proposing factored formulation for solving SDPs
* [Journ\'ee et al. 2010](https://epubs.siam.org/doi/abs/10.1137/080731359) How to escape a saddle point with gradient information
* [Boumal et al. 2014](http://www.jmlr.org/papers/volume15/boumal14a/boumal14a.pdf)
* [Boumal, Voroninski, and Bandeira 2016](???) The non-convex Burer-Monteiro approach works on smooth semidefinite programs
* [Bhojanapalli et al. 2018](???) Smoothed analysis of BM factorization
* finding local minima efficiently: [Lee et al. 2016](http://www.jmlr.org/proceedings/papers/v49/lee16.pdf) shows GD only converges to minimizers (not saddle points), and [Lee et al. 2017](https://arxiv.org/abs/1710.07406) extends the result to other first order methods
* [Gunasekar et al. 2017](http://papers.nips.cc/paper/7195-implicit-regularization-in-matrix-factorization.pdf) Gradient descent on factored formulation of matrix completion implicitly regularized the nuclear norm
* [Bhojanapalli, Neyshabur, and Srebro 2016](http://papers.nips.cc/paper/6271-global-optimality-of-local-search-for-low-rank-matrix-recovery.pdf) [Ge, Lee, and Ma 2016](http://papers.nips.cc/paper/6048-matrix-completion-has-no-spurious-local-minimum.pdf) The factored formulation of matrix completion from incoherent measurements has no spurious local minima
* [Ma et al. 2017](https://arxiv.org/pdf/1711.10467.pdf) Gradient descent (implicitly) imposes regularization for a wide variety of statistical models

<!-- Streaming low rank optimization

* grouse
* balzano recent review -->

## Optimization for Deep Learning

What properties of deep nets make them easy or hard to optimize?
* [Dauphin et al. 2014](https://papers.nips.cc/paper/5486-identifying-and-attacking-the-saddle-point-problem-in-high-dimensional-non-convex-optimization.pdf) Is the quality of a critical point proportional to the number of directions of   positive curvature?
* [Zhang et al. 2016](https://arxiv.org/abs/1611.03530) (Not very) deep nets can exactly fit noise. So why do they generalize well for real data?
* [Hao Li and 2017](http://arxiv.org/abs/1712.09913) Visualizing the loss landscape of neural nets. Certain architectures are dramatically more "convex" than others!
* [D Alberti et al. 2018](https://arxiv.org/pdf/1810.08591.pdf) How does the depth and width of a deep neural net (and the associated difficulties with optimization) affect the bias variance tradeoff?
* [Behnam Neyshabur et al. 2019](???) Maybe deeps nets aren't as overparametrized as they seem
* [Ian Goodfellow, Oriol Vinyals, and Andrew Saxe 2015](http://arxiv.org/abs/1412.6544) The loss surface looks convex on the path from the initial to final SGD iterate

Is optimization enough? Is SGD necessary to provide implicit regularization?
* [Hardt, Recht, and Singer 2015](???) Stability of SGD means that good solutions found quickly should generalize well
* [Keskar et al. 2016](???) Large batch training and sharp minima
* [Hoffer, Hubara, and Soudry 2017](???) A proposal to decrease the generalization gap when using large batch sizes, proposing different explanation than [Keskar et al. 2016](???)
* [Rahimi and Recht 2009](http://papers.nips.cc/paper/3495-weighted-sums-of-random-kitchen-sinks-replacing-minimization-with) + [Rahimi Test of Time Talk at NeurIPS 2017](https://www.youtube.com/watch?v=Qi1Yry33TQE)
* [Kawaguchi, Kaelbling, and Bengio 2017](https://arxiv.org/abs/1710.05468) Generalization in deep learning
* [Neyshabur et al. 2017](http://papers.nips.cc/paper/7176-exploring-generalization-in-deep-learning.pdf) Do (particular) optimization algorithms implicitly regularize the solution found?
* [Gunasekar et al. 2018](???) Studies the same question as above, with new theoretical results
* [Nacson et al. 2018](https://arxiv.org/abs/1803.01905) Studies the same question as above in a simpler case

Can we improve deep learning using more sophisticated ideas from optimization?
* Gradient science blog posts [1](https://gradientscience.org/intro_adversarial/) [2](https://gradientscience.org/robust_opt_pt1/) [3](https://gradientscience.org/robust_opt_pt2/) expound the thesis that GANs are better fit by robust optimization
* [Sinha, Namkoong, and Duchi 2017](https://arxiv.org/abs/1710.10571) Distributionally robust optimization foils adversarial examples
* Gradient science blog posts on [batch normalization](https://gradientscience.org/batchnorm/) attempt to explain its success as a change of geometry
* [Neyshabur, Salakhutdinov, and Srebro 2015](???) Why not optimize in a geometry invariant to rescalings of the parameters that don't affect the output?
* [Wilson et al. 2017](???) Adaptive optimization methods (which learn the geometry from the iterates) can be worse than useless
* Can we use second order methods for training deep nets? Proposals include [Raghu Bollapragada, Richard H. Byrd, and Jorge Nocedal 2016](https://www.semanticscholar.org/paper/Exact-and-Inexact-Subsampled-Newton-Methods-for-Bollapragada-Byrd/d84c77ad09e76e1eba5c511696667582bda6c334) and  [Zhewei Yao et al. 2018](https://arxiv.org/pdf/1810.01021.pdf)

Learn better with fewer parameters
* [Chen et al. 2018](http://papers.nips.cc/paper/7892-neural-ordinary-differential-equations.pdf) Treat number of layers as a continuous parameter (!)
* [Jeremy Bernstein et al. 2018](http://arxiv.org/abs/1802.04434) Train a NN with compressed (one-bit) gradients
* [Majid Janzamin, Hanie Sedghi, and Anima Anandkumar 2015](https://arxiv.org/abs/1506.08473) Train a two-layer NN provably using tensor methods
* [Kossaifi et al. 2017](http://openaccess.thecvf.com/content_cvpr_2017_workshops/w29/papers/Kossaifi_Tensor_Contraction_Layers_CVPR_2017_paper.pdf) Tensor contraction layers to reduce parameters in NN

Other interesting ideas connecting optimization and deep learning
* [Lin et al. 2018](http://papers.nips.cc/paper/7423-pacgan-the-power-of-two-samples-in-generative-adversarial-networks.pdf) Mode collapse in GANs implies network does not generalize; this paper proposes a fix
* [Armin Askari et al. 2018](http://arxiv.org/abs/1805.01532) Reformulate DNNs as a biconvex problem and use ADMM


## (Deep) Learning Regularizers

* [Bora et al. 2017](https://arxiv.org/abs/1703.03208) Compressed sensing using generative models
* [Chang et al. 2017](http://openaccess.thecvf.com/content_ICCV_2017/papers/Chang_One_Network_to_ICCV_2017_paper.pdf) Solving all inverse problems
* [Mardani et al. 2017](https://arxiv.org/abs/1706.00051) Application to MRI imaging
* [Mardani et al. 2018](http://stanford.edu/~qysun/NIPS2018-neural-proximal-gradient-descent-for-compressive-imaging.pdf) Use a DNN to learn (a proximal map for) the best regularizer and denoise via PGD
* [Lucas et al. 2018](https://ieeexplore.ieee.org/abstract/document/8253590) IEEE review on deep learning for inverse problems in imaging
* [Krull, Buchholz, and Jug 2018](https://arxiv.org/abs/1811.10980) Learn to denoise without clean target images

## Continuous Control and Reinforcement Learning

* [Recht 2018](https://arxiv.org/abs/1806.09460) Reinforcement Learning: connections with continuous control.
* Also consider [the blog posts on this topic](http://www.argmin.net/2018/06/25/outsider-rl/), which are even nicer to read
* See also [Bertsimas 2018](http://web.mit.edu/dimitrib/www/RLbook.html) book on Reinforcement Learning and Optimal Control

## Optimization for Trustworthy Machine Learning

Trustworthy machine learning is an umbrella term that includes
*  Privacy-preserving Statistics and Machine Learning
*  Fairness
*  Interpretability
*  Robust Statistics and Machine Learning
*  Causality
*  Adversarial Examples

Some nice recent paperson the topic that are fair game for this class:
* [Hardt et al. 2016](http://papers.nips.cc/paper/6374-equality-of-opportunity-in-supervised-learning.pdf) Some (optimization-capable) definitions of fairness
* [Hashimoto et al. 2018](https://arxiv.org/abs/1806.08010) Fairness (without group labels!) via robust optimization
* [Goh et al. 2016](http://papers.nips.cc/paper/6315-satisfying-real-world-goals-with-dataset-constraints) Optimization with Dataset Constraints
* [Blum et al. 2018](http://papers.nips.cc/paper/8058-on-preserving-non-discrimination-when-combining-expert-advice.pdf) Can we preserve fairness when combining classifiers?
* [Liu et al. 2018](https://arxiv.org/pdf/1803.04383.pdf) Fairness criteria, when naively applied, can result in unfair behavior over multiple rounds of decisions

<!--
# Check their recent papers for other stuff to add
Elad Hazan
Alex Dimakis (+ Eric Price)
Nati Srebro
Ben Recht (argmin)
Alex Madry (gradientscience)
Sanjeev Arora (offconvex)
Moritz Hardt
Maya Gupta
Jacob Abernethy
Recent best papers at ICML/NIPS

# Questions to ask

* Boumal: what's the best ref on manopt?
* Chouldechova: good fairness readings?
* Andrew Wilson: more good papers
-->
