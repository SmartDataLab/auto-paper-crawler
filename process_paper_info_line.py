#%%
paper_lines = """
Alon, N., Matias, Y. and Szegedy, M. (1996) The space complexity of approximating the frequency moments. In Proc. 28th A. Symp. Theory of Computing (ed. G. L. Miller), pp. 20-29. New York: Association for Computing Machinery.

Balakrishnan, S., Wainwright, M. J. and Yu, B. (2017) Statistical guarantees for the EM algorithm: from population to sample-based analysis. Ann. Statist., $\mathbf{4 5}, 77-120$.

Bhatia, K., Jain, P. and Kar, P. (2015) Robust regression via hard thresholding. In Advances in Neural Information Processing Systems 28 (eds C. Cortes, N. D. Lawrence, D. D. Lee, M. Sugiyama and R. Garnett), pp. 721-729.

Box, G. E. P. (1953) Non-normality and tests on variances. Biometrika, 40, 318-335.

Brownlees, C., Joly, E. and Lugosi, G. (2015) Empirical risk minimization for heavy-tailed losses. Ann. Statist., $\mathbf{4 3}, 2507-2536$

Bubeck, S. (2015) Convex optimization: algorithms and complexity. Foundns Trends Mach. Learn., 8, 231-357.

Candès, E. J., Li, X., Ma, Y. and Wright, J. (2011) Robust principal component analysis. J. Ass. Comput. Mach., 58, no. 3,11

Catoni, O. (2012) Challenging the empirical mean and empirical variance: a deviation study. Ann. Inst. H. Poincaré, $\mathbf{4 8}, 1148-1185 .$

Charikar, M., Steinhardt, J. and Valiant, G. (2017) Learning from untrusted data. In Proc. 49th A. Symp. Theory of Computing. New York: Association for Computing Machinery.

Chen, M., Gao, C. and Ren, Z. (2016) A general decision theory for Huber's epsilon-contamination model. Electron. J. Statist., 10, 3752-3774.

Chen, M., Gao, C. and Ren, Z. (2018) Robust covariance and scatter matrix estimation under Huber's contamination model. Ann. Statist., 46, 1932-1960.

Chen, Y., Caramanis, C. and Mannor, S. (2013) Robust sparse regression under adversarial corruption. In Proc. 30th Int. Conf. Machine Learning, Atlanta, June 16th-21st, pp. 774-782.

Devroye, L. and Györfi, L. (1985) Nonparametric Density Estimation: the Ll View. New York: Wiley.

Diakonikolas, I., Kamath, G., Kane, D. M., Li, J., Moitra, A. and Stewart, A. (2016) Robust estimators in high dimensions without the computational intractability. In Foundations of Computer Science (ed. I. Dinur), pp. 655-664. New York: Institute of Electrical and Electronics Engineers.

Diakonikolas, I., Kamath, G., Kane, D. M., Li, J., Moitra, A. and Stewart, A. (2017) Being robust (in high dimensions) can be practical. In Proc. Int. Conf. Machine Learning (eds D. Precup and Y. W. Teh), pp. 999 1008

Donoho, D. L. and Liu, R. C. (1988) The "automatic" robustness of minimum distance functionals. Ann. Statist., $16,552-586$

Du, S. S., Balakrishnan, S. and Singh, A. (2017) Computationally efficient robust estimation of sparse functionals. In Proc. 30th Conf. Learning Theory, Amsterdam, July 7th-10th (eds S. Kale and O. Shamir), pp. $169-212$.

Duchi, J. and Namkoong, H. (2016) Variance-based regularization with convex objectives. Preprint arXiv: $1610.02581$

Fan, J., Wang, W. and Zhu, Z. (2016) A shrinkage principle for heavy-tailed data: high-dimensional robust lowrank matrix recovery. Preprint arXiv 1603.08315.

Fischler, M. A. and Bolles, R. C. (1981) Random sample consensus: a paradigm for model fitting with applications to image analysis and automated cartography. Communs $A C M, \mathbf{2 4}, 381-395$. Gao, C. (2017) Robust regression via mutivariate regression depth. Preprint arXiv: $1702.04656 .$ van de Geer, S. (2000) Empirical Processes in $M$-estimation. New York: Cambridge University Press. Hampel, F. R., Ronchetti, E. M., Rousseeuw, P. J. and Stahel, W. A. (2011) Robust Statistics: the Approach based on Influence Functions. New York: Wiley.

Hastings, Jr, C., Mosteller, F., Tukey, J. W. and Winsor, C. P. (1947) Low moments for small samples: a comparative study of order statistics. Ann. Math. Statist., 18, 413-426.

Hopkins, S. B. (2018) Sub-Gaussian mean estimation in polynomial time. Preprint arXiv: 1809.07425.

Hsu, D. and Sabato, S. (2016) Loss minimization and parameter estimation with heavy tails. J. Mach. Learn. Res., 17, no. $18,1-40$

Huber, P. J. (1964) Robust estimation of a location parameter. Ann. Math. Statist., 35, 73-101.

Huber, P. J. (1965) A robust version of the probability ratio test. Ann. Math. Statist., 36, 1753-1758.

Huber, P. J. (1981) Robust Statistics. New York: Wiley.

Jerrum, M. R., Valiant, L. G. and Vazirani, V. V. (1986) Random generation of combinatorial structures from a uniform distribution. Theor. Comput. Sci., 43, 169-188.

Karimi, H., Nutini, J. and Schmidt, M. (2016) Linear convergence of gradient and proximal-gradient methods under the Polyak-Lojasiewicz condition. In Proc. Eur. Conf. Machine Learning and Knowledge Discovery in Databases (eds P. Frasconi, N. Landwehr, G. Manco and J. Vreeken), pp. 795-811. New York: Springer.

Lai, K. A., Rao, A. B. and Vempala, S. (2016) Agnostic estimation of mean and covariance. In Foundations of Computer Science (ed. I. Dinur), pp. 665-674. New York: Institute of Electrical and Electronics Engineers.

Lecué, G. and Lerasle, M. (2017) Robust machine learning by median-of-means: theory and practice. Preprint arXiv: $1711.10306$

Lee, K.-C., Ho, J. and Kriegman, D. J. (2005) Acquiring linear subspaces for face recognition under variable lighting. IEEE Trans. Pattn Anal. Mach. Intell., 27, 684-698.

Lerasle, M. and Oliveira, R. I. (2011) Robust empirical mean estimators. Preprint arXiv:1112.3914.

Loh, P.-L. (2017) Statistical consistency and asymptotic normality for high-dimensional robust $m$-estimators. Ann. Statist., 45, 866-896.

Loh, P.-L. and Wainwright, M. J. (2011) High-dimensional regression with noisy and missing data: provable guarantees with non-convexity. In Advances in Neural Information Processing Systems (eds J. Shaw-Taylor, R. S. Zemel, P. L. Bartlett, F. C. N. Pereira and K. Q. Weinberger), pp. 2726-2734.

Lugosi, G. and Mendelson, S. (2017) Sub-Gaussian estimators of the mean of a random vector. Ann. Statist., $\mathbf{4 5}$, $783-794$

Lugosi, G. and Mendelson, S. (2019) Risk minimization by median-of-means tournaments. J. Eur. Math. Soc., $\mathbf{2 2}, 925-965$

Minsker, S. (2015) Geometric median and robust estimation in Banach spaces. Bernoulli, 21, 2308-2335.

Mizera, I. (2002) On depth and deep points: a calculus. Ann. Statist., 30, 1681-1736.

Nemirovski, A. S. and Yudin, D. B. (1983) Problem Complexity and Method Efficiency in Optimization. New York: Wiley Interscience.

Tibshirani, R. (1996) Regression shrinkage and selection via the lasso. J. R. Statist. Soc. B, 58, 267-288.

Tukey, J. W. (1975) Mathematics and the picturing of data. In Proc. Int. Congr. Mathematicians, vol. 2 (ed. R. D. James), pp. 523-531.

Yatracos, Y. G. (1985) Rates of convergence of minimum distance estimators and Kolmogorov's entropy. Ann. Statist., 13, 768-774.

Yi, X., Park, D., Chen, Y. and Caramanis, C. (2016) Fast algorithms for robust PCA via gradient descent. In Advances in Neural Information Processing Systems 29 (eds D. D. Lee, M. Sugiyama, U. von Luxburg, I. Guyon and R. Garnett), pp. $4152-4160 .$

Zhou, W.-X., Bose, K., Fan, J. and Liu, H. (2018) A new perspective on robust $M$-estimation: finite sample theory and applications to dependence-adjusted multiple testing. Ann. Statist., $\mathbf{4 6}, 1904-1931 .$
"""
paper_list = [one for one in paper_lines.split("\n") if len(one) > 0]
paper_list
# %%
import json

json.dump(paper_list, open("data/paper_list.json", "w"))
# %%
from generate_bibtex import get_bibtex

get_bibtex(paper_list[0])
# %%
bibtex_list = []
import time
from tqdm import tqdm

start = 0
for i in tqdm(range(start, len(paper_list))):
    start = i
    title = paper_list[i]
    bibtex = get_bibtex(title)
    bibtex_list.append(bibtex)
    time.sleep(3)
# %%
file = open("data/su_paper_list.bib", "a+")
for one in bibtex_list:
    file.write(one)
    file.write("\n")
file.close()


#%%
paper_lines2 = """Baranowski, R., Chen, Y. \& Fryzlewicz, P. (2019) Narrowest-Over-Threshold detection of multiple change points and change-point-like features. Journal of the Royal Statistical Society Series B, 81, 649-672.

Barnard, G. A. (1959) Control charts and stochastic processes. Journal of the Royal Statistical Society Series B, 21 , $239-271$

Birgé, L. (2001) An alternative point of view on Lepski's method. In State of the art in probability and statistics (Leiden, 1999). Beachwood, OH: IMS, pp. 113-133.

Boucheron, S., Lugosi, G. \& Massart, P. (2013) Concentration Inequalities: A Nonasymptotic Theory of Independence. Oxford: Oxford University Press.

Caudron, C., White, R. S., Green, R. G., Woods, J., Ágústsdóttir, T., Donaldson, C., et al. (2018) Seismic amplitude ratio analysis of the 2014-15 Bárðarbunga-Holuhraun dike propagation and eruption. Journal of Geophysical Research: Solid Earth $, 123,264-276 .$

Chan, H. P. (2017) Optimal sequential detection in multi-stream data. Annals of Statistics, 45, 2736-2763.

Chen, Y., Wang, T. \& Samworth, R. J. (2020) ocd: high-dimensional, multiscale online changepoint detection. Available from \href{https://cran.r-project.org/web/packages/ocd/index.html}{https://cran.r-project.org/web/packages/ocd/index.html}.

Chen, Y., Wang, T. \& Samworth, R. J. (2021) Online supplementary material to 'High-dimensional, multiscale online changepoint detection'. Submitted.

Cho, H. (2016) Change-point detection in panel data via double CUSUM statistic. Electronic Journal of Statistics, $10,2000-2038$

Chu, C.-S. J., Stinchcombe, M. \& White, H. (1996) Monitoring structural change. Econometrica, 64, 1045-1065.
$$
\begin{aligned}
& \overline{\mathbb{E}}_{\theta}^{w \mathrm{c}}(N)=\overline{\mathbb{E}}_{\theta}^{\mathrm{wc}}\left[\left(N^{\text {diag }} \wedge N^{\mathrm{off}, \mathrm{d}}\right) \wedge\left(N^{\mathrm{diag}} \wedge N^{\mathrm{off}, \mathrm{s}}\right)\right] \\
& \leq \bar{E}_{\theta}^{\mathrm{Wc}}\left[\left(N^{\mathrm{diag}} \wedge N^{\mathrm{off}, \mathrm{d}}\right)\right] \wedge \overline{\mathbb{E}}_{\theta}^{\mathrm{Wc}}\left[\left(N^{\mathrm{diag}} \wedge N^{\mathrm{off}, \mathrm{s}}\right)\right] 
\end{aligned}
$$
Collier, O., Comminges, L. \& Tsybakov, A. B. (2017) Minimax estimation of linear and quadratic functionals on sparsity classes. Annals of Statistics, 45, 923-958.

Csörgő, M. \& Horváth, L. (1997) Limit Theorems in Change-Point Analysis. New York: John Wiley and Sons.

Duncan, A. J. (1952) Quality Control and Industrial Statistics. Chicago: Richard D. Irwin Professional Publishing Inc.

Enikeeva, F. \& Harchaoui, Z. (2019) High-dimensional change-point detection under sparse alternatives. Annals of Statistics, 47, 2051-2079.

Fearnhead, P. \& Liu, Z. (2007) On-line inference for multiple changepoint problems. Journal of the Royal Statistical Society Series $B, 69,589-605$.

Frick, K., Munk, A. \& Sieling, H. (2014) Multiscale change point inference. Journal of the Royal Statistical Society Series $B, 76,495-580 .$

Gösmann, J., Stoehr, C., Heiny, J. \& Dette, H. (2020) Sequential change point detection in high dimensional time series. Available from \href{https://arxiv.org/abs/2006.00636}{https://arxiv.org/abs/2006.00636}.

Hoeffding, W. (1963) Probability inequalities for sums of bounded random variables. Journal of the American Statistical Association, $58,13-30$.

Horváth, L. \& Rice, G. (2014) Extensions of some classical methods in change point analysis. TEST, 23 , $219-255$

Killick, R., Fearnhead, P. \& Eckley, I.A. (2012) Optimal detection of changepoints with a linear computational cost. Journal of the American Statistical Association, 107, 1590-1598.

Komlós, J. Major, P. \& Tusnády, G. (1976) An approximation of partial sums of independent RVs, and the sample DF. II. Z. Wahrscheinlichkeitstheorie verw. Gebiete, 34, 33-58.

Laurent, B. \& Massart, P. (2000) Adaptive estimation of a quadratic functional by model selection. Annals of Statistics, 28, 1302-1338.

Leisch, F., Hornik, K. \& Kuan, C.-M. (2000) Monitoring structural changes with the generalized fluctuation test. Econometric Theory, 16,835-854.

Liu, H., Gao, C. \& Samworth, R. J. (2021) Minimax rates in sparse, high-dimensional changepoint detection. Annals of Statistics, 49, 1081-1112.

Lorden, G. (1971) Procedures for reacting to a change in distribution. Annals of Mathematical Statistics, 42, $1897-1908 .$

Mei, Y. (2010) Efficient scalable schemes for monitoring a large number of data streams. Biometrika, 97, $419-433$

Mörters, P. \& Peres, Y. (2010) Brownian motion. Cambridge: Cambridge University Press

Oakland, J.S. (2007) Statistical Process Control 6th edn. London: Routledge.

Padilla, O.H.M., Yu, Y., Wang, D. \& Rinaldo, A. (2019) Optimal nonparametric multivariate change point detection and localization. Available from \href{https://arxiv.org/abs/1910.13289}{https://arxiv.org/abs/1910.13289}.

Page, E.S. (1954) Continuous inspection schemes. Biometrika, 41, 100-115.

Page, E.S. (1955) A test for a change in a parameter occurring at an unknown point. Biometrika, 42, 523-527.

Soh, Y.S. \& Chandrasekaran, V. (2017) High-dimensional change-point estimation: Combining filtering with convex optimization. Applied and Computational Harmonic Analysis, 43, 122-147.

Tartakovsky, A.G., Rozovskii, B.L., Blažek, R.B. \& Kim, H. (2006) Detection of intrusions in information systems by sequential change-point methods. Statistical Methodology, 3, 252-293.

Tartakovsky, A., Nikiforov, I. \& Basseville, M. (2014) Sequential Analysis: Hypothesis Testing and Changepoint Detection. London: Chapman and Hall.

van der Vaart, A.W. \& Wellner, J.A. (1996) Weak Convergence and Empirical Processes. New York: Springer.

Wang, T. \& Samworth, R. J. (2018) High dimensional change point estimation via sparse projection. Journal of the Royal Statistical Society Series $B, 80,57-83 .$

Wang, D., Yu, Y. \& Rinaldo, A. (2018) Univariate mean change point detection: penalization, CUSUM and optimality. Available from \href{https://arxiv.org/abs/1810.09498v4}{https://arxiv.org/abs/1810.09498v4}.

Xie, Y. \& Siegmund, D. (2013) Sequential multi-sensor change-point detection. Annals of Statistics, 41, 670-692.

Xie, L., Xie, Y. \& Moustakides, G.V. (2019) Asynchronous multi-sensor change-point detection for seismic tremors. IEEE International Symposium on Information Theory (ISIT), 787-791.

Zeileis, A., Leisch, F., Kleiber, C. \& Hornik, K. (2005) Monitoring structural change in dynamic econometric models. Journal of Applied Econometrics, 20, 99-121. Zou, C., Wang, Z., Zi, X. \& Jiang, W. (2015) An efficient online monitoring method for high-dimensional data streams. Technometrics, $57,374-387 .$"""
#%%
paper_list = [one for one in paper_lines2.split("\n") if len(one) > 0]
paper_list
bibtex_list = []
import time
from tqdm import tqdm

start = 0
for i in tqdm(range(start, len(paper_list))):
    start = i
    title = paper_list[i]
    bibtex = get_bibtex(title)
    bibtex_list.append(bibtex)
    time.sleep(3)
# %%
file = open("data/txy_paper_list.bib", "a+")
for one in bibtex_list:
    file.write(one)
    file.write("\n")
file.close()