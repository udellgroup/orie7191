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
% understanding implicit regularizers and learning better explicit regularizers for deep learning,
connections between control theory and modern reinforcement learning,
and optimization for trustworthy machine learning (including fair, causal, or interpretable models).
Topics may change according to student interest.

The format will consist of student-guided discussion on papers.
The course will culminate in a final research project
which will constitute a majority of the grade.
Students will deliver short presentations on their projects in class
in addition to written reports.

# Contact

Join our workspace on [slack](https://join.slack.com/t/orie7191/signup) (use your cornell.edu address)
for general questions and comments.

Office hours will be chosen via an in-class poll.
You can also talk with Prof. Udell after class or
contact her by email at udell@cornell.edu to set up an appointment.

# Course format and requirements

Students are required to attend class, with at most two absences.
(Up to two classes may also be attended remotely via [Zoom](https://zoom.us/j/7221862735)
by prior arrangement with the instructor.)

Course grades have four components (weights in parentheses):

* **Reviews** (.3): Students will write reviews of half of the papers we read for class and upload them to [CMT]().
* **Quiz** (.1): Each class will begin with a two-question quiz to make sure students read the paper.
Grading on this portion of the course will be nonlinear (eg, 0 points if too few quiz questions are answered correctly).
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

* [barvinok1995problems], [pataki1998rank] show that rank of exact solutions to SDP with m linear constraints grow as O(sqrt(m))
* [barvinok2002course] p. 140: rank of epsilon approximation to a PSD matrix satisfying m linear constraints grows as log(m / epsilon)
* [so2008unified] Similar to above low rank approximation idea, more algorithmic. Still requires solving the SDP first.
* [hazan2008sparse] suggests using Franke Wolfe for semidefinite programming
* [garber2011approximating] integrates the above idea into a method to produce approximate solutions of SDP
% * Hazan multiplicative weights?
* [jaggi2013revisiting] Solving matrix completion with Frank Wolfe ensures rank is bounded by number of iterations
* [yurtsever2017sketchy] The first storage-optimal convex method for matrix completion
% * Facial reduction

### Nonsmooth convex low rank optimization

* [burer2003nonlinear] Original paper proposing factored formulation for solving SDPs
* [journee2010low] How to escape a saddle point with gradient information
* [boumal2014manopt]
* [boumal2016non] The non-convex Burer-Monteiro approach works on smooth semidefinite programs
* [bhojanapalli2018smoothed] Smoothed analysis of BM factorization
* finding local minima efficiently
  * [lee2016gradient] GD only converges to minimizers
  * [lee2017first] More generally, first order methods avoid saddle points
* [gunasekar2017implicit] Gradient descent on factored formulation of matrix completion implicitly regularized the nuclear norm
* [bhojanapalli2016global] [ge2016matrix] The factored formulation of matrix completion from incoherent measurements has no spurious local minima
* [ma2017implicit] Gradient descent (implicitly) imposes regularization for a wide variety of statistical models
%* cubic regularization?
%* adding noise?
%* fancy provable stuff by Allen-Zhu?

<!-- Streaming low rank optimization

* grouse
* balzano recent review -->

## Optimization for Deep Learning

Is optimization enough? Is SGD necessary to provide implicit regularization?
  * [dauphin2014identifying] Is the quality of a critical point proportional to the number of directions of positive curvature? % NB has since been discredited (?)
  * [zhang2016understanding] (Not very) deep nets can exactly fit noise. So why do they generalize well for real data?
  * [hardt2015train] Stability of SGD means that good solutions found quickly should generalize well
  * [keskar2016large] Large batch training and sharp minima % not yet read
  * [hoffer2017train] A proposal to decrease the generalization gap when using large batch sizes, proposing different explanation than [keskar2016large] % I don't understand this yet
  * [rahimi2009weighted] + [Rahimi Test of Time Talk at NeurIPS 2017](https://www.youtube.com/watch?v=Qi1Yry33TQE)
  * [kawaguchi2017generalization] Generalization in deep learning % haven't read yet
  * [neyshabur2018role] Maybe deeps nets aren't as overparametrized as they seem
  * [neyshabur2017exploring] Do (particular) optimization algorithms implicitly regularize the solution found?
  * [gunasekar2018characterizing] Studies the same question as above, with new theoretical results
  * [nacson2018convergence] Studies the same question as above in a simpler case

Can we improve deep learning using more sophisticated ideas from optimization?
* Gradient science blog posts [1](https://gradientscience.org/intro_adversarial/) [2](https://gradientscience.org/robust_opt_pt1/) [3](https://gradientscience.org/robust_opt_pt2/) expound the thesis that GANs are better fit by robust optimization
* [sinha2017certifiable] Distributionally robust optimization foils adversarial examples
* Gradient science blog posts on [batch normalization](https://gradientscience.org/batchnorm/) attempt to explain its success as a change of geometry
* [neyshabur2015path] Why not optimize in a geometry invariant to rescalings of the parameters that don't affect the output?
* [wilson2017marginal] Adaptive optimization methods (which learn the geometry from the iterates) can be worse than useless

Learn better with fewer parameters
  * [chen2018neural] Treat number of layers as a continuous parameter (!)
  * [bernstein2018sign] Train a NN with compressed (one-bit) gradients
  * [janzamin2015generalization] Train a two-layer NN provably using tensor methods
  * [kossaifi2017tensor] Tensor contraction layers to reduce parameters in NN

Other interesting ideas connecting optimization and deep learning
* [lin2018pacgan] Mode collapse in GANs implies network does not generalize; this paper proposes a fix
* [askari2018lifted] Reformulate DNNs as a biconvex problem and use ADMM % similar work by Donald Goldfarb?


## (Deep) Learning Regularizers

* [bora2017compressed] Compressed sensing using generative models %(based on my conversation with Eric at OpenAI)
* [chang2017one] Solving all inverse problems
* [mardani2017deep] Application to MRI imaging
* [mardani2018neural] Use a DNN to learn (a proximal map for) the best regularizer and denoise via PGD
* [lucas2018using] IEEE review on deep learning for inverse problems in imaging
* [krull2018noise2void] Learn to denoise without clean target images
% * [hand2018global] Global Guarantees for Enforcing Deep Generative Priors by Empirical Risk % check and see if this is vacuous theory...

## Continuous Control and Reinforcement Learning

* [recht2018tour] Reinforcement Learning: connections with continuous control.
* Also consider [the blog posts on this topic](http://www.argmin.net/2018/06/25/outsider-rl/), which are even nicer to read
% * [Post 10 (PID)](http://www.argmin.net/2018/04/19/pid/) vs learning-to-learn literature on learning domain-specific opt methods
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
* [hardt2016equality] Some (optimization-capable) definitions of fairness
* [hashimoto2018fairness] Fairness (without group labels!) via robust optimization
* [goh2016satisfying] Optimization with Dataset Constraints
* [blum2018preserving] Can we preserve fairness when combining classifiers?
* [liu2018delayed] Fairness criteria, when naively applied, can result in unfair behavior over multiple rounds of decisions

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
