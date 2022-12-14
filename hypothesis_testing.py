import scipy.stats as stats
import numpy as np


def test_h1(male_dict, female_dict):
    male_sorted = sorted(male_dict.items())
    female_sorted = sorted(female_dict.items())

    years, males = zip(*male_sorted)
    years, females = zip(*female_sorted)

    t, p = stats.ttest_ind(males, females)
    print("t =", t)
    print("p =", p)


def test_h2(female_dict):

    female_sorted = sorted(female_dict.items())
    years, female = zip(*female_sorted)

    female_percentage_change = [((y - female[i - 1]) / female[i - 1]) * 100 for i, y in enumerate(female)][:]

    # Calculate the linear regression line (i.e. the best fit line) for the changes (average slope)
    slope, intercept, r_value, p_value, std_err = stats.linregress(years, female_percentage_change)
    # female_poly_coef = np.polyfit(years, female_percentage_change, 1)
    # female_poly_fit = np.poly1d(female_poly_coef)

    n = len(years)
    k = 1

    f = (r_value ** 2 / (1 - r_value ** 2)) * ((n - k - 1) / k)
    p = stats.f.sf(f, k, n - k - 1)

    print("f =", f)
    print("p =", p)
    print("p =", p_value)
    print("Der Anteil weiblicher Autoren steigt mit einer Steigung von", slope, " % pro Jahr.")


def test_h3(male_dict, female_dict):
    sum = {}
    for year in male_dict.keys():
        sum[year] = male_dict[year] + female_dict[year]

    sum_sorted = sorted(sum.items())
    years, sums = zip(*sum_sorted)

    slope, intercept, r_value, p_value, std_err = stats.linregress(years, sums)

    n = len(years)
    k = 1

    f = (r_value ** 2 / (1 - r_value ** 2)) * ((n - k - 1) / k)
    p = stats.f.sf(f, k, n - k - 1)

    print("f =", f)
    print("p =", p)
    print("Die Anzahl Paper steigt mit einer Steigung von", slope, "pro Jahr.")


def test_h4(male_citation_dict, female_citation_dict):

    male_sorted = sorted(male_citation_dict.items())
    female_sorted = sorted(female_citation_dict.items())

    years, males = zip(*male_sorted)
    years, females = zip(*female_sorted)

    t, p1 = stats.ttest_ind(males, females)
    f, p = stats.f_oneway(males, females)
    print("t =", t)
    print("p1 =", p1)
    print("f =", f)
    print("p =", p)

